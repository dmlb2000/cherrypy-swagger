[![Build Status](https://travis-ci.org/dmlb2000/cherrypy-swagger.svg?branch=master)](https://travis-ci.org/dmlb2000/cherrypy-swagger)
[![Code Climate](https://codeclimate.com/github/dmlb2000/cherrypy-swagger/badges/gpa.svg)](https://codeclimate.com/github/dmlb2000/cherrypy-swagger)
[![Test Coverage](https://codeclimate.com/github/dmlb2000/cherrypy-swagger/badges/coverage.svg)](https://codeclimate.com/github/dmlb2000/cherrypy-swagger/coverage)
[![Issue Count](https://codeclimate.com/github/dmlb2000/cherrypy-swagger/badges/issue_count.svg)](https://codeclimate.com/github/dmlb2000/cherrypy-swagger)

# CherryPy-Swagger
Swagger Extensions for CherryPy

## Examples

### Random String Generator

`string_generator.py`

This is a modified version of the CherryPy
[Give us a REST](http://docs.cherrypy.org/en/latest/tutorials.html#tutorial-7-give-us-a-rest)
example that uses static files instead of sessions. Swagger 2.0 doesn't
support sessions currently so using a session in the example won't work.

To run the application:

```
python server.py
```

## Run Swagger 2.0 UI

Start the Swagger 2.0 UI service by following the instructions with
the [code](https://github.com/swagger-api/swagger-ui).

In the web page you can go to the `http://localhost:1234/swagger.json`
to play around with the UI.
