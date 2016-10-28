#!/usr/bin/python
"""This is a sample module docstring for the hello module."""


class Hello(object):
    """This is a sample docstring for the Hello Class."""

    def __init__(self):
        """Hello class constructor."""
        self._hello = 'Hello!'

    def hello(self):
        """Example hello method."""
        return self._hello
