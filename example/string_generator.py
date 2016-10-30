#!/usr/bin/python
"""
CherryPy String Generator Service.

This is the example random string generator service, slightly
modified for swagger to not use session support.
"""
import random
import string
import os
import cherrypy

STRING_FILE = 'string.txt'


@cherrypy.expose
class StringGeneratorWebService(object):
    """String Generator Class."""

    @cherrypy.tools.json_out()
    # pylint: disable=no-self-use
    # pylint: disable=invalid-name
    def GET(self):
        """CherryPy Get Method."""
        strfd = open(STRING_FILE)
        mystring = strfd.read()
        strfd.close()
        return {'mystring': mystring}

    @cherrypy.tools.json_out()
    # pylint: disable=no-self-use
    # pylint: disable=invalid-name
    def POST(self, length=8):
        """CherryPy Post Method."""
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        strfd = open(STRING_FILE, 'w')
        strfd.write(some_string)
        strfd.close()
        return {'mystring': some_string}

    @cherrypy.tools.json_out()
    # pylint: disable=no-self-use
    # pylint: disable=invalid-name
    def PUT(self, another_string):
        """CherryPy Put Method."""
        strfd = open(STRING_FILE, 'w')
        strfd.write(another_string)
        strfd.close()
        return {'mystring': another_string}

    @cherrypy.tools.json_out()
    # pylint: disable=no-self-use
    # pylint: disable=invalid-name
    def DELETE(self):
        """CherryPy Delete Method."""
        strfd = os.open(STRING_FILE, os.O_WRONLY | os.O_CREAT)
        os.ftruncate(strfd, 0)
        os.close(strfd)
        cherrypy.response.status = 204
        return ''

    @cherrypy.tools.json_out()
    # pylint: disable=no-self-use
    # pylint: disable=unused-argument
    # pylint: disable=invalid-name
    def OPTIONS(self, another_string=None):
        """CherryPy Options Method."""
        cherrypy.response.status = 204
        return ''
