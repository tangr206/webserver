# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Identity.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Identity'):
    _M_Ice.Identity = Ice.createTempClass()
    class Identity(object):
        def __init__(self, name='', category=''):
            self.name = name
            self.category = category

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.name)
            _h = 5 * _h + __builtin__.hash(self.category)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            if self.category < other.category:
                return -1
            elif self.category > other.category:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Identity)

        __repr__ = __str__

    _M_Ice._t_Identity = IcePy.defineStruct('::Ice::Identity', Identity, (), (
        ('name', (), IcePy._t_string),
        ('category', (), IcePy._t_string)
    ))

    _M_Ice.Identity = Identity
    del Identity

if not _M_Ice.__dict__.has_key('_t_ObjectDict'):
    _M_Ice._t_ObjectDict = IcePy.defineDictionary('::Ice::ObjectDict', (), _M_Ice._t_Identity, IcePy._t_Object)

if not _M_Ice.__dict__.has_key('_t_IdentitySeq'):
    _M_Ice._t_IdentitySeq = IcePy.defineSequence('::Ice::IdentitySeq', (), _M_Ice._t_Identity)

# End of module Ice
