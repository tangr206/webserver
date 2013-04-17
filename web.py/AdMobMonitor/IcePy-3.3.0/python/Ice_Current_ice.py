# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Current.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_ObjectAdapterF_ice
import Ice_ConnectionF_ice
import Ice_Identity_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('_t_Context'):
    _M_Ice._t_Context = IcePy.defineDictionary('::Ice::Context', (), IcePy._t_string, IcePy._t_string)

if not _M_Ice.__dict__.has_key('OperationMode'):
    _M_Ice.OperationMode = Ice.createTempClass()
    class OperationMode(object):

        def __init__(self, val):
            assert(val >= 0 and val < 3)
            self.value = val

        def __str__(self):
            if self.value == 0:
                return 'Normal'
            elif self.value == 1:
                return 'Nonmutating'
            elif self.value == 2:
                return 'Idempotent'
            return None

        __repr__ = __str__

        def __hash__(self):
            return self.value

        def __cmp__(self, other):
            return cmp(self.value, other.value)

    OperationMode.Normal = OperationMode(0)
    OperationMode.Nonmutating = OperationMode(1)
    OperationMode.Idempotent = OperationMode(2)

    _M_Ice._t_OperationMode = IcePy.defineEnum('::Ice::OperationMode', OperationMode, (), (OperationMode.Normal, OperationMode.Nonmutating, OperationMode.Idempotent))

    _M_Ice.OperationMode = OperationMode
    del OperationMode

if not _M_Ice.__dict__.has_key('Current'):
    _M_Ice.Current = Ice.createTempClass()
    class Current(object):
        def __init__(self, adapter=None, con=None, id=Ice._struct_marker, facet='', operation='', mode=_M_Ice.OperationMode.Normal, ctx=None, requestId=0):
            self.adapter = adapter
            self.con = con
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id
            self.facet = facet
            self.operation = operation
            self.mode = mode
            self.ctx = ctx
            self.requestId = requestId

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.adapter)
            _h = 5 * _h + __builtin__.hash(self.con)
            _h = 5 * _h + __builtin__.hash(self.id)
            _h = 5 * _h + __builtin__.hash(self.facet)
            _h = 5 * _h + __builtin__.hash(self.operation)
            _h = 5 * _h + __builtin__.hash(self.mode)
            if self.ctx:
                for _i0 in self.ctx:
                    _h = 5 * _h + __builtin__.hash(_i0)
                    _h = 5 * _h + __builtin__.hash(self.ctx[_i0])
            _h = 5 * _h + __builtin__.hash(self.requestId)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.adapter < other.adapter:
                return -1
            elif self.adapter > other.adapter:
                return 1
            if self.con < other.con:
                return -1
            elif self.con > other.con:
                return 1
            if self.id < other.id:
                return -1
            elif self.id > other.id:
                return 1
            if self.facet < other.facet:
                return -1
            elif self.facet > other.facet:
                return 1
            if self.operation < other.operation:
                return -1
            elif self.operation > other.operation:
                return 1
            if self.mode < other.mode:
                return -1
            elif self.mode > other.mode:
                return 1
            if self.ctx < other.ctx:
                return -1
            elif self.ctx > other.ctx:
                return 1
            if self.requestId < other.requestId:
                return -1
            elif self.requestId > other.requestId:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Current)

        __repr__ = __str__

    _M_Ice._t_Current = IcePy.defineStruct('::Ice::Current', Current, (), (
        ('adapter', (), _M_Ice._t_ObjectAdapter),
        ('con', (), _M_Ice._t_Connection),
        ('id', (), _M_Ice._t_Identity),
        ('facet', (), IcePy._t_string),
        ('operation', (), IcePy._t_string),
        ('mode', (), _M_Ice._t_OperationMode),
        ('ctx', (), _M_Ice._t_Context),
        ('requestId', (), IcePy._t_int)
    ))

    _M_Ice.Current = Current
    del Current

# End of module Ice
