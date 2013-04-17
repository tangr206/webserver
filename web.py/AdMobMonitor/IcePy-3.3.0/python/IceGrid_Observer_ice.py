# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Observer.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Glacier2_Session_ice
import IceGrid_Exception_ice
import IceGrid_Descriptor_ice
import IceGrid_Admin_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')

# Start of module IceGrid
__name__ = 'IceGrid'

if not _M_IceGrid.__dict__.has_key('ServerDynamicInfo'):
    _M_IceGrid.ServerDynamicInfo = Ice.createTempClass()
    class ServerDynamicInfo(object):
        def __init__(self, id='', state=_M_IceGrid.ServerState.Inactive, pid=0, enabled=False):
            self.id = id
            self.state = state
            self.pid = pid
            self.enabled = enabled

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.id)
            _h = 5 * _h + __builtin__.hash(self.state)
            _h = 5 * _h + __builtin__.hash(self.pid)
            _h = 5 * _h + __builtin__.hash(self.enabled)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.id < other.id:
                return -1
            elif self.id > other.id:
                return 1
            if self.state < other.state:
                return -1
            elif self.state > other.state:
                return 1
            if self.pid < other.pid:
                return -1
            elif self.pid > other.pid:
                return 1
            if self.enabled < other.enabled:
                return -1
            elif self.enabled > other.enabled:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ServerDynamicInfo)

        __repr__ = __str__

    _M_IceGrid._t_ServerDynamicInfo = IcePy.defineStruct('::IceGrid::ServerDynamicInfo', ServerDynamicInfo, (), (
        ('id', (), IcePy._t_string),
        ('state', (), _M_IceGrid._t_ServerState),
        ('pid', (), IcePy._t_int),
        ('enabled', (), IcePy._t_bool)
    ))

    _M_IceGrid.ServerDynamicInfo = ServerDynamicInfo
    del ServerDynamicInfo

if not _M_IceGrid.__dict__.has_key('_t_ServerDynamicInfoSeq'):
    _M_IceGrid._t_ServerDynamicInfoSeq = IcePy.defineSequence('::IceGrid::ServerDynamicInfoSeq', (), _M_IceGrid._t_ServerDynamicInfo)

if not _M_IceGrid.__dict__.has_key('AdapterDynamicInfo'):
    _M_IceGrid.AdapterDynamicInfo = Ice.createTempClass()
    class AdapterDynamicInfo(object):
        def __init__(self, id='', proxy=None):
            self.id = id
            self.proxy = proxy

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.id)
            _h = 5 * _h + __builtin__.hash(self.proxy)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.id < other.id:
                return -1
            elif self.id > other.id:
                return 1
            if self.proxy < other.proxy:
                return -1
            elif self.proxy > other.proxy:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_AdapterDynamicInfo)

        __repr__ = __str__

    _M_IceGrid._t_AdapterDynamicInfo = IcePy.defineStruct('::IceGrid::AdapterDynamicInfo', AdapterDynamicInfo, (), (
        ('id', (), IcePy._t_string),
        ('proxy', (), IcePy._t_ObjectPrx)
    ))

    _M_IceGrid.AdapterDynamicInfo = AdapterDynamicInfo
    del AdapterDynamicInfo

if not _M_IceGrid.__dict__.has_key('_t_AdapterDynamicInfoSeq'):
    _M_IceGrid._t_AdapterDynamicInfoSeq = IcePy.defineSequence('::IceGrid::AdapterDynamicInfoSeq', (), _M_IceGrid._t_AdapterDynamicInfo)

if not _M_IceGrid.__dict__.has_key('NodeDynamicInfo'):
    _M_IceGrid.NodeDynamicInfo = Ice.createTempClass()
    class NodeDynamicInfo(object):
        def __init__(self, info=Ice._struct_marker, servers=None, adapters=None):
            if info is Ice._struct_marker:
                self.info = _M_IceGrid.NodeInfo()
            else:
                self.info = info
            self.servers = servers
            self.adapters = adapters

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.info)
            if self.servers:
                for _i0 in self.servers:
                    _h = 5 * _h + __builtin__.hash(_i0)
            if self.adapters:
                for _i1 in self.adapters:
                    _h = 5 * _h + __builtin__.hash(_i1)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.info < other.info:
                return -1
            elif self.info > other.info:
                return 1
            if self.servers < other.servers:
                return -1
            elif self.servers > other.servers:
                return 1
            if self.adapters < other.adapters:
                return -1
            elif self.adapters > other.adapters:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_NodeDynamicInfo)

        __repr__ = __str__

    _M_IceGrid._t_NodeDynamicInfo = IcePy.defineStruct('::IceGrid::NodeDynamicInfo', NodeDynamicInfo, (), (
        ('info', (), _M_IceGrid._t_NodeInfo),
        ('servers', (), _M_IceGrid._t_ServerDynamicInfoSeq),
        ('adapters', (), _M_IceGrid._t_AdapterDynamicInfoSeq)
    ))

    _M_IceGrid.NodeDynamicInfo = NodeDynamicInfo
    del NodeDynamicInfo

