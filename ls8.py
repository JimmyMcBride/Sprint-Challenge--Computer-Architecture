#!/bin/python

"""Main."""

import sys
from cpu import *

cpu = CPU()
# sys.argv[1]
cpu.load(sys.argv[1])
cpu.run()
