#!/usr/bin/python
"""
CherryPy String Generator Service.

This is the example random string generator service, slightly
modified for swagger to not use session support.
"""
import random
import string
import cherrypy

STRING_TO_KEEP = ""

@cherrypy.expose
class StringGeneratorWebService(object):
    """String Generator Class."""

    @staticmethod
    @cherrypy.tools.json_out()
    # pylint: disable=invalid-name
    def GET():
        """CherryPy Get Method."""
        return {'mystring': STRING_TO_KEEP}

    @staticmethod
    @cherrypy.tools.json_out()
    # pylint: disable=invalid-name
    def POST(length=8):
        """CherryPy Post Method."""
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        STRING_TO_KEEP = some_string
        return {'mystring': some_string}

    @staticmethod
    @cherrypy.tools.json_out()
    # pylint: disable=invalid-name
    def PUT(another_string):
        """CherryPy Put Method."""
        global STRING_TO_KEEP
        STRING_TO_KEEP = another_string
        return {'mystring': another_string}

    @staticmethod
    @cherrypy.tools.json_out()
    # pylint: disable=invalid-name
    def DELETE():
        """CherryPy Delete Method."""
        global STRING_TO_KEEP
        STRING_TO_KEEP = ""
        cherrypy.response.status = 204

    @staticmethod
    @cherrypy.tools.json_out()
    # pylint: disable=unused-argument
    # pylint: disable=invalid-name
    def OPTIONS(another_string=None):
        """CherryPy Options Method."""
        cherrypy.response.status = 204
