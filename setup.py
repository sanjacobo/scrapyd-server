import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="scrapyd",
    version=read('VERSION'),
    author="Santiago Guichon",
    author_email="santiago.guichon@gmail.com",
    description="Scrapyd server",
    # packages=['an_example_pypi_project', 'tests'],
    install_requires=[
        'scrapy',
        'scrapyd',
        'scrapyd-client',
    ]
)
