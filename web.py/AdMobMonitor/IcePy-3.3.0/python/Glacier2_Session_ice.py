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
import Ice_BuiltinSequences_ice
import Ice_Identity_ice
import Glacier2_SSLInfo_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Start of module Glacier2
__name__ = 'Glacier2'

if not _M_Glacier2.__dict__.has_key('CannotCreateSessionException'):
    _M_Glacier2.CannotCreateSessionException = Ice.createTempClass()
    class CannotCreateSessionException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'Glacier2::CannotCreateSessionException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Glacier2._t_CannotCreateSessionException = IcePy.defineException('::Glacier2::CannotCreateSessionException', CannotCreateSessionException, (), None, (('reason', (), IcePy._t_string),))
    CannotCreateSessionException.ice_type = _M_Glacier2._t_CannotCreateSessionException

    _M_Glacier2.CannotCreateSessionException = CannotCreateSessionException
    del CannotCreateSessionException

if not _M_Glacier2.__dict__.has_key('Session'):
    _M_Glacier2.Session = Ice.createTempClass()
    class Session(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.Session:
                raise RuntimeError('Glacier2.Session is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::Session', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Glacier2::Session'

        def ice_staticId():
            return '::Glacier2::Session'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def destroy(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_Session)

        __repr__ = __str__

    _M_Glacier2.SessionPrx = Ice.createTempClass()
    class SessionPrx(Ice.ObjectPrx):

        def destroy(self, _ctx=None):
            return _M_Glacier2.Session._op_destroy.invoke(self, ((), _ctx))

        def destroy_async(self, _cb, _ctx=None):
            return _M_Glacier2.Session._op_destroy.invokeAsync(self, (_cb, (), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.SessionPrx.ice_checkedCast(proxy, '::Glacier2::Session', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.SessionPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_SessionPrx = IcePy.defineProxy('::Glacier2::Session', SessionPrx)

    _M_Glacier2._t_Session = IcePy.defineClass('::Glacier2::Session', Session, (), True, None, (), ())
    Session.ice_type = _M_Glacier2._t_Session

    Session._op_destroy = IcePy.Operation('destroy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())

    _M_Glacier2.Session = Session
    del Session

    _M_Glacier2.SessionPrx = SessionPrx
    del SessionPrx

if not _M_Glacier2.__dict__.has_key('StringSet'):
    _M_Glacier2.StringSet = Ice.createTempClass()
    class StringSet(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.StringSet:
                raise RuntimeError('Glacier2.StringSet is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::StringSet', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Glacier2::StringSet'

        def ice_staticId():
            return '::Glacier2::StringSet'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def add(self, additions, current=None):
        # def remove(self, deletions, current=None):
        # def get(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_StringSet)

        __repr__ = __str__

    _M_Glacier2.StringSetPrx = Ice.createTempClass()
    class StringSetPrx(Ice.ObjectPrx):

        def add(self, additions, _ctx=None):
            return _M_Glacier2.StringSet._op_add.invoke(self, ((additions, ), _ctx))

        def remove(self, deletions, _ctx=None):
            return _M_Glacier2.StringSet._op_remove.invoke(self, ((deletions, ), _ctx))

        def get(self, _ctx=None):
            return _M_Glacier2.StringSet._op_get.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.StringSetPrx.ice_checkedCast(proxy, '::Glacier2::StringSet', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.StringSetPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_StringSetPrx = IcePy.defineProxy('::Glacier2::StringSet', StringSetPrx)

    _M_Glacier2._t_StringSet = IcePy.defineClass('::Glacier2::StringSet', StringSet, (), True, None, (), ())
    StringSet.ice_type = _M_Glacier2._t_StringSet

    StringSet._op_add = IcePy.Operation('add', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), _M_Ice._t_StringSeq),), (), None, ())
    StringSet._op_remove = IcePy.Operation('remove', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), _M_Ice._t_StringSeq),), (), None, ())
    StringSet._op_get = IcePy.Operation('get', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), _M_Ice._t_StringSeq, ())

    _M_Glacier2.StringSet = StringSet
    del StringSet

    _M_Glacier2.StringSetPrx = StringSetPrx
    del StringSetPrx

if not _M_Glacier2.__dict__.has_key('IdentitySet'):
    _M_Glacier2.IdentitySet = Ice.createTempClass()
    class IdentitySet(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.IdentitySet:
                raise RuntimeError('Glacier2.IdentitySet is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::IdentitySet', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Glacier2::IdentitySet'

        def ice_staticId():
            return '::Glacier2::IdentitySet'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def add(self, additions, current=None):
        # def remove(self, deletions, current=None):
        # def get(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_IdentitySet)

        __repr__ = __str__

    _M_Glacier2.IdentitySetPrx = Ice.createTempClass()
    class IdentitySetPrx(Ice.ObjectPrx):

        def add(self, additions, _ctx=None):
            return _M_Glacier2.IdentitySet._op_add.invoke(self, ((additions, ), _ctx))

        def remove(self, deletions, _ctx=None):
            return _M_Glacier2.IdentitySet._op_remove.invoke(self, ((deletions, ), _ctx))

        def get(self, _ctx=None):
            return _M_Glacier2.IdentitySet._op_get.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.IdentitySetPrx.ice_checkedCast(proxy, '::Glacier2::IdentitySet', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.IdentitySetPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_IdentitySetPrx = IcePy.defineProxy('::Glacier2::IdentitySet', IdentitySetPrx)

    _M_Glacier2._t_IdentitySet = IcePy.defineClass('::Glacier2::IdentitySet', IdentitySet, (), True, None, (), ())
    IdentitySet.ice_type = _M_Glacier2._t_IdentitySet

    IdentitySet._op_add = IcePy.Operation('add', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), _M_Ice._t_IdentitySeq),), (), None, ())
    IdentitySet._op_remove = IcePy.Operation('remove', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), _M_Ice._t_IdentitySeq),), (), None, ())
    IdentitySet._op_get = IcePy.Operation('get', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), _M_Ice._t_IdentitySeq, ())

    _M_Glacier2.IdentitySet = IdentitySet
    del IdentitySet

    _M_Glacier2.IdentitySetPrx = IdentitySetPrx
    del IdentitySetPrx

