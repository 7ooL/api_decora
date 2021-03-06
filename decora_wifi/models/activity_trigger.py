# Leviton Cloud Services API model ActivityTrigger.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from ..base_model import BaseModel


class ActivityTrigger(BaseModel):
    def __init__(self, session, model_id=None):
        super(ActivityTrigger, self).__init__(session, model_id)

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/count"
        return session.call_api(api, attribs, 'get')

    def count_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/activities/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers"
        return session.call_api(api, attribs, 'post')

    def create_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/activities".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers"
        return session.call_api(api, attribs, 'post')

    def delete_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/activities".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_activities(self, activity_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/activities/{1}".format(self._id, activity_id)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = ActivityTrigger(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    def find_by_id_activities(self, activity_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/activities/{1}".format(self._id, activity_id)
        data = self._session.call_api(api, attribs, 'get')

        from .activity import Activity
        model = Activity(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/ActivityTriggers/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/activities".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .activity import Activity
        result = []
        if items is not None:
            for data in items:
                model = Activity(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_area(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/area".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .area import Area
        model = Area(self._session, data['id'])
        model.data = data
        return model

    def get_load(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/load".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .load import Load
        model = Load(self._session, data['id'])
        model.data = data
        return model

    def get_schedule(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/schedule".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_sensor(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/sensor".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .sensor import Sensor
        model = Sensor(self._session, data['id'])
        model.data = data
        return model

    def get_shade(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/shade".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .shade import Shade
        model = Shade(self._session, data['id'])
        model.data = data
        return model

    def get_thermostat(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/thermostat".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .thermostat import Thermostat
        model = Thermostat(self._session, data['id'])
        model.data = data
        return model

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    def update_by_id_activities(self, activity_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/activities/{1}".format(self._id, activity_id)
        data = self._session.call_api(api, attribs, 'put')

        from .activity import Activity
        model = Activity(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers"
        data = session.call_api(api, attribs, 'put')

        model = ActivityTrigger(session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

