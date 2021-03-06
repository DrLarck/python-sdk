# -*- coding: utf-8 -*-

"""
Top.gg Python API Wrapper
~~~~~~~~~~~~~~~~~~~~~~
A basic wrapper for the top.gg API.
:copyright: (c) 2020 Assanali Mukhanov & top.gg
:license: MIT, see LICENSE for more details.
"""

__title__ = 'topggpy'
__author__ = 'Assanali Mukhanov'
__license__ = 'MIT'
__version__ = '1.0.0'

from collections import namedtuple

from .client import DBLClient
from .errors import *
from .http import HTTPClient
from .webhook import WebhookManager

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=4, micro=0, releaselevel='final', serial=0)
