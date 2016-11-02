# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name="aldryn-elasticsearch",
    version=__import__('aldryn_elasticsearch').__version__,
    description='Easily configure Elasticsearch on Aldryn.',
    long_description=open('README.rst').read(),
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-elasticsearch',
    packages=find_packages(),
    install_requires=(
        'aldryn-django',
        'elasticsearch',
        'elasticsearch-dsl',
        'requests-aws4auth',
        'furl',
        'django-getenv',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
    ]
)
