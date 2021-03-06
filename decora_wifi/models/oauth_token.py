# Leviton Cloud Services API model OauthToken.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from ..base_model import BaseModel


class OauthToken(BaseModel):
    def __init__(self, session, model_id=None):
        super(OauthToken, self).__init__(session, model_id)

    @classmethod
    def control_device(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/controlDevice"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens"
        return session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def discover_devices(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/discoverDevices"
        return session.call_api(api, attribs, 'get')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = OauthToken(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/OauthTokens/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_api_partner(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/{0}/apiPartner".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .api_partner import ApiPartner
        model = ApiPartner(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def poll_device(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/pollDevice"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def subscribe_to_notifications(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/subscribeToNotifications"
        return session.call_api(api, attribs, 'post')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens"
        data = session.call_api(api, attribs, 'put')

        model = OauthToken(session, data['id'])
        model.data = data
        return model

