# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Session.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Glacier2_Session_ice
import IceGrid_Exception_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')

# Start of module IceGrid
__name__ = 'IceGrid'

if not _M_IceGrid.__dict__.has_key('Session'):
    _M_IceGrid.Session = Ice.createTempClass()
    class Session(_M_Glacier2.Session):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.Session:
                raise RuntimeError('IceGrid.Session is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::Session', '::Ice::Object', '::IceGrid::Session')

        def ice_id(self, current=None):
            return '::IceGrid::Session'

        def ice_staticId():
            return '::IceGrid::Session'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def keepAlive(self, current=None):
        # def allocateObjectById_async(self, _cb, id, current=None):
        # def allocateObjectByType_async(self, _cb, type, current=None):
        # def releaseObject(self, id, current=None):
        # def setAllocationTimeout(self, timeout, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_Session)

        __repr__ = __str__

    _M_IceGrid.SessionPrx = Ice.createTempClass()
    class SessionPrx(_M_Glacier2.SessionPrx):

        def keepAlive(self, _ctx=None):
            return _M_IceGrid.Session._op_keepAlive.invoke(self, ((), _ctx))

        def allocateObjectById(self, id, _ctx=None):
            return _M_IceGrid.Session._op_allocateObjectById.invoke(self, ((id, ), _ctx))

        def allocateObjectById_async(self, _cb, id, _ctx=None):
            return _M_IceGrid.Session._op_allocateObjectById.invokeAsync(self, (_cb, (id, ), _ctx))

        def allocateObjectByType(self, type, _ctx=None):
            return _M_IceGrid.Session._op_allocateObjectByType.invoke(self, ((type, ), _ctx))

        def allocateObjectByType_async(self, _cb, type, _ctx=None):
            return _M_IceGrid.Session._op_allocateObjectByType.invokeAsync(self, (_cb, (type, ), _ctx))

        def releaseObject(self, id, _ctx=None):
            return _M_IceGrid.Session._op_releaseObject.invoke(self, ((id, ), _ctx))

        def setAllocationTimeout(self, timeout, _ctx=None):
            return _M_IceGrid.Session._op_setAllocationTimeout.invoke(self, ((timeout, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.SessionPrx.ice_checkedCast(proxy, '::IceGrid::Session', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.SessionPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_SessionPrx = IcePy.defineProxy('::IceGrid::Session', SessionPrx)

    _M_IceGrid._t_Session = IcePy.defineClass('::IceGrid::Session', Session, (), True, None, (_M_Glacier2._t_Session,), ())
    Session.ice_type = _M_IceGrid._t_Session

    Session._op_keepAlive = IcePy.Operation('keepAlive', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), None, ())
    Session._op_allocateObjectById = IcePy.Operation('allocateObjectById', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), _M_Ice._t_Identity),), (), IcePy._t_ObjectPrx, (_M_IceGrid._t_ObjectNotRegisteredException, _M_IceGrid._t_AllocationException))
    Session._op_allocateObjectByType = IcePy.Operation('allocateObjectByType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), IcePy._t_string),), (), IcePy._t_ObjectPrx, (_M_IceGrid._t_AllocationException,))
    Session._op_releaseObject = IcePy.Operation('releaseObject', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_Ice._t_Identity),), (), None, (_M_IceGrid._t_ObjectNotRegisteredException, _M_IceGrid._t_AllocationException))
    Session._op_setAllocationTimeout = IcePy.Operation('setAllocationTimeout', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_int),), (), None, ())

    _M_IceGrid.Session = Session
    del Session

    _M_IceGrid.SessionPrx = SessionPrx
    del SessionPrx

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::Session"] = "cf4206d0a8aff6c1b0f2c437f34c5d"
