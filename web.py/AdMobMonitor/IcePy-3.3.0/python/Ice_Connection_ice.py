# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Connection.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_ObjectAdapterF_ice
import Ice_Identity_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Connection'):
    _M_Ice.Connection = Ice.createTempClass()
    class Connection(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Connection:
                raise RuntimeError('Ice.Connection is an abstract class')

        #
        # Operation signatures.
        #
        # def close(self, force):
        # def createProxy(self, id):
        # def setAdapter(self, adapter):
        # def getAdapter(self):
        # def flushBatchRequests(self):
        # def type(self):
        # def timeout(self):
        # def toString(self):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Connection)

        __repr__ = __str__

    _M_Ice._t_Connection = IcePy.defineClass('::Ice::Connection', Connection, (), True, None, (), ())
    Connection.ice_type = _M_Ice._t_Connection

    _M_Ice.Connection = Connection
    del Connection

# End of module Ice
