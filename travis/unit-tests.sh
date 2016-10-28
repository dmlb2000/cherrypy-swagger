#!/bin/bash -xe

coverage run -m unittest discover -v
codeclimate-test-reporter
