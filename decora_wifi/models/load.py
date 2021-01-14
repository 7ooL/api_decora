# Leviton Cloud Services API model Load.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from ..base_model import BaseModel


class Load(BaseModel):
    def __init__(self, session, model_id=None):
        super(Load, self).__init__(session, model_id)

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/count"
        return session.call_api(api, attribs, 'get')

    def count_activity_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/activityTriggers/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_feed_items(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/feedItems/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_load_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/loadSnapshots/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads"
        return session.call_api(api, attribs, 'post')

    def create_activity_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/activityTriggers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_load_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/loadSnapshots".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads"
        return session.call_api(api, attribs, 'post')

    def delete_activity_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/activityTriggers".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_load_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/loadSnapshots".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_activity_triggers(self, activity_trigger_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/activityTriggers/{1}".format(self._id, activity_trigger_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_load_snapshots(self, load_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/loadSnapshots/{1}".format(self._id, load_snapshot_id)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = Load(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    def find_by_id_activity_triggers(self, activity_trigger_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/activityTriggers/{1}".format(self._id, activity_trigger_id)
        data = self._session.call_api(api, attribs, 'get')

        from .activity_trigger import ActivityTrigger
        model = ActivityTrigger(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_feed_items(self, feed_item_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/feedItems/{1}".format(self._id, feed_item_id)
        data = self._session.call_api(api, attribs, 'get')

        from .feed_item import FeedItem
        model = FeedItem(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_load_snapshots(self, load_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/loadSnapshots/{1}".format(self._id, load_snapshot_id)
        data = self._session.call_api(api, attribs, 'get')

        from .load_snapshot import LoadSnapshot
        model = LoadSnapshot(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/Loads/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_activity_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/activityTriggers".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .activity_trigger import ActivityTrigger
        result = []
        if items is not None:
            for data in items:
                model = ActivityTrigger(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_area(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/area".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .area import Area
        model = Area(self._session, data['id'])
        model.data = data
        return model

    def get_device_definition(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/deviceDefinition".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_feed_items(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/feedItems".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .feed_item import FeedItem
        result = []
        if items is not None:
            for data in items:
                model = FeedItem(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/installation".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .installation import Installation
        model = Installation(self._session, data['id'])
        model.data = data
        return model

    def get_load_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/loadSnapshots".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .load_snapshot import LoadSnapshot
        result = []
        if items is not None:
            for data in items:
                model = LoadSnapshot(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    def update_by_id_activity_triggers(self, activity_trigger_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/activityTriggers/{1}".format(self._id, activity_trigger_id)
        data = self._session.call_api(api, attribs, 'put')

        from .activity_trigger import ActivityTrigger
        model = ActivityTrigger(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_load_snapshots(self, load_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/loadSnapshots/{1}".format(self._id, load_snapshot_id)
        data = self._session.call_api(api, attribs, 'put')

        from .load_snapshot import LoadSnapshot
        model = LoadSnapshot(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads"
        data = session.call_api(api, attribs, 'put')

        model = Load(session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

