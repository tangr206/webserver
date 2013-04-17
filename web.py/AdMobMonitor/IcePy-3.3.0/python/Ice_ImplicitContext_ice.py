# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `ImplicitContext.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_LocalException_ice
import Ice_Current_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('ImplicitContext'):
    _M_Ice.ImplicitContext = Ice.createTempClass()
    class ImplicitContext(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.ImplicitContext:
                raise RuntimeError('Ice.ImplicitContext is an abstract class')

        #
        # Operation signatures.
        #
        # def getContext(self):
        # def setContext(self, newContext):
        # def containsKey(self, key):
        # def get(self, key):
        # def put(self, key, value):
        # def remove(self, key):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_ImplicitContext)

        __repr__ = __str__

    _M_Ice._t_ImplicitContext = IcePy.defineClass('::Ice::ImplicitContext', ImplicitContext, (), True, None, (), ())
    ImplicitContext.ice_type = _M_Ice._t_ImplicitContext

    _M_Ice.ImplicitContext = ImplicitContext
    del ImplicitContext

# End of module Ice
