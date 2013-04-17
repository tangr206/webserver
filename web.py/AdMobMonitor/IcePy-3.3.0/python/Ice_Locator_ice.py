# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Locator.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_Identity_ice
import Ice_ProcessF_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('AdapterNotFoundException'):
    _M_Ice.AdapterNotFoundException = Ice.createTempClass()
    class AdapterNotFoundException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::AdapterNotFoundException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_AdapterNotFoundException = IcePy.defineException('::Ice::AdapterNotFoundException', AdapterNotFoundException, (), None, ())
    AdapterNotFoundException.ice_type = _M_Ice._t_AdapterNotFoundException

    _M_Ice.AdapterNotFoundException = AdapterNotFoundException
    del AdapterNotFoundException

if not _M_Ice.__dict__.has_key('InvalidReplicaGroupIdException'):
    _M_Ice.InvalidReplicaGroupIdException = Ice.createTempClass()
    class InvalidReplicaGroupIdException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::InvalidReplicaGroupIdException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_InvalidReplicaGroupIdException = IcePy.defineException('::Ice::InvalidReplicaGroupIdException', InvalidReplicaGroupIdException, (), None, ())
    InvalidReplicaGroupIdException.ice_type = _M_Ice._t_InvalidReplicaGroupIdException

    _M_Ice.InvalidReplicaGroupIdException = InvalidReplicaGroupIdException
    del InvalidReplicaGroupIdException

if not _M_Ice.__dict__.has_key('AdapterAlreadyActiveException'):
    _M_Ice.AdapterAlreadyActiveException = Ice.createTempClass()
    class AdapterAlreadyActiveException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::AdapterAlreadyActiveException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_AdapterAlreadyActiveException = IcePy.defineException('::Ice::AdapterAlreadyActiveException', AdapterAlreadyActiveException, (), None, ())
    AdapterAlreadyActiveException.ice_type = _M_Ice._t_AdapterAlreadyActiveException

    _M_Ice.AdapterAlreadyActiveException = AdapterAlreadyActiveException
    del AdapterAlreadyActiveException

if not _M_Ice.__dict__.has_key('ObjectNotFoundException'):
    _M_Ice.ObjectNotFoundException = Ice.createTempClass()
    class ObjectNotFoundException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::ObjectNotFoundException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ObjectNotFoundException = IcePy.defineException('::Ice::ObjectNotFoundException', ObjectNotFoundException, (), None, ())
    ObjectNotFoundException.ice_type = _M_Ice._t_ObjectNotFoundException

    _M_Ice.ObjectNotFoundException = ObjectNotFoundException
    del ObjectNotFoundException

if not _M_Ice.__dict__.has_key('ServerNotFoundException'):
    _M_Ice.ServerNotFoundException = Ice.createTempClass()
    class ServerNotFoundException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::ServerNotFoundException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ServerNotFoundException = IcePy.defineException('::Ice::ServerNotFoundException', ServerNotFoundException, (), None, ())
    ServerNotFoundException.ice_type = _M_Ice._t_ServerNotFoundException

    _M_Ice.ServerNotFoundException = ServerNotFoundException
    del ServerNotFoundException

if not _M_Ice.__dict__.has_key('LocatorRegistry'):
    _M_Ice._t_LocatorRegistry = IcePy.declareClass('::Ice::LocatorRegistry')
    _M_Ice._t_LocatorRegistryPrx = IcePy.declareProxy('::Ice::LocatorRegistry')

