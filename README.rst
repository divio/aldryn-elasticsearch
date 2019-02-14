=================
Aldryn Elasticsearch App
=================

Small addon which helps configure the Elastic Search connection
using environment variables. Meant to be used as an Aldryn Addon together with aldryn-django.

Installation
============

**Aldryn Platform Users** ask support to provision ElasticSeearch for you.

Contributing
============

This is a an open-source project. We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

We're grateful to all contributors who have helped create and maintain this package.
Contributors are listed at the `contributors <https://github.com/divio/aldryn-elasticsearch/graphs/contributors>`_
section.

Local docker setup
==================

For local development add a ElasticSearch service to ``docker-compose.yml``::

    es:
        image: elasticsearch:2.4

and add a link to it from the web service::

    web:
        links:
          - "es:es"

Then add the environment variable to configure the connection (on the default
aldryn setup: add to ``.env-local``)::

    DEFAULT_ELASTICSEARCH_URL=es+http://es:9200/local-*


Usage
=====

To get a connection to the default index simply run::

    from aldryn_elasticsearch.connection import es_conn, es_index
    es_conn.search(index=es_index)


To get a connection to a specific index run::

    from aldryn_elasticsearch.connection import get_connection
    es_conn, es_index = get_connection(suffix='my-index-name')
    es_conn.search(index=es_index)

If you want to use a different host URL than the default
(read from the environment ``DEFAULT_ELASTICSEARCH_URL``) you can pass that like this::

    from aldryn_elasticsearch.connection import get_connection
    es_conn, es_index = get_connection(
        url='es+http://elasticsearch:9200/local-*',
        suffix='my-index-name',
    )
    es_conn.search(index=es_index)


Other Stuff
===========

``DEFAULT_ELASTICSEARCH_URL`` environment variable

Set an environment variable::

    DEFAULT_ELASTICSEARCH_URL=es+http://hostname:9200/my-index-name

There is also native support for AWS ElasticSearch style connections::

    DEFAULT_ELASTICSEARCH_URL=es+https+aws://AWS_ACCESS_KEY:AWS_SECRET_KEY@cluster-name.us-east-1.amazonaws.com/my-index-name

There is also support to define the index name with a wildcard ``*`` that can
be used for setting up multiple indeces.

Debugging
=========

Set the ``ALDRYN_ELASTICSEARCH_DEBUG`` environment variable to True to get detailed
logs from Elasticsearch.
