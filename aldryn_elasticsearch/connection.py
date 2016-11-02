# -*- coding: utf-8 -*-
from django.conf import settings

from elasticsearch_dsl.connections import connections

from . import elasticsearch_url


def get_connection(url=None, suffix='default'):
    if url is None:
        url = settings.DEFAULT_ELASTICSEARCH_URL
    conn_info = elasticsearch_url.parse(url, suffix)
    return connections.create_connection(**conn_info), conn_info['INDEX']

es_conn, es_index = get_connection()
