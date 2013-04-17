# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Endpoint.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('EndpointSelectionType'):
    _M_Ice.EndpointSelectionType = Ice.createTempClass()
    class EndpointSelectionType(object):

        def __init__(self, val):
            assert(val >= 0 and val < 2)
            self.value = val

        def __str__(self):
            if self.value == 0:
                return 'Random'
            elif self.value == 1:
                return 'Ordered'
            return None

        __repr__ = __str__

        def __hash__(self):
            return self.value

        def __cmp__(self, other):
            return cmp(self.value, other.value)

    EndpointSelectionType.Random = EndpointSelectionType(0)
    EndpointSelectionType.Ordered = EndpointSelectionType(1)

    _M_Ice._t_EndpointSelectionType = IcePy.defineEnum('::Ice::EndpointSelectionType', EndpointSelectionType, (), (EndpointSelectionType.Random, EndpointSelectionType.Ordered))

    _M_Ice.EndpointSelectionType = EndpointSelectionType
    del EndpointSelectionType

if not _M_Ice.__dict__.has_key('Endpoint'):
    _M_Ice.Endpoint = Ice.createTempClass()
    class Endpoint(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Endpoint:
                raise RuntimeError('Ice.Endpoint is an abstract class')

        #
        # Operation signatures.
        #
        # def toString(self):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Endpoint)

        __repr__ = __str__

    _M_Ice._t_Endpoint = IcePy.defineClass('::Ice::Endpoint', Endpoint, (), True, None, (), ())
    Endpoint.ice_type = _M_Ice._t_Endpoint

    _M_Ice.Endpoint = Endpoint
    del Endpoint

if not _M_Ice.__dict__.has_key('_t_EndpointSeq'):
    _M_Ice._t_EndpointSeq = IcePy.defineSequence('::Ice::EndpointSeq', (), _M_Ice._t_Endpoint)

# End of module Ice
