#!/usr/bin/python3
"""bu modul atribut ve metidlarin axtarmaq ucun lookup funksiyasini temin edir"""


def lookup(obj):
    """obyektin atribut ve metodlarini qaytarir"""
    return dir(obj)
