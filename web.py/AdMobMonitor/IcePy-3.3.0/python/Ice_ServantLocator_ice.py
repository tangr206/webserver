# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `ServantLocator.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_ObjectAdapterF_ice
import Ice_Current_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('ServantLocator'):
    _M_Ice.ServantLocator = Ice.createTempClass()
    class ServantLocator(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.ServantLocator:
                raise RuntimeError('Ice.ServantLocator is an abstract class')

        #
        # Operation signatures.
        #
        # def locate(self, curr):
        # def finished(self, curr, servant, cookie):
        # def deactivate(self, category):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_ServantLocator)

        __repr__ = __str__

    _M_Ice._t_ServantLocator = IcePy.defineClass('::Ice::ServantLocator', ServantLocator, (), True, None, (), ())
    ServantLocator.ice_type = _M_Ice._t_ServantLocator

    _M_Ice.ServantLocator = ServantLocator
    del ServantLocator

# End of module Ice
