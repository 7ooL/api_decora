# Leviton Cloud Services API model Geocoder.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from ..base_model import BaseModel


class Geocoder(BaseModel):
    def __init__(self, session, model_id=None):
        super(Geocoder, self).__init__(session, model_id)

    @classmethod
    def geocode(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Geocoder/geocode"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/Geocoder/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    @classmethod
    def normalize(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Geocoder/normalize"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def reverse(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Geocoder/reverse"
        return session.call_api(api, attribs, 'get')

