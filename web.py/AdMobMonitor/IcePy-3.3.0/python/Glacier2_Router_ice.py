# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Router.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_Router_ice
import Glacier2_Session_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Start of module Glacier2
__name__ = 'Glacier2'

if not _M_Glacier2.__dict__.has_key('PermissionDeniedException'):
    _M_Glacier2.PermissionDeniedException = Ice.createTempClass()
    class PermissionDeniedException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'Glacier2::PermissionDeniedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Glacier2._t_PermissionDeniedException = IcePy.defineException('::Glacier2::PermissionDeniedException', PermissionDeniedException, (), None, (('reason', (), IcePy._t_string),))
    PermissionDeniedException.ice_type = _M_Glacier2._t_PermissionDeniedException

    _M_Glacier2.PermissionDeniedException = PermissionDeniedException
    del PermissionDeniedException

if not _M_Glacier2.__dict__.has_key('SessionNotExistException'):
    _M_Glacier2.SessionNotExistException = Ice.createTempClass()
    class SessionNotExistException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Glacier2::SessionNotExistException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Glacier2._t_SessionNotExistException = IcePy.defineException('::Glacier2::SessionNotExistException', SessionNotExistException, (), None, ())
    SessionNotExistException.ice_type = _M_Glacier2._t_SessionNotExistException

    _M_Glacier2.SessionNotExistException = SessionNotExistException
    del SessionNotExistException

if not _M_Glacier2.__dict__.has_key('Router'):
    _M_Glacier2.Router = Ice.createTempClass()
    class Router(_M_Ice.Router):
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.Router:
                raise RuntimeError('Glacier2.Router is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::Router', '::Ice::Object', '::Ice::Router')

        def ice_id(self, current=None):
            return '::Glacier2::Router'

        def ice_staticId():
            return '::Glacier2::Router'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def getCategoryForClient(self, current=None):
        # def createSession_async(self, _cb, userId, password, current=None):
        # def createSessionFromSecureConnection_async(self, _cb, current=None):
        # def destroySession(self, current=None):
        # def getSessionTimeout(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_Router)

        __repr__ = __str__

    _M_Glacier2.RouterPrx = Ice.createTempClass()
    class RouterPrx(_M_Ice.RouterPrx):

        def getCategoryForClient(self, _ctx=None):
            return _M_Glacier2.Router._op_getCategoryForClient.invoke(self, ((), _ctx))

        def createSession(self, userId, password, _ctx=None):
            return _M_Glacier2.Router._op_createSession.invoke(self, ((userId, password), _ctx))

        def createSessionFromSecureConnection(self, _ctx=None):
            return _M_Glacier2.Router._op_createSessionFromSecureConnection.invoke(self, ((), _ctx))

        def destroySession(self, _ctx=None):
            return _M_Glacier2.Router._op_destroySession.invoke(self, ((), _ctx))

        def destroySession_async(self, _cb, _ctx=None):
            return _M_Glacier2.Router._op_destroySession.invokeAsync(self, (_cb, (), _ctx))

        def getSessionTimeout(self, _ctx=None):
            return _M_Glacier2.Router._op_getSessionTimeout.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.RouterPrx.ice_checkedCast(proxy, '::Glacier2::Router', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.RouterPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_RouterPrx = IcePy.defineProxy('::Glacier2::Router', RouterPrx)

    _M_Glacier2._t_Router = IcePy.defineClass('::Glacier2::Router', Router, (), True, None, (_M_Ice._t_Router,), ())
    Router.ice_type = _M_Glacier2._t_Router

    Router._op_getCategoryForClient = IcePy.Operation('getCategoryForClient', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_string, ())
    Router._op_createSession = IcePy.Operation('createSession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), _M_Glacier2._t_SessionPrx, (_M_Glacier2._t_PermissionDeniedException, _M_Glacier2._t_CannotCreateSessionException))
    Router._op_createSessionFromSecureConnection = IcePy.Operation('createSessionFromSecureConnection', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (), (), _M_Glacier2._t_SessionPrx, (_M_Glacier2._t_PermissionDeniedException, _M_Glacier2._t_CannotCreateSessionException))
    Router._op_destroySession = IcePy.Operation('destroySession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, (_M_Glacier2._t_SessionNotExistException,))
    Router._op_getSessionTimeout = IcePy.Operation('getSessionTimeout', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_long, ())

    _M_Glacier2.Router = Router
    del Router

    _M_Glacier2.RouterPrx = RouterPrx
    del RouterPrx

if not _M_Glacier2.__dict__.has_key('Admin'):
    _M_Glacier2.Admin = Ice.createTempClass()
    class Admin(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.Admin:
                raise RuntimeError('Glacier2.Admin is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::Admin', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Glacier2::Admin'

        def ice_staticId():
            return '::Glacier2::Admin'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def shutdown(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_Admin)

        __repr__ = __str__

    _M_Glacier2.AdminPrx = Ice.createTempClass()
    class AdminPrx(Ice.ObjectPrx):

        def shutdown(self, _ctx=None):
            return _M_Glacier2.Admin._op_shutdown.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.AdminPrx.ice_checkedCast(proxy, '::Glacier2::Admin', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.AdminPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_AdminPrx = IcePy.defineProxy('::Glacier2::Admin', AdminPrx)

    _M_Glacier2._t_Admin = IcePy.defineClass('::Glacier2::Admin', Admin, (), True, None, (), ())
    Admin.ice_type = _M_Glacier2._t_Admin

    Admin._op_shutdown = IcePy.Operation('shutdown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())

    _M_Glacier2.Admin = Admin
    del Admin

    _M_Glacier2.AdminPrx = AdminPrx
    del AdminPrx

# End of module Glacier2

Ice.sliceChecksums["::Glacier2::Admin"] = "a2df2d4165d639f36f3adadca59f154b"
Ice.sliceChecksums["::Glacier2::PermissionDeniedException"] = "27def8d4569ab203b629b9162d530ba"
Ice.sliceChecksums["::Glacier2::Router"] = "b7924dd83f479f59a338391178466c"
Ice.sliceChecksums["::Glacier2::SessionNotExistException"] = "9b3392dc48a63f86d96c13662972328"
