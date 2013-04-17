# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `PermissionsVerifier.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Glacier2_SSLInfo_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Start of module Glacier2
__name__ = 'Glacier2'

if not _M_Glacier2.__dict__.has_key('PermissionsVerifier'):
    _M_Glacier2.PermissionsVerifier = Ice.createTempClass()
    class PermissionsVerifier(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.PermissionsVerifier:
                raise RuntimeError('Glacier2.PermissionsVerifier is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::PermissionsVerifier', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Glacier2::PermissionsVerifier'

        def ice_staticId():
            return '::Glacier2::PermissionsVerifier'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def checkPermissions(self, userId, password, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_PermissionsVerifier)

        __repr__ = __str__

    _M_Glacier2.PermissionsVerifierPrx = Ice.createTempClass()
    class PermissionsVerifierPrx(Ice.ObjectPrx):

        def checkPermissions(self, userId, password, _ctx=None):
            return _M_Glacier2.PermissionsVerifier._op_checkPermissions.invoke(self, ((userId, password), _ctx))

        def checkPermissions_async(self, _cb, userId, password, _ctx=None):
            return _M_Glacier2.PermissionsVerifier._op_checkPermissions.invokeAsync(self, (_cb, (userId, password), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.PermissionsVerifierPrx.ice_checkedCast(proxy, '::Glacier2::PermissionsVerifier', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.PermissionsVerifierPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_PermissionsVerifierPrx = IcePy.defineProxy('::Glacier2::PermissionsVerifier', PermissionsVerifierPrx)

    _M_Glacier2._t_PermissionsVerifier = IcePy.defineClass('::Glacier2::PermissionsVerifier', PermissionsVerifier, (), True, None, (), ())
    PermissionsVerifier.ice_type = _M_Glacier2._t_PermissionsVerifier

    PermissionsVerifier._op_checkPermissions = IcePy.Operation('checkPermissions', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (((), IcePy._t_string),), IcePy._t_bool, ())

    _M_Glacier2.PermissionsVerifier = PermissionsVerifier
    del PermissionsVerifier

    _M_Glacier2.PermissionsVerifierPrx = PermissionsVerifierPrx
    del PermissionsVerifierPrx

if not _M_Glacier2.__dict__.has_key('SSLPermissionsVerifier'):
    _M_Glacier2.SSLPermissionsVerifier = Ice.createTempClass()
    class SSLPermissionsVerifier(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.SSLPermissionsVerifier:
                raise RuntimeError('Glacier2.SSLPermissionsVerifier is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::SSLPermissionsVerifier', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Glacier2::SSLPermissionsVerifier'

        def ice_staticId():
            return '::Glacier2::SSLPermissionsVerifier'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def authorize(self, info, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_SSLPermissionsVerifier)

        __repr__ = __str__

    _M_Glacier2.SSLPermissionsVerifierPrx = Ice.createTempClass()
    class SSLPermissionsVerifierPrx(Ice.ObjectPrx):

        def authorize(self, info, _ctx=None):
            return _M_Glacier2.SSLPermissionsVerifier._op_authorize.invoke(self, ((info, ), _ctx))

        def authorize_async(self, _cb, info, _ctx=None):
            return _M_Glacier2.SSLPermissionsVerifier._op_authorize.invokeAsync(self, (_cb, (info, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.SSLPermissionsVerifierPrx.ice_checkedCast(proxy, '::Glacier2::SSLPermissionsVerifier', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.SSLPermissionsVerifierPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_SSLPermissionsVerifierPrx = IcePy.defineProxy('::Glacier2::SSLPermissionsVerifier', SSLPermissionsVerifierPrx)

    _M_Glacier2._t_SSLPermissionsVerifier = IcePy.defineClass('::Glacier2::SSLPermissionsVerifier', SSLPermissionsVerifier, (), True, None, (), ())
    SSLPermissionsVerifier.ice_type = _M_Glacier2._t_SSLPermissionsVerifier

    SSLPermissionsVerifier._op_authorize = IcePy.Operation('authorize', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), _M_Glacier2._t_SSLInfo),), (((), IcePy._t_string),), IcePy._t_bool, ())

    _M_Glacier2.SSLPermissionsVerifier = SSLPermissionsVerifier
    del SSLPermissionsVerifier

    _M_Glacier2.SSLPermissionsVerifierPrx = SSLPermissionsVerifierPrx
    del SSLPermissionsVerifierPrx

# End of module Glacier2

Ice.sliceChecksums["::Glacier2::PermissionsVerifier"] = "224cf229a378614459a5959f346c50"
Ice.sliceChecksums["::Glacier2::SSLPermissionsVerifier"] = "b796e7d91f35d3acbb5be98291aa9be4"
