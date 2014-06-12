#!/usr/bin/env python

import os

TEST_VIRTUALENV = os.path.join('tests', 'virtualenvs', 'equimapper')

if not os.path.isdir(TEST_VIRTUALENV):
    print('Creating test virtualenv: {0}'.format(TEST_VIRTUALENV))
    os.system('virtualenv {0}'.format(TEST_VIRTUALENV))
    os.system('{0}/bin/pip install -r {0}/../equimapper_requirements.txt'
              .format(TEST_VIRTUALENV))
