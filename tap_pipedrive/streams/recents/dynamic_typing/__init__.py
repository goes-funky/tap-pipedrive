import singer
from requests import RequestException
from tap_pipedrive.streams.recents import RecentsStream, DealsDynamicStream, DealDetails
import re

logger = singer.get_logger()


def get_dynamic_schema(stream):
    # custom_map = {}
    if not stream.schema_cache:
        schema = stream.load_schema()

        try:
            fields_response = stream.tap.execute_request(endpoint=stream.fields_endpoint)
        except (ConnectionError, RequestException) as e:
            raise e

        try:
            payload = fields_response.json()  # Verifying response in execute_request

            for property in payload['data']:
                if property['key'] not in stream.static_fields:
                    logger.debug(property['key'], property['field_type'], property['mandatory_flag'])

                    if property['key'] in schema['properties']:
                        logger.warn('Dynamic property "{}" overrides with type {} existing entry in ' \
                                    'static JSON schema of {} stream.'.format(
                            property['key'],
                            property['field_type'],
                            stream.schema
                        )
                        )

                    property_content = {
                        'type': []
                    }

                    if property['field_type'] in ['int']:
                        property_content['type'].append('integer')

                    elif property['field_type'] in ['timestamp']:
                        property_content['type'].append('string')
                        property_content['format'] = 'date-time'

                    else:
                        property_content['type'].append('string')

                    # allow all dynamic properties to be null since this
                    # happens in practice probably because a property could
                    # be marked mandatory for some amount of time and not
                    # mandatory for another amount of time
                    property_content['type'].append('null')
                    if re.search('^([a-zA-Z0-9]{32,})', property['key']):
                        new_field_id = re.sub('[^a-zA-Z0-9_]', '_', property['name'].lower())
                        if new_field_id[0].isdigit():
                            new_field_id = "c_" + new_field_id
                        stream.schema_custom_fields[property['key']] = new_field_id
                        schema['properties'][new_field_id] = property_content
                    else:
                        schema['properties'][property['key']] = property_content

        except Exception as e:
            raise e

        stream.schema_cache = schema
    return stream.schema_cache


class DynamicTypingRecentsStream(RecentsStream):
    schema_path = 'schemas/recents/dynamic_typing/{}.json'
    static_fields = []
    fields_endpoint = ''

    def get_schema(self):
        return get_dynamic_schema(self)


class DynamicsDeals(DealsDynamicStream):
    schema_path = 'schemas/recents/dynamic_typing/{}.json'
    static_fields = []
    fields_endpoint = ''

    def get_schema(self):
        return get_dynamic_schema(self)


class DynamicsDealDetails(DealDetails):
    schema_path = 'schemas/recents/dynamic_typing/{}.json'
    static_fields = []
    fields_endpoint = ''

    def get_schema(self):
        return get_dynamic_schema(self)
