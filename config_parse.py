#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016 ARCCN (www.arccn.ru)

import configparser
config = configparser.ConfigParser()

config.read('config.cfg')
# print config.sections()
def conf_to_dict(section):
    try:
        # config.read('config.cfg')
        dictory = {}
        for i in config.items(section):
                if len(i) == 2:
                    dictory[i[0]] = i[1]
        return dictory
    except configparser.MissingSectionHeaderError:
        # LOG.error("Error configuration file")
        return True
    except configparser.NoSectionError:
        # LOG.error("Error section %s configuration file" %section)
        return False

def list_section():
    return config.sections()
DEFAULT = config.defaults()
# print (DEFAULT.get(''))