# -*- coding: utf-8 -*-
"""
Functions to work with JSON
"""

from __future__ import absolute_import, unicode_literals

# Import Python libs
import json  # future lint: blacklisted-module
import logging


import hubblestack.utils.stringutils


log = logging.getLogger(__name__)


# One to one mappings
JSONEncoder = json.JSONEncoder


def loads(s, **kwargs):
    """
    .. versionadded:: 2018.3.0

    Wraps json.loads and prevents a traceback in the event that a bytestring is
    passed to the function. (Python < 3.6 cannot load bytestrings)

    You can pass an alternate json module (loaded via import_json() above)
    using the _json_module argument)
    """
    json_module = kwargs.pop("_json_module", json)
    try:
        return json_module.loads(s, **kwargs)
    except TypeError as exc:
        # json.loads cannot load bytestrings in Python < 3.6
            return json_module.loads(hubblestack.utils.stringutils.to_unicode(s), **kwargs)


def dumps(obj, **kwargs):
    """
    .. versionadded:: 2018.3.0
    Wraps json.dumps, and assumes that ensure_ascii is False (unless explicitly
    passed as True) for unicode compatibility. Note that setting it to True
    will mess up any unicode characters, as they will be dumped as the string
    literal version of the unicode code point.
    On Python 2, encodes the result to a str since json.dumps does not want
    unicode types.
    You can pass an alternate json module (loaded via import_json() above)
    using the _json_module argument)
    """
    json_module = kwargs.pop("_json_module", json)
    if "ensure_ascii" not in kwargs:
        kwargs["ensure_ascii"] = False
    return json_module.dumps(obj, **kwargs)  # future lint: blacklisted-function
