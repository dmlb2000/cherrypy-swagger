#!/usr/bin/python
"""Test the string generator class."""

import os
import cherrypy
from cherrypy.test import helper
from string_generator import StringGeneratorWebService, STRING_TO_KEEP


class TestStringGenerator(helper.CPWebCase):
    """The test framework for string generator service."""
    PORT = 1234
    HOST = '127.0.0.1'

    @staticmethod
    def setup_server():
        """Setup each test by starting the CherryPy server."""
        STRING_TO_KEEP = ""
        cherrypy.config.update('server.conf')
        cherrypy.tree.mount(StringGeneratorWebService(), '/', 'server.conf')

    def test_get_method(self):
        """Test the GET method."""
        self.getPage('/')
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'application/json')
        self.assertBody('{"mystring": ""}')

    def test_get_with_real_data(self):
        """Test the GET method with data in the system."""
        self.getPage('/blah', method='PUT')
        self.getPage('/')
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'application/json')
        self.assertBody('{"mystring": "blah"}')

    def test_put_method(self):
        """Test the PUT method."""
        self.getPage('/blah', method='PUT')
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'application/json')
        self.assertBody('{"mystring": "blah"}')

    def test_post_method(self):
        """Test the POST method."""
        self.getPage('/', method='POST')
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'application/json')

    def test_delete_method(self):
        """Test the DELETE method."""
        self.getPage('/blah', method='PUT')
        self.getPage('/', method='DELETE')
        self.assertStatus('204 No Content')
        self.assertHeader('Content-Type', 'application/json')

    def test_options_method(self):
        """Test the Options method."""
        self.getPage('/', method='OPTIONS')
        self.assertStatus('204 No Content')
        self.assertHeader('Content-Type', 'application/json')
