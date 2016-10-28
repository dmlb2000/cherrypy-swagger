#!/bin/bash -xe

coverage run -m unittest
codeclimate-test-reporter
