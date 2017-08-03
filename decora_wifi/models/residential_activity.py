# Leviton Cloud Services API model ResidentialActivity.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class ResidentialActivity(BaseModel):
    def __init__(self, session, model_id=None):
        super(ResidentialActivity, self).__init__(session, model_id)

    def count(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_residence_residential_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def count_residential_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/:id/residentialActions/count"
        return session.call_api(api, attribs, 'get')

    def create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_residence_residential_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_residence_residential_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_residential_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/:id/residentialActions"
        return session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_residence_residential_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_residential_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/:id/residentialActions"
        return session.call_api(api, attribs, 'delete')

    def destroy_by_id_residence_residential_activities(self, residential_activity, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities/{1}".format(self._id, residential_activity)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_residential_actions(cls, session, residential_action, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/:id/residentialActions/{0}".format(residential_action)
        return session.call_api(api, attribs, 'delete')

    def execute(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/execute".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_residence_residential_activities(self, residential_activity, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities/{1}".format(self._id, residential_activity)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_residential_actions(cls, session, residential_action, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/:id/residentialActions/{0}".format(residential_action)
        return session.call_api(api, attribs, 'get')

    def find_one(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/findOne".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.set_model_data(data)
        return self

        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_residence(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/:id/residence"
        return session.call_api(api, attribs, 'get')

    def get_residence_residential_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_residential_action_residential_activity(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActions/{0}/residentialActivity".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_residential_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/:id/residentialActions"
        return session.call_api(api, attribs, 'get')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_or_create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/replaceOrCreate".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def update_attributes(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/:id"
        return session.call_api(api, attribs, 'put')

    def update_by_id_residence_residential_activities(self, residential_activity, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities/{1}".format(self._id, residential_activity)
        return self._session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_residential_actions(cls, session, residential_action, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/:id/residentialActions/{0}".format(residential_action)
        return session.call_api(api, attribs, 'put')

    def upsert(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities".format(self._id)
        return self._session.call_api(api, attribs, 'put')

    def upsert_with_where(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialActivities/upsertWithWhere".format(self._id)
        return self._session.call_api(api, attribs, 'post')
