# -*- coding: utf-8 -*-

"""Main module."""

import copy

from hammock import Hammock


class METRC:
    """Class for wrapping requests to the METRC Web API"""

    def __init__(self, base_path, vendor_key, user_key, license_number, api_version="v1", **kwargs):
        self.base_path = base_path
        self.auth = (vendor_key, user_key)
        self.api_version = api_version
        self.params = {"licenseNumber": license_number}

        self._name = base_path
        self._parent = None
        self._endpoint = Hammock(self.base_path, auth=self.auth, params=self.params, **kwargs)

    def __repr__(self):
        return self._url()

    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)

        return self._spawn(name)

    def __call__(self, *args):
        return self._chain(*args)

    def __iter__(self):
        current = self
        while current:
            if current._name:
                yield current
            current = current._parent

    def _spawn(self, name):
        child = copy.copy(self)

        if not child._parent:
            child._name = name + "/" + self.api_version
        else:
            child._name = name

        child._parent = self
        return child

    def _chain(self, *args):
        chain = self
        for arg in args:
            chain = chain._spawn(str(arg))
        return chain

    def _url(self, *args):
        path_comps = [mock._name for mock in self._chain(*args)]
        url = "/".join(reversed(path_comps))

        if self._append_slash:
            url = url + "/"

        return url

    def _request(self, method, kwargs=None):
        if not kwargs:
            kwargs = {}

        if self._url() != self._parent:
            self._endpoint._name = self._name
            self._endpoint._parent = self._parent

        request = getattr(self._endpoint, method)
        response = request(**kwargs)

        if not response.status_code == 200:
            response.raise_for_status()

        return response

    def get(self):
        return self._request("GET")

    def post(self, data=None):
        return self._request("POST", {"json": data})

    def delete(self):
        return self._request("DELETE")
