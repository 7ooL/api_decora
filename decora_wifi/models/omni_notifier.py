# Leviton Cloud Services API model OmniNotifier.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from homeauto.api_decora.decora_wifi.base_model import BaseModel


class OmniNotifier(BaseModel):
    def __init__(self, session, model_id=None):
        super(OmniNotifier, self).__init__(session, model_id)

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/count"
        return session.call_api(api, attribs, 'get')

    def count_omni_notifier_emails(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/omniNotifierEmails/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers"
        return session.call_api(api, attribs, 'post')

    def create_omni_notifier_emails(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/omniNotifierEmails".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_omni_notifier_emails(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/omniNotifierEmails".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_omni_notifier_emails(self, omni_notifier_email_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/omniNotifierEmails/{1}".format(self._id, omni_notifier_email_id)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = OmniNotifier(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    def find_by_id_omni_notifier_emails(self, omni_notifier_email_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/omniNotifierEmails/{1}".format(self._id, omni_notifier_email_id)
        data = self._session.call_api(api, attribs, 'get')

        from .omni_notifier_email import OmniNotifierEmail
        model = OmniNotifierEmail(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/OmniNotifiers/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_omni_notifier_emails(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/omniNotifierEmails".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .omni_notifier_email import OmniNotifierEmail
        result = []
        if items is not None:
            for data in items:
                model = OmniNotifierEmail(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_residence(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/residence".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .residence import Residence
        model = Residence(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def get_session_id(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/getSessionId"
        return session.call_api(api, attribs, 'get')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def send_email(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/sendEmail"
        return session.call_api(api, attribs, 'post')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    def update_by_id_omni_notifier_emails(self, omni_notifier_email_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/omniNotifierEmails/{1}".format(self._id, omni_notifier_email_id)
        data = self._session.call_api(api, attribs, 'put')

        from .omni_notifier_email import OmniNotifierEmail
        model = OmniNotifierEmail(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers"
        data = session.call_api(api, attribs, 'put')

        model = OmniNotifier(session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

