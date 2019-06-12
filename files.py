# -*- coding: utf8 -*-


def read(path):
    out = []
    with open(path) as f:
        out = f.readlines()
    return out