if not _M_IceGrid.__dict__.has_key('_t_NodeDynamicInfoSeq'):
    _M_IceGrid._t_NodeDynamicInfoSeq = IcePy.defineSequence('::IceGrid::NodeDynamicInfoSeq', (), _M_IceGrid._t_NodeDynamicInfo)

if not _M_IceGrid.__dict__.has_key('NodeObserver'):
    _M_IceGrid.NodeObserver = Ice.createTempClass()
    class NodeObserver(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.NodeObserver:
                raise RuntimeError('IceGrid.NodeObserver is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::NodeObserver')

        def ice_id(self, current=None):
            return '::IceGrid::NodeObserver'

        def ice_staticId():
            return '::IceGrid::NodeObserver'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def nodeInit(self, nodes, current=None):
        # def nodeUp(self, node, current=None):
        # def nodeDown(self, name, current=None):
        # def updateServer(self, node, updatedInfo, current=None):
        # def updateAdapter(self, node, updatedInfo, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_NodeObserver)

        __repr__ = __str__

    _M_IceGrid.NodeObserverPrx = Ice.createTempClass()
    class NodeObserverPrx(Ice.ObjectPrx):

        def nodeInit(self, nodes, _ctx=None):
            return _M_IceGrid.NodeObserver._op_nodeInit.invoke(self, ((nodes, ), _ctx))

        def nodeInit_async(self, _cb, nodes, _ctx=None):
            return _M_IceGrid.NodeObserver._op_nodeInit.invokeAsync(self, (_cb, (nodes, ), _ctx))

        def nodeUp(self, node, _ctx=None):
            return _M_IceGrid.NodeObserver._op_nodeUp.invoke(self, ((node, ), _ctx))

        def nodeDown(self, name, _ctx=None):
            return _M_IceGrid.NodeObserver._op_nodeDown.invoke(self, ((name, ), _ctx))

        def updateServer(self, node, updatedInfo, _ctx=None):
            return _M_IceGrid.NodeObserver._op_updateServer.invoke(self, ((node, updatedInfo), _ctx))

        def updateAdapter(self, node, updatedInfo, _ctx=None):
            return _M_IceGrid.NodeObserver._op_updateAdapter.invoke(self, ((node, updatedInfo), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.NodeObserverPrx.ice_checkedCast(proxy, '::IceGrid::NodeObserver', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.NodeObserverPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_NodeObserverPrx = IcePy.defineProxy('::IceGrid::NodeObserver', NodeObserverPrx)

    _M_IceGrid._t_NodeObserver = IcePy.defineClass('::IceGrid::NodeObserver', NodeObserver, (), True, None, (), ())
    NodeObserver.ice_type = _M_IceGrid._t_NodeObserver

    NodeObserver._op_nodeInit = IcePy.Operation('nodeInit', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_NodeDynamicInfoSeq),), (), None, ())
    NodeObserver._op_nodeUp = IcePy.Operation('nodeUp', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_NodeDynamicInfo),), (), None, ())
    NodeObserver._op_nodeDown = IcePy.Operation('nodeDown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, ())
    NodeObserver._op_updateServer = IcePy.Operation('updateServer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), _M_IceGrid._t_ServerDynamicInfo)), (), None, ())
    NodeObserver._op_updateAdapter = IcePy.Operation('updateAdapter', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), _M_IceGrid._t_AdapterDynamicInfo)), (), None, ())

    _M_IceGrid.NodeObserver = NodeObserver
    del NodeObserver

    _M_IceGrid.NodeObserverPrx = NodeObserverPrx
    del NodeObserverPrx

