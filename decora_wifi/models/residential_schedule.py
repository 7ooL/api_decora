# Leviton Cloud Services API model ResidentialSchedule.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from homeauto.api_decora.decora_wifi.base_model import BaseModel


class ResidentialSchedule(BaseModel):
    def __init__(self, session, model_id=None):
        super(ResidentialSchedule, self).__init__(session, model_id)

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/count"
        return session.call_api(api, attribs, 'get')

    def count_residential_actions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}/residentialActions/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules"
        return session.call_api(api, attribs, 'post')

    def create_residential_actions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}/residentialActions".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_residential_actions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}/residentialActions".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_residential_actions(self, residential_action_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}/residentialActions/{1}".format(self._id, residential_action_id)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = ResidentialSchedule(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    def find_by_id_residential_actions(self, residential_action_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}/residentialActions/{1}".format(self._id, residential_action_id)
        data = self._session.call_api(api, attribs, 'get')

        from .residential_action import ResidentialAction
        model = ResidentialAction(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/ResidentialSchedules/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_residence(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}/residence".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .residence import Residence
        model = Residence(self._session, data['id'])
        model.data = data
        return model

    def get_residential_actions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}/residentialActions".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .residential_action import ResidentialAction
        result = []
        if items is not None:
            for data in items:
                model = ResidentialAction(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    def update_by_id_residential_actions(self, residential_action_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/{0}/residentialActions/{1}".format(self._id, residential_action_id)
        data = self._session.call_api(api, attribs, 'put')

        from .residential_action import ResidentialAction
        model = ResidentialAction(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules"
        data = session.call_api(api, attribs, 'put')

        model = ResidentialSchedule(session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ResidentialSchedules/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

