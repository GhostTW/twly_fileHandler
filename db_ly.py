#! /usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
from psycopg2.extras import Json

def con():
    psycopg2.extensions.register_adapter(dict, Json)
    conn = psycopg2.connect(dbname='ly_dev', host='localhost', user='postgres' , password='postgres')
    return conn



