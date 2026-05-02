#!/usr/bin/python3
"""basic serialization"""


def serialization_and_save_to_file(data, filename):
    """json formatina cevirir ve fayla yzir"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f):

def load_and_deserialize(filename):
    """json faylini oxuyur"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
