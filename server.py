#!/usr/bin/python
"""Main server script."""
import os
import cherrypy
from example.string_generator import StringGeneratorWebService


def main():
    """The main method for starting the server."""
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
        '/swagger.json': {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': os.path.join(os.getcwd(), 'swagger.json'),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': swagger_headers,
        },
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 1234
        }
    }
    cherrypy.config.update('server.conf')
    cherrypy.quickstart(StringGeneratorWebService(), '/', conf)

if __name__ == '__main__':
    main()
