from tap_pipedrive.streams.recents.dynamic_typing import DynamicsDealDetails


class DealDetailsStream(DynamicsDealDetails):
    base_endpoint = 'deals'
    id_endpoint = 'deals/{}'
    schema = 'deal_details'
    state_field = None
    key_properties = ['id']
    fields_endpoint = 'dealFields'


    def get_name(self):
        return self.schema

    def update_endpoint(self, deal_id):
        self.endpoint = self.id_endpoint.format(deal_id)
