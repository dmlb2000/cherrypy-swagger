#!/bin/bash -xe

coverage run -m unittest discover
codeclimate-test-reporter
