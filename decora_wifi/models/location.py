# Leviton Cloud Services API model Location.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from ..base_model import BaseModel


class Location(BaseModel):
    def __init__(self, session, model_id=None):
        super(Location, self).__init__(session, model_id)

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/count"
        return session.call_api(api, attribs, 'get')

    def count_feed_items(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/feedItems/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_holidays(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/holidays/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_installations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations"
        return session.call_api(api, attribs, 'post')

    def create_holidays(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/holidays".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_installations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations"
        return session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_holidays(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/holidays".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_installations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_holidays(self, holiday_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/holidays/{1}".format(self._id, holiday_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_installations(self, installation_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations/{1}".format(self._id, installation_id)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = Location(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    def find_by_id_feed_items(self, feed_item_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/feedItems/{1}".format(self._id, feed_item_id)
        data = self._session.call_api(api, attribs, 'get')

        from .feed_item import FeedItem
        model = FeedItem(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_holidays(self, holiday_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/holidays/{1}".format(self._id, holiday_id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_installations(self, installation_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations/{1}".format(self._id, installation_id)
        data = self._session.call_api(api, attribs, 'get')

        from .installation import Installation
        model = Installation(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/Locations/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_feed_items(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/feedItems".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .feed_item import FeedItem
        result = []
        if items is not None:
            for data in items:
                model = FeedItem(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_holidays(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/holidays".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_installations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .installation import Installation
        result = []
        if items is not None:
            for data in items:
                model = Installation(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_management_tier(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/managementTier".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .management_tier import ManagementTier
        model = ManagementTier(self._session, data['id'])
        model.data = data
        return model

    def get_organization(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/organization".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .organization import Organization
        model = Organization(self._session, data['id'])
        model.data = data
        return model

    def installers_near(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installersNear".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    def update_by_id_holidays(self, holiday_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/holidays/{1}".format(self._id, holiday_id)
        return self._session.call_api(api, attribs, 'put')

    def update_by_id_installations(self, installation_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations/{1}".format(self._id, installation_id)
        data = self._session.call_api(api, attribs, 'put')

        from .installation import Installation
        model = Installation(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations"
        data = session.call_api(api, attribs, 'put')

        model = Location(session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

