#!/usr/bin/env python3

from distutils.core import setup
import py2exe

setup(windows=['victim.py'], options={'py2exe':{'optimize':2}})
