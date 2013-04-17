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
import Ice_BuiltinSequences_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Router'):
    _M_Ice.Router = Ice.createTempClass()
    class Router(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Router:
                raise RuntimeError('Ice.Router is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Ice::Router')

        def ice_id(self, current=None):
            return '::Ice::Router'

        def ice_staticId():
            return '::Ice::Router'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def getClientProxy(self, current=None):
        # def getServerProxy(self, current=None):
        # def addProxy(self, proxy, current=None):
        # def addProxies(self, proxies, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Router)

        __repr__ = __str__

    _M_Ice.RouterPrx = Ice.createTempClass()
    class RouterPrx(Ice.ObjectPrx):

        def getClientProxy(self, _ctx=None):
            return _M_Ice.Router._op_getClientProxy.invoke(self, ((), _ctx))

        def getClientProxy_async(self, _cb, _ctx=None):
            return _M_Ice.Router._op_getClientProxy.invokeAsync(self, (_cb, (), _ctx))

        def getServerProxy(self, _ctx=None):
            return _M_Ice.Router._op_getServerProxy.invoke(self, ((), _ctx))

        def addProxy(self, proxy, _ctx=None):
            return _M_Ice.Router._op_addProxy.invoke(self, ((proxy, ), _ctx))

        def addProxies(self, proxies, _ctx=None):
            return _M_Ice.Router._op_addProxies.invoke(self, ((proxies, ), _ctx))

        def addProxies_async(self, _cb, proxies, _ctx=None):
            return _M_Ice.Router._op_addProxies.invokeAsync(self, (_cb, (proxies, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Ice.RouterPrx.ice_checkedCast(proxy, '::Ice::Router', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Ice.RouterPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Ice._t_RouterPrx = IcePy.defineProxy('::Ice::Router', RouterPrx)

    _M_Ice._t_Router = IcePy.defineClass('::Ice::Router', Router, (), True, None, (), ())
    Router.ice_type = _M_Ice._t_Router

    Router._op_getClientProxy = IcePy.Operation('getClientProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_ObjectPrx, ())
    Router._op_getServerProxy = IcePy.Operation('getServerProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_ObjectPrx, ())
    Router._op_addProxy = IcePy.Operation('addProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_ObjectPrx),), (), None, ())
    Router._op_addProxy.deprecate("addProxy() is deprecated, use addProxies() instead.")
    Router._op_addProxies = IcePy.Operation('addProxies', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), _M_Ice._t_ObjectProxySeq),), (), _M_Ice._t_ObjectProxySeq, ())

    _M_Ice.Router = Router
    del Router

    _M_Ice.RouterPrx = RouterPrx
    del RouterPrx

# End of module Ice
