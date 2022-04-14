from tap_pipedrive.stream import PipedriveStream


class DealsStream(PipedriveStream):
    endpoint = 'deals'
    schema = 'deals'
    key_properties = ['id', ]


class DeletedDealsStream(DealsStream):

    def write_schema(self):
        pass

    def update_request_params(self, params):
        params.update({
            'status': 'deleted'
        })
        return params