if not _M_IceGrid.__dict__.has_key('ApplicationObserver'):
    _M_IceGrid.ApplicationObserver = Ice.createTempClass()
    class ApplicationObserver(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.ApplicationObserver:
                raise RuntimeError('IceGrid.ApplicationObserver is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::ApplicationObserver')

        def ice_id(self, current=None):
            return '::IceGrid::ApplicationObserver'

        def ice_staticId():
            return '::IceGrid::ApplicationObserver'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def applicationInit(self, serial, applications, current=None):
        # def applicationAdded(self, serial, desc, current=None):
        # def applicationRemoved(self, serial, name, current=None):
        # def applicationUpdated(self, serial, desc, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ApplicationObserver)

        __repr__ = __str__

    _M_IceGrid.ApplicationObserverPrx = Ice.createTempClass()
    class ApplicationObserverPrx(Ice.ObjectPrx):

        def applicationInit(self, serial, applications, _ctx=None):
            return _M_IceGrid.ApplicationObserver._op_applicationInit.invoke(self, ((serial, applications), _ctx))

        def applicationInit_async(self, _cb, serial, applications, _ctx=None):
            return _M_IceGrid.ApplicationObserver._op_applicationInit.invokeAsync(self, (_cb, (serial, applications), _ctx))

        def applicationAdded(self, serial, desc, _ctx=None):
            return _M_IceGrid.ApplicationObserver._op_applicationAdded.invoke(self, ((serial, desc), _ctx))

        def applicationRemoved(self, serial, name, _ctx=None):
            return _M_IceGrid.ApplicationObserver._op_applicationRemoved.invoke(self, ((serial, name), _ctx))

        def applicationUpdated(self, serial, desc, _ctx=None):
            return _M_IceGrid.ApplicationObserver._op_applicationUpdated.invoke(self, ((serial, desc), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.ApplicationObserverPrx.ice_checkedCast(proxy, '::IceGrid::ApplicationObserver', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.ApplicationObserverPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_ApplicationObserverPrx = IcePy.defineProxy('::IceGrid::ApplicationObserver', ApplicationObserverPrx)

    _M_IceGrid._t_ApplicationObserver = IcePy.defineClass('::IceGrid::ApplicationObserver', ApplicationObserver, (), True, None, (), ())
    ApplicationObserver.ice_type = _M_IceGrid._t_ApplicationObserver

    ApplicationObserver._op_applicationInit = IcePy.Operation('applicationInit', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_int), ((), _M_IceGrid._t_ApplicationInfoSeq)), (), None, ())
    ApplicationObserver._op_applicationAdded = IcePy.Operation('applicationAdded', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_int), ((), _M_IceGrid._t_ApplicationInfo)), (), None, ())
    ApplicationObserver._op_applicationRemoved = IcePy.Operation('applicationRemoved', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_int), ((), IcePy._t_string)), (), None, ())
    ApplicationObserver._op_applicationUpdated = IcePy.Operation('applicationUpdated', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_int), ((), _M_IceGrid._t_ApplicationUpdateInfo)), (), None, ())

    _M_IceGrid.ApplicationObserver = ApplicationObserver
    del ApplicationObserver

    _M_IceGrid.ApplicationObserverPrx = ApplicationObserverPrx
    del ApplicationObserverPrx

