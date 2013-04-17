# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Stats.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Stats'):
    _M_Ice.Stats = Ice.createTempClass()
    class Stats(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Stats:
                raise RuntimeError('Ice.Stats is an abstract class')

        #
        # Operation signatures.
        #
        # def bytesSent(self, protocol, num):
        # def bytesReceived(self, protocol, num):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Stats)

        __repr__ = __str__

    _M_Ice._t_Stats = IcePy.defineClass('::Ice::Stats', Stats, (), True, None, (), ())
    Stats.ice_type = _M_Ice._t_Stats

    _M_Ice.Stats = Stats
    del Stats

# End of module Ice
