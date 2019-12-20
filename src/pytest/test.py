# -*- coding: utf-8 -*-
#!/usr/bin/env python

import importlib
import sys
from ctypes import *

ctest=CDLL('./test.so')
ctest.test()


# test=importlib.import_module("test")

# test.test()
