# coding:utf-8

import os

from handers.hander import *

urls = [
    (r"/intake/",IntakeHander),
    (r"/api/v1/series",SeriesHander)
]
