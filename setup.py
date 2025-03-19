from distutils.core import setup
import py2exe
import sys
import os

# Exclude the mods directory
excludes = ['mods/']

setup(
    console=['fetch.py'],
    options={
        'py2exe': {
            'excludes': excludes
        }
    }
)
