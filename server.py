#!/usr/bin/python
"""Main server script."""
import cherrypy
from string_generator import StringGeneratorWebService


def main():
    """The main method for starting the server."""
    cherrypy.quickstart(StringGeneratorWebService(), '/', 'server.conf')

if __name__ == '__main__':
    main()