if not _M_IceGrid.__dict__.has_key('AdapterObserver'):
    _M_IceGrid.AdapterObserver = Ice.createTempClass()
    class AdapterObserver(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.AdapterObserver:
                raise RuntimeError('IceGrid.AdapterObserver is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::AdapterObserver')

        def ice_id(self, current=None):
            return '::IceGrid::AdapterObserver'

        def ice_staticId():
            return '::IceGrid::AdapterObserver'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def adapterInit(self, adpts, current=None):
        # def adapterAdded(self, info, current=None):
        # def adapterUpdated(self, info, current=None):
        # def adapterRemoved(self, id, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_AdapterObserver)

        __repr__ = __str__

    _M_IceGrid.AdapterObserverPrx = Ice.createTempClass()
    class AdapterObserverPrx(Ice.ObjectPrx):

        def adapterInit(self, adpts, _ctx=None):
            return _M_IceGrid.AdapterObserver._op_adapterInit.invoke(self, ((adpts, ), _ctx))

        def adapterInit_async(self, _cb, adpts, _ctx=None):
            return _M_IceGrid.AdapterObserver._op_adapterInit.invokeAsync(self, (_cb, (adpts, ), _ctx))

        def adapterAdded(self, info, _ctx=None):
            return _M_IceGrid.AdapterObserver._op_adapterAdded.invoke(self, ((info, ), _ctx))

        def adapterUpdated(self, info, _ctx=None):
            return _M_IceGrid.AdapterObserver._op_adapterUpdated.invoke(self, ((info, ), _ctx))

        def adapterRemoved(self, id, _ctx=None):
            return _M_IceGrid.AdapterObserver._op_adapterRemoved.invoke(self, ((id, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.AdapterObserverPrx.ice_checkedCast(proxy, '::IceGrid::AdapterObserver', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.AdapterObserverPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_AdapterObserverPrx = IcePy.defineProxy('::IceGrid::AdapterObserver', AdapterObserverPrx)

    _M_IceGrid._t_AdapterObserver = IcePy.defineClass('::IceGrid::AdapterObserver', AdapterObserver, (), True, None, (), ())
    AdapterObserver.ice_type = _M_IceGrid._t_AdapterObserver

    AdapterObserver._op_adapterInit = IcePy.Operation('adapterInit', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_AdapterInfoSeq),), (), None, ())
    AdapterObserver._op_adapterAdded = IcePy.Operation('adapterAdded', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_AdapterInfo),), (), None, ())
    AdapterObserver._op_adapterUpdated = IcePy.Operation('adapterUpdated', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_AdapterInfo),), (), None, ())
    AdapterObserver._op_adapterRemoved = IcePy.Operation('adapterRemoved', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, ())

    _M_IceGrid.AdapterObserver = AdapterObserver
    del AdapterObserver

    _M_IceGrid.AdapterObserverPrx = AdapterObserverPrx
    del AdapterObserverPrx

if not _M_IceGrid.__dict__.has_key('ObjectObserver'):
    _M_IceGrid.ObjectObserver = Ice.createTempClass()
    class ObjectObserver(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.ObjectObserver:
                raise RuntimeError('IceGrid.ObjectObserver is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::ObjectObserver')

        def ice_id(self, current=None):
            return '::IceGrid::ObjectObserver'

        def ice_staticId():
            return '::IceGrid::ObjectObserver'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def objectInit(self, objects, current=None):
        # def objectAdded(self, info, current=None):
        # def objectUpdated(self, info, current=None):
        # def objectRemoved(self, id, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ObjectObserver)

        __repr__ = __str__

    _M_IceGrid.ObjectObserverPrx = Ice.createTempClass()
    class ObjectObserverPrx(Ice.ObjectPrx):

        def objectInit(self, objects, _ctx=None):
            return _M_IceGrid.ObjectObserver._op_objectInit.invoke(self, ((objects, ), _ctx))

        def objectInit_async(self, _cb, objects, _ctx=None):
            return _M_IceGrid.ObjectObserver._op_objectInit.invokeAsync(self, (_cb, (objects, ), _ctx))

        def objectAdded(self, info, _ctx=None):
            return _M_IceGrid.ObjectObserver._op_objectAdded.invoke(self, ((info, ), _ctx))

        def objectUpdated(self, info, _ctx=None):
            return _M_IceGrid.ObjectObserver._op_objectUpdated.invoke(self, ((info, ), _ctx))

        def objectRemoved(self, id, _ctx=None):
            return _M_IceGrid.ObjectObserver._op_objectRemoved.invoke(self, ((id, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.ObjectObserverPrx.ice_checkedCast(proxy, '::IceGrid::ObjectObserver', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.ObjectObserverPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_ObjectObserverPrx = IcePy.defineProxy('::IceGrid::ObjectObserver', ObjectObserverPrx)

    _M_IceGrid._t_ObjectObserver = IcePy.defineClass('::IceGrid::ObjectObserver', ObjectObserver, (), True, None, (), ())
    ObjectObserver.ice_type = _M_IceGrid._t_ObjectObserver

    ObjectObserver._op_objectInit = IcePy.Operation('objectInit', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_ObjectInfoSeq),), (), None, ())
    ObjectObserver._op_objectAdded = IcePy.Operation('objectAdded', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_ObjectInfo),), (), None, ())
    ObjectObserver._op_objectUpdated = IcePy.Operation('objectUpdated', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_ObjectInfo),), (), None, ())
    ObjectObserver._op_objectRemoved = IcePy.Operation('objectRemoved', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_Ice._t_Identity),), (), None, ())

    _M_IceGrid.ObjectObserver = ObjectObserver
    del ObjectObserver

    _M_IceGrid.ObjectObserverPrx = ObjectObserverPrx
    del ObjectObserverPrx

