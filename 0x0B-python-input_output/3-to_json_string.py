#!/usr/bin/python3
"""Function that returns the JSON representation of an object (st
ring).
"""
import json


def to_json_string(my_obj):
    """Return JSON format of my_obj
    """

    return json.dumps(my_obj)
