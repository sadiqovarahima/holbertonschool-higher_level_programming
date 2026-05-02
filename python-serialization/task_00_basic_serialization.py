#!/usr/bin/python3
"""basic serialization"""
import json


def serialization_and_save_to_file(data, filename):
    """json formatina cevirir ve fayla yzir"""
    with open(filename, "w") as f:
        json.dump(data, f):

def load_and_deserialize(filename):
    """json faylini oxuyur"""
    with open(filename, "r") as f:
        return json.load(f)
