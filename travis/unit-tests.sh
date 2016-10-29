#!/bin/bash -xe

coverage run --include='example/*,hello/*' test.py -v
codeclimate-test-reporter