if not _M_IceGrid.__dict__.has_key('RegistryObserver'):
    _M_IceGrid.RegistryObserver = Ice.createTempClass()
    class RegistryObserver(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.RegistryObserver:
                raise RuntimeError('IceGrid.RegistryObserver is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::RegistryObserver')

        def ice_id(self, current=None):
            return '::IceGrid::RegistryObserver'

        def ice_staticId():
            return '::IceGrid::RegistryObserver'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def registryInit(self, registries, current=None):
        # def registryUp(self, node, current=None):
        # def registryDown(self, name, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_RegistryObserver)

        __repr__ = __str__

    _M_IceGrid.RegistryObserverPrx = Ice.createTempClass()
    class RegistryObserverPrx(Ice.ObjectPrx):

        def registryInit(self, registries, _ctx=None):
            return _M_IceGrid.RegistryObserver._op_registryInit.invoke(self, ((registries, ), _ctx))

        def registryInit_async(self, _cb, registries, _ctx=None):
            return _M_IceGrid.RegistryObserver._op_registryInit.invokeAsync(self, (_cb, (registries, ), _ctx))

        def registryUp(self, node, _ctx=None):
            return _M_IceGrid.RegistryObserver._op_registryUp.invoke(self, ((node, ), _ctx))

        def registryDown(self, name, _ctx=None):
            return _M_IceGrid.RegistryObserver._op_registryDown.invoke(self, ((name, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.RegistryObserverPrx.ice_checkedCast(proxy, '::IceGrid::RegistryObserver', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.RegistryObserverPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_RegistryObserverPrx = IcePy.defineProxy('::IceGrid::RegistryObserver', RegistryObserverPrx)

    _M_IceGrid._t_RegistryObserver = IcePy.defineClass('::IceGrid::RegistryObserver', RegistryObserver, (), True, None, (), ())
    RegistryObserver.ice_type = _M_IceGrid._t_RegistryObserver

    RegistryObserver._op_registryInit = IcePy.Operation('registryInit', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_RegistryInfoSeq),), (), None, ())
    RegistryObserver._op_registryUp = IcePy.Operation('registryUp', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_RegistryInfo),), (), None, ())
    RegistryObserver._op_registryDown = IcePy.Operation('registryDown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, ())

    _M_IceGrid.RegistryObserver = RegistryObserver
    del RegistryObserver

    _M_IceGrid.RegistryObserverPrx = RegistryObserverPrx
    del RegistryObserverPrx

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::AdapterDynamicInfo"] = "b371e9a58f115e6ebfbcda735fee57f7"
Ice.sliceChecksums["::IceGrid::AdapterDynamicInfoSeq"] = "54465843167a2f93fa96d13b7f41ea32"
Ice.sliceChecksums["::IceGrid::AdapterObserver"] = "7f4ed59e236da9d6c35ad7e6ad9cb0"
Ice.sliceChecksums["::IceGrid::ApplicationObserver"] = "2862cdcba54714282f68b13a8fb4ae"
Ice.sliceChecksums["::IceGrid::NodeDynamicInfo"] = "3ad52341f32973212d26a9a6dda08b"
Ice.sliceChecksums["::IceGrid::NodeDynamicInfoSeq"] = "f61633c5e3992f718dba78b7f165c2"
Ice.sliceChecksums["::IceGrid::NodeObserver"] = "e06c1ad6807d2876de9e818855a65738"
Ice.sliceChecksums["::IceGrid::ObjectObserver"] = "5364683a872f127e46cc5e215d98c3c"
Ice.sliceChecksums["::IceGrid::RegistryObserver"] = "fd83b1558e7c77f2d322b25449518"
Ice.sliceChecksums["::IceGrid::ServerDynamicInfo"] = "fd4b9177ca54ae4688b51fa51d6870"
Ice.sliceChecksums["::IceGrid::ServerDynamicInfoSeq"] = "e3fda58997d5cd946e78cae739174cb"
