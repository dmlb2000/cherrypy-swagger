#!/usr/bin/python
"""Test the string generator class."""

import os
import cherrypy
from cherrypy.test import helper
from example.string_generator import StringGeneratorWebService, STRING_FILE


class TestStringGenerator(helper.CPWebCase):
    """The test framework for string generator service."""

    @classmethod
    def setUpClass(cls):
        """Setup the class by changing the PORT."""
        cls.PORT = 1234
        cls.HOST = '127.0.0.1'

    def setUp(self):
        """Setup each test by starting the CherryPy server."""
        if not os.access(STRING_FILE, os.F_OK):
            os.ftruncate(os.open(STRING_FILE, os.O_WRONLY | os.O_CREAT), 0)
        swagger_headers = [
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', 'GET, POST, DELETE, PUT'),
            ('Access-Control-Allow-Headers', 'Content-Type, api_key, Authorization')
        ]
        conf = {
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.response_headers.on': True,
                'tools.response_headers.headers': swagger_headers,
            },
            'global': {
                'server.socket_host': '0.0.0.0',
                'server.socket_port': 1234
            }
        }
        cherrypy.config.update('testing.conf')
        cherrypy.tree.mount(StringGeneratorWebService(), '/', conf)
        cherrypy.engine.start()

    def tearDown(self):
        """Tear down the CherryPy server after each test."""
        cherrypy.engine.exit()
        if os.access(STRING_FILE, os.F_OK):
            os.unlink(STRING_FILE)

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
