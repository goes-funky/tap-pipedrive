from tap_pipedrive.stream import PipedriveIterStream


class DealsSummaryStream(PipedriveIterStream):
    base_endpoint = '/deals/summary'
    id_endpoint = '/deals/summary?stage_id={}'
    schema = 'deals_summary'
    state_field = None
    key_properties = ['stage_id']

    def get_name(self):
        return self.schema

    def update_endpoint(self, stage_id):
        self.endpoint = self.id_endpoint.format(stage_id)

    def process_row(self, row):
        # TODO: here we transform row data
        print('.................', row)
