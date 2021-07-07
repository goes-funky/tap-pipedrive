import singer
from tap_pipedrive.stream import PipedriveIterStream


class DealStageChangeStream(PipedriveIterStream):
    base_endpoint = 'deals'
    id_endpoint = 'deals/{0}/flow?items={1}'
    schema = 'dealflow'
    state_field = 'log_time'
    key_properties = ['id', ]
    items = "call,activity,plannedActivity,change,note,deal,file,dealChange,personChange,organizationChange," \
            "follower,dealFollower,personFollower,organizationFollower,participant,comment,mailMessage," \
            "mailMessageWithAttachment,invoice,document,marketing_campaign_stat,marketing_status_change"

    def get_name(self):
        return self.schema

    def process_row(self, row):
        # grab only rows that are dealChange objects with changes in add_time or stage_id
        if row['object'] == 'dealChange':
            if row['data']['field_key'] == 'add_time' or row['data']['field_key'] == 'stage_id':
                return row['data']

    def update_endpoint(self, deal_id):
        self.endpoint = self.id_endpoint.format(deal_id, self.items)
