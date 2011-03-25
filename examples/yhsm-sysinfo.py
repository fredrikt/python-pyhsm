#!/usr/bin/env python
#
# Copyright (c) 2011, Yubico AB
# All rights reserved.
#
# Utility to show system information of a YubiHSM.
#

import sys
sys.path.append('Lib');
import serveronstick

device = "/dev/ttyACM0"

# simplified arguments parsing
d_argv = dict.fromkeys(sys.argv)
debug = d_argv.has_key('-v')

if d_argv.has_key('-h'):
    sys.stderr.write("Syntax: %s [-v]\n" % (sys.argv[0]))
    sys.exit(0)

res = 0
try:
    s = serveronstick.base.SoS(device=device, debug=debug)

    print "Version: %s" % s.info()
except serveronstick.exception.SoS_Error, e:
    print "ERROR: %s" % e
    res = 1

sys.exit(res)
