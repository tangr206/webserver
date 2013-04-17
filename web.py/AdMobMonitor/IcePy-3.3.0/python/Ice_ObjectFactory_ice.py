# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `ObjectFactory.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('ObjectFactory'):
    _M_Ice.ObjectFactory = Ice.createTempClass()
    class ObjectFactory(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.ObjectFactory:
                raise RuntimeError('Ice.ObjectFactory is an abstract class')

        #
        # Operation signatures.
        #
        # def create(self, type):
        # def destroy(self):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_ObjectFactory)

        __repr__ = __str__

    _M_Ice._t_ObjectFactory = IcePy.defineClass('::Ice::ObjectFactory', ObjectFactory, (), True, None, (), ())
    ObjectFactory.ice_type = _M_Ice._t_ObjectFactory

    _M_Ice.ObjectFactory = ObjectFactory
    del ObjectFactory

# End of module Ice
