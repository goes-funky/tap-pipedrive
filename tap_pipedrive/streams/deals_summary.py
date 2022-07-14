from tap_pipedrive.stream import PipedriveIterStream

# This stream gets first the stages and for each stage id gets the deal summary, but uses the same flow as other
# streams that get first the deals and foreach deal gets the properties
class DealsSummaryStream(PipedriveIterStream):
    base_endpoint = 'stages'
    id_endpoint = '/deals/summary?stage_id={}'
    schema = 'deals_summary'
    state_field = None
    key_properties = ['stage_id']
    stage_id = None

    def get_name(self):
        return self.schema

    def update_endpoint(self, stage_id):
        self.stage_id = stage_id
        self.endpoint = self.id_endpoint.format(stage_id)

    def add_currency(self, row):
        new_list = []
        for elm in row:
            row[elm]['currency'] = elm
            new_list.append(row[elm])
        return new_list

    def process_row(self, row):
        # add currency field
        row['stage_id'] = self.stage_id
        if row['total_count'] > 0:
            row['values_total'] = self.add_currency(row['values_total'])
            row['weighted_values_total'] = self.add_currency(row['weighted_values_total'])
        return row