#!/usr/bin/python3
def magic_string(holder={'counter': 0}):
    holder['counter'] += 1
    return (', '.join(['BestSchool'] * (holder['counter'])))