if not _M_Ice.__dict__.has_key('Locator'):
    _M_Ice.Locator = Ice.createTempClass()
    class Locator(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Locator:
                raise RuntimeError('Ice.Locator is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Locator', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Ice::Locator'

        def ice_staticId():
            return '::Ice::Locator'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def findObjectById_async(self, _cb, id, current=None):
        # def findAdapterById_async(self, _cb, id, current=None):
        # def getRegistry(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Locator)

        __repr__ = __str__

    _M_Ice.LocatorPrx = Ice.createTempClass()
    class LocatorPrx(Ice.ObjectPrx):

        def findObjectById(self, id, _ctx=None):
            return _M_Ice.Locator._op_findObjectById.invoke(self, ((id, ), _ctx))

        def findObjectById_async(self, _cb, id, _ctx=None):
            return _M_Ice.Locator._op_findObjectById.invokeAsync(self, (_cb, (id, ), _ctx))

        def findAdapterById(self, id, _ctx=None):
            return _M_Ice.Locator._op_findAdapterById.invoke(self, ((id, ), _ctx))

        def findAdapterById_async(self, _cb, id, _ctx=None):
            return _M_Ice.Locator._op_findAdapterById.invokeAsync(self, (_cb, (id, ), _ctx))

        def getRegistry(self, _ctx=None):
            return _M_Ice.Locator._op_getRegistry.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Ice.LocatorPrx.ice_checkedCast(proxy, '::Ice::Locator', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Ice.LocatorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Ice._t_LocatorPrx = IcePy.defineProxy('::Ice::Locator', LocatorPrx)

    _M_Ice._t_Locator = IcePy.defineClass('::Ice::Locator', Locator, (), True, None, (), ())
    Locator.ice_type = _M_Ice._t_Locator

    Locator._op_findObjectById = IcePy.Operation('findObjectById', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, True, (), (((), _M_Ice._t_Identity),), (), IcePy._t_ObjectPrx, (_M_Ice._t_ObjectNotFoundException,))
    Locator._op_findAdapterById = IcePy.Operation('findAdapterById', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, True, (), (((), IcePy._t_string),), (), IcePy._t_ObjectPrx, (_M_Ice._t_AdapterNotFoundException,))
    Locator._op_getRegistry = IcePy.Operation('getRegistry', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_LocatorRegistryPrx, ())

    _M_Ice.Locator = Locator
    del Locator

    _M_Ice.LocatorPrx = LocatorPrx
    del LocatorPrx

if not _M_Ice.__dict__.has_key('LocatorRegistry'):
    _M_Ice.LocatorRegistry = Ice.createTempClass()
    class LocatorRegistry(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.LocatorRegistry:
                raise RuntimeError('Ice.LocatorRegistry is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::LocatorRegistry', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Ice::LocatorRegistry'

        def ice_staticId():
            return '::Ice::LocatorRegistry'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def setAdapterDirectProxy_async(self, _cb, id, proxy, current=None):
        # def setReplicatedAdapterDirectProxy_async(self, _cb, adapterId, replicaGroupId, p, current=None):
        # def setServerProcessProxy_async(self, _cb, id, proxy, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_LocatorRegistry)

        __repr__ = __str__

    _M_Ice.LocatorRegistryPrx = Ice.createTempClass()
    class LocatorRegistryPrx(Ice.ObjectPrx):

        def setAdapterDirectProxy(self, id, proxy, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setAdapterDirectProxy.invoke(self, ((id, proxy), _ctx))

        def setAdapterDirectProxy_async(self, _cb, id, proxy, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setAdapterDirectProxy.invokeAsync(self, (_cb, (id, proxy), _ctx))

        def setReplicatedAdapterDirectProxy(self, adapterId, replicaGroupId, p, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setReplicatedAdapterDirectProxy.invoke(self, ((adapterId, replicaGroupId, p), _ctx))

        def setReplicatedAdapterDirectProxy_async(self, _cb, adapterId, replicaGroupId, p, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setReplicatedAdapterDirectProxy.invokeAsync(self, (_cb, (adapterId, replicaGroupId, p), _ctx))

        def setServerProcessProxy(self, id, proxy, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setServerProcessProxy.invoke(self, ((id, proxy), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Ice.LocatorRegistryPrx.ice_checkedCast(proxy, '::Ice::LocatorRegistry', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Ice.LocatorRegistryPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Ice._t_LocatorRegistryPrx = IcePy.defineProxy('::Ice::LocatorRegistry', LocatorRegistryPrx)

    _M_Ice._t_LocatorRegistry = IcePy.defineClass('::Ice::LocatorRegistry', LocatorRegistry, (), True, None, (), ())
    LocatorRegistry.ice_type = _M_Ice._t_LocatorRegistry

    LocatorRegistry._op_setAdapterDirectProxy = IcePy.Operation('setAdapterDirectProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), IcePy._t_ObjectPrx)), (), None, (_M_Ice._t_AdapterNotFoundException, _M_Ice._t_AdapterAlreadyActiveException))
    LocatorRegistry._op_setReplicatedAdapterDirectProxy = IcePy.Operation('setReplicatedAdapterDirectProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), IcePy._t_string), ((), IcePy._t_ObjectPrx)), (), None, (_M_Ice._t_AdapterNotFoundException, _M_Ice._t_AdapterAlreadyActiveException, _M_Ice._t_InvalidReplicaGroupIdException))
    LocatorRegistry._op_setServerProcessProxy = IcePy.Operation('setServerProcessProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), _M_Ice._t_ProcessPrx)), (), None, (_M_Ice._t_ServerNotFoundException,))

    _M_Ice.LocatorRegistry = LocatorRegistry
    del LocatorRegistry

    _M_Ice.LocatorRegistryPrx = LocatorRegistryPrx
    del LocatorRegistryPrx

# End of module Ice
