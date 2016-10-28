#!/bin/bash -xe

coverage run test.py -v
codeclimate-test-reporter