if not _M_Glacier2.__dict__.has_key('SessionControl'):
    _M_Glacier2.SessionControl = Ice.createTempClass()
    class SessionControl(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.SessionControl:
                raise RuntimeError('Glacier2.SessionControl is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::SessionControl', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Glacier2::SessionControl'

        def ice_staticId():
            return '::Glacier2::SessionControl'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def categories(self, current=None):
        # def adapterIds(self, current=None):
        # def identities(self, current=None):
        # def getSessionTimeout(self, current=None):
        # def destroy(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_SessionControl)

        __repr__ = __str__

    _M_Glacier2.SessionControlPrx = Ice.createTempClass()
    class SessionControlPrx(Ice.ObjectPrx):

        def categories(self, _ctx=None):
            return _M_Glacier2.SessionControl._op_categories.invoke(self, ((), _ctx))

        def adapterIds(self, _ctx=None):
            return _M_Glacier2.SessionControl._op_adapterIds.invoke(self, ((), _ctx))

        def identities(self, _ctx=None):
            return _M_Glacier2.SessionControl._op_identities.invoke(self, ((), _ctx))

        def getSessionTimeout(self, _ctx=None):
            return _M_Glacier2.SessionControl._op_getSessionTimeout.invoke(self, ((), _ctx))

        def destroy(self, _ctx=None):
            return _M_Glacier2.SessionControl._op_destroy.invoke(self, ((), _ctx))

        def destroy_async(self, _cb, _ctx=None):
            return _M_Glacier2.SessionControl._op_destroy.invokeAsync(self, (_cb, (), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.SessionControlPrx.ice_checkedCast(proxy, '::Glacier2::SessionControl', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.SessionControlPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_SessionControlPrx = IcePy.defineProxy('::Glacier2::SessionControl', SessionControlPrx)

    _M_Glacier2._t_SessionControl = IcePy.defineClass('::Glacier2::SessionControl', SessionControl, (), True, None, (), ())
    SessionControl.ice_type = _M_Glacier2._t_SessionControl

    SessionControl._op_categories = IcePy.Operation('categories', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_Glacier2._t_StringSetPrx, ())
    SessionControl._op_adapterIds = IcePy.Operation('adapterIds', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_Glacier2._t_StringSetPrx, ())
    SessionControl._op_identities = IcePy.Operation('identities', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_Glacier2._t_IdentitySetPrx, ())
    SessionControl._op_getSessionTimeout = IcePy.Operation('getSessionTimeout', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), IcePy._t_int, ())
    SessionControl._op_destroy = IcePy.Operation('destroy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())

    _M_Glacier2.SessionControl = SessionControl
    del SessionControl

    _M_Glacier2.SessionControlPrx = SessionControlPrx
    del SessionControlPrx

if not _M_Glacier2.__dict__.has_key('SessionManager'):
    _M_Glacier2.SessionManager = Ice.createTempClass()
    class SessionManager(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.SessionManager:
                raise RuntimeError('Glacier2.SessionManager is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::SessionManager', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Glacier2::SessionManager'

        def ice_staticId():
            return '::Glacier2::SessionManager'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def create(self, userId, control, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_SessionManager)

        __repr__ = __str__

    _M_Glacier2.SessionManagerPrx = Ice.createTempClass()
    class SessionManagerPrx(Ice.ObjectPrx):

        def create(self, userId, control, _ctx=None):
            return _M_Glacier2.SessionManager._op_create.invoke(self, ((userId, control), _ctx))

        def create_async(self, _cb, userId, control, _ctx=None):
            return _M_Glacier2.SessionManager._op_create.invokeAsync(self, (_cb, (userId, control), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.SessionManagerPrx.ice_checkedCast(proxy, '::Glacier2::SessionManager', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.SessionManagerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_SessionManagerPrx = IcePy.defineProxy('::Glacier2::SessionManager', SessionManagerPrx)

    _M_Glacier2._t_SessionManager = IcePy.defineClass('::Glacier2::SessionManager', SessionManager, (), True, None, (), ())
    SessionManager.ice_type = _M_Glacier2._t_SessionManager

    SessionManager._op_create = IcePy.Operation('create', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), _M_Glacier2._t_SessionControlPrx)), (), _M_Glacier2._t_SessionPrx, (_M_Glacier2._t_CannotCreateSessionException,))

    _M_Glacier2.SessionManager = SessionManager
    del SessionManager

    _M_Glacier2.SessionManagerPrx = SessionManagerPrx
    del SessionManagerPrx

if not _M_Glacier2.__dict__.has_key('SSLSessionManager'):
    _M_Glacier2.SSLSessionManager = Ice.createTempClass()
    class SSLSessionManager(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.SSLSessionManager:
                raise RuntimeError('Glacier2.SSLSessionManager is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::SSLSessionManager', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Glacier2::SSLSessionManager'

        def ice_staticId():
            return '::Glacier2::SSLSessionManager'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def create(self, info, control, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_SSLSessionManager)

        __repr__ = __str__

    _M_Glacier2.SSLSessionManagerPrx = Ice.createTempClass()
    class SSLSessionManagerPrx(Ice.ObjectPrx):

        def create(self, info, control, _ctx=None):
            return _M_Glacier2.SSLSessionManager._op_create.invoke(self, ((info, control), _ctx))

        def create_async(self, _cb, info, control, _ctx=None):
            return _M_Glacier2.SSLSessionManager._op_create.invokeAsync(self, (_cb, (info, control), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.SSLSessionManagerPrx.ice_checkedCast(proxy, '::Glacier2::SSLSessionManager', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.SSLSessionManagerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_SSLSessionManagerPrx = IcePy.defineProxy('::Glacier2::SSLSessionManager', SSLSessionManagerPrx)

    _M_Glacier2._t_SSLSessionManager = IcePy.defineClass('::Glacier2::SSLSessionManager', SSLSessionManager, (), True, None, (), ())
    SSLSessionManager.ice_type = _M_Glacier2._t_SSLSessionManager

    SSLSessionManager._op_create = IcePy.Operation('create', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_Glacier2._t_SSLInfo), ((), _M_Glacier2._t_SessionControlPrx)), (), _M_Glacier2._t_SessionPrx, (_M_Glacier2._t_CannotCreateSessionException,))

    _M_Glacier2.SSLSessionManager = SSLSessionManager
    del SSLSessionManager

    _M_Glacier2.SSLSessionManagerPrx = SSLSessionManagerPrx
    del SSLSessionManagerPrx

# End of module Glacier2

Ice.sliceChecksums["::Glacier2::CannotCreateSessionException"] = "f3cf2057ea305ed04671164dfaeb6d95"
Ice.sliceChecksums["::Glacier2::IdentitySet"] = "622e43adfd1f535abaee1b089583847"
Ice.sliceChecksums["::Glacier2::SSLSessionManager"] = "4eb77cf437452f5296bf24dda4967d"
Ice.sliceChecksums["::Glacier2::Session"] = "8e47590dc18dd2a2e2e7749c941fc7"
Ice.sliceChecksums["::Glacier2::SessionControl"] = "83a11c547492ddc72db70659938222"
Ice.sliceChecksums["::Glacier2::SessionManager"] = "f3c67f2f29415754c0f1ccc1ab5558e"
Ice.sliceChecksums["::Glacier2::StringSet"] = "1b46953cdce5ef8b6fe92056adf3fda0"
