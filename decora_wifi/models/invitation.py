# Leviton Cloud Services API model Invitation.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from homeauto.api_decora.decora_wifi.base_model import BaseModel


class Invitation(BaseModel):
    def __init__(self, session, model_id=None):
        super(Invitation, self).__init__(session, model_id)

    def accept(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/accept".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def count_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/permissions/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations"
        return session.call_api(api, attribs, 'post')

    def create_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/permissions".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def delete_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/permissions".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_permissions(self, permission_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/permissions/{1}".format(self._id, permission_id)
        return self._session.call_api(api, attribs, 'delete')

    def find_by_id_permissions(self, permission_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/permissions/{1}".format(self._id, permission_id)
        data = self._session.call_api(api, attribs, 'get')

        from .permission import Permission
        model = Permission(self._session, data['id'])
        model.data = data
        return model

    def refresh(self):
        api = "/Invitations/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_location(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/location".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .location import Location
        model = Location(self._session, data['id'])
        model.data = data
        return model

    def get_management_tier(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/managementTier".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .management_tier import ManagementTier
        model = ManagementTier(self._session, data['id'])
        model.data = data
        return model

    def get_organization(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/organization".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .organization import Organization
        model = Organization(self._session, data['id'])
        model.data = data
        return model

    def get_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/permissions".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .permission import Permission
        result = []
        if items is not None:
            for data in items:
                model = Permission(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_person(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/person".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .person import Person
        model = Person(self._session, data['id'])
        model.data = data
        return model

    def get_residence(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/residence".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .residence import Residence
        model = Residence(self._session, data['id'])
        model.data = data
        return model

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    def update_by_id_permissions(self, permission_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/{0}/permissions/{1}".format(self._id, permission_id)
        data = self._session.call_api(api, attribs, 'put')

        from .permission import Permission
        model = Permission(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Invitations/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

