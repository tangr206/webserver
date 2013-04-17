# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Logger.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Logger'):
    _M_Ice.Logger = Ice.createTempClass()
    class Logger(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Logger:
                raise RuntimeError('Ice.Logger is an abstract class')

        #
        # Operation signatures.
        #
        # def _print(self, message):
        # def trace(self, category, message):
        # def warning(self, message):
        # def error(self, message):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Logger)

        __repr__ = __str__

    _M_Ice._t_Logger = IcePy.defineClass('::Ice::Logger', Logger, (), True, None, (), ())
    Logger.ice_type = _M_Ice._t_Logger

    _M_Ice.Logger = Logger
    del Logger

# End of module Ice
