# -*- coding: utf-8 -*-

"""Main module."""

import copy

from hammock import Hammock, bind_method


class METRC(Hammock):
    """Class for wrapping requests to the METRC Web API"""

    def __init__(self, base_path, vendor_key, user_key, license_number, api_version="v1", **kwargs):
        kwargs.update({
            "auth": (vendor_key, user_key),
            "params": {"licenseNumber": license_number},
        })

        super().__init__(base_path, **kwargs)

        self.api_version = api_version

    def _spawn(self, name):
        child = copy.copy(self)

        if not child._parent:
            child._name = name + "/" + self.api_version
        else:
            child._name = name

        child._parent = self
        return child

for method in ["get", "post", "delete"]:
    setattr(METRC, method, bind_method(method))
