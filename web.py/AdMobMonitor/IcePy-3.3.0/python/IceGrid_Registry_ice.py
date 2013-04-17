# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Registry.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import IceGrid_Exception_ice
import IceGrid_Session_ice
import IceGrid_Admin_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Start of module IceGrid
__name__ = 'IceGrid'

if not _M_IceGrid.__dict__.has_key('Registry'):
    _M_IceGrid.Registry = Ice.createTempClass()
    class Registry(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.Registry:
                raise RuntimeError('IceGrid.Registry is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::Registry')

        def ice_id(self, current=None):
            return '::IceGrid::Registry'

        def ice_staticId():
            return '::IceGrid::Registry'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def createSession(self, userId, password, current=None):
        # def createAdminSession(self, userId, password, current=None):
        # def createSessionFromSecureConnection(self, current=None):
        # def createAdminSessionFromSecureConnection(self, current=None):
        # def getSessionTimeout(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_Registry)

        __repr__ = __str__

    _M_IceGrid.RegistryPrx = Ice.createTempClass()
    class RegistryPrx(Ice.ObjectPrx):

        def createSession(self, userId, password, _ctx=None):
            return _M_IceGrid.Registry._op_createSession.invoke(self, ((userId, password), _ctx))

        def createAdminSession(self, userId, password, _ctx=None):
            return _M_IceGrid.Registry._op_createAdminSession.invoke(self, ((userId, password), _ctx))

        def createSessionFromSecureConnection(self, _ctx=None):
            return _M_IceGrid.Registry._op_createSessionFromSecureConnection.invoke(self, ((), _ctx))

        def createAdminSessionFromSecureConnection(self, _ctx=None):
            return _M_IceGrid.Registry._op_createAdminSessionFromSecureConnection.invoke(self, ((), _ctx))

        def getSessionTimeout(self, _ctx=None):
            return _M_IceGrid.Registry._op_getSessionTimeout.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.RegistryPrx.ice_checkedCast(proxy, '::IceGrid::Registry', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.RegistryPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_RegistryPrx = IcePy.defineProxy('::IceGrid::Registry', RegistryPrx)

    _M_IceGrid._t_Registry = IcePy.defineClass('::IceGrid::Registry', Registry, (), True, None, (), ())
    Registry.ice_type = _M_IceGrid._t_Registry

    Registry._op_createSession = IcePy.Operation('createSession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), _M_IceGrid._t_SessionPrx, (_M_IceGrid._t_PermissionDeniedException,))
    Registry._op_createAdminSession = IcePy.Operation('createAdminSession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), _M_IceGrid._t_AdminSessionPrx, (_M_IceGrid._t_PermissionDeniedException,))
    Registry._op_createSessionFromSecureConnection = IcePy.Operation('createSessionFromSecureConnection', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_IceGrid._t_SessionPrx, (_M_IceGrid._t_PermissionDeniedException,))
    Registry._op_createAdminSessionFromSecureConnection = IcePy.Operation('createAdminSessionFromSecureConnection', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_IceGrid._t_AdminSessionPrx, (_M_IceGrid._t_PermissionDeniedException,))
    Registry._op_getSessionTimeout = IcePy.Operation('getSessionTimeout', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_int, ())

    _M_IceGrid.Registry = Registry
    del Registry

    _M_IceGrid.RegistryPrx = RegistryPrx
    del RegistryPrx

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::Registry"] = "c78158c7cf2552d132645cd358d74c"
