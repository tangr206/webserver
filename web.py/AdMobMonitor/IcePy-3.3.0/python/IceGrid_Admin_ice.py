# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Admin.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_Identity_ice
import Ice_BuiltinSequences_ice
import Ice_Properties_ice
import Ice_SliceChecksumDict_ice
import Glacier2_Session_ice
import IceGrid_Exception_ice
import IceGrid_Descriptor_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')

# Start of module IceGrid
__name__ = 'IceGrid'

if not _M_IceGrid.__dict__.has_key('ServerState'):
    _M_IceGrid.ServerState = Ice.createTempClass()
    class ServerState(object):

        def __init__(self, val):
            assert(val >= 0 and val < 7)
            self.value = val

        def __str__(self):
            if self.value == 0:
                return 'Inactive'
            elif self.value == 1:
                return 'Activating'
            elif self.value == 2:
                return 'ActivationTimedOut'
            elif self.value == 3:
                return 'Active'
            elif self.value == 4:
                return 'Deactivating'
            elif self.value == 5:
                return 'Destroying'
            elif self.value == 6:
                return 'Destroyed'
            return None

        __repr__ = __str__

        def __hash__(self):
            return self.value

        def __cmp__(self, other):
            return cmp(self.value, other.value)

    ServerState.Inactive = ServerState(0)
    ServerState.Activating = ServerState(1)
    ServerState.ActivationTimedOut = ServerState(2)
    ServerState.Active = ServerState(3)
    ServerState.Deactivating = ServerState(4)
    ServerState.Destroying = ServerState(5)
    ServerState.Destroyed = ServerState(6)

    _M_IceGrid._t_ServerState = IcePy.defineEnum('::IceGrid::ServerState', ServerState, (), (ServerState.Inactive, ServerState.Activating, ServerState.ActivationTimedOut, ServerState.Active, ServerState.Deactivating, ServerState.Destroying, ServerState.Destroyed))

    _M_IceGrid.ServerState = ServerState
    del ServerState

if not _M_IceGrid.__dict__.has_key('_t_StringObjectProxyDict'):
    _M_IceGrid._t_StringObjectProxyDict = IcePy.defineDictionary('::IceGrid::StringObjectProxyDict', (), IcePy._t_string, IcePy._t_ObjectPrx)

if not _M_IceGrid.__dict__.has_key('ObjectInfo'):
    _M_IceGrid.ObjectInfo = Ice.createTempClass()
    class ObjectInfo(object):
        def __init__(self, proxy=None, type=''):
            self.proxy = proxy
            self.type = type

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.proxy)
            _h = 5 * _h + __builtin__.hash(self.type)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.proxy < other.proxy:
                return -1
            elif self.proxy > other.proxy:
                return 1
            if self.type < other.type:
                return -1
            elif self.type > other.type:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ObjectInfo)

        __repr__ = __str__

    _M_IceGrid._t_ObjectInfo = IcePy.defineStruct('::IceGrid::ObjectInfo', ObjectInfo, (), (
        ('proxy', (), IcePy._t_ObjectPrx),
        ('type', (), IcePy._t_string)
    ))

    _M_IceGrid.ObjectInfo = ObjectInfo
    del ObjectInfo

if not _M_IceGrid.__dict__.has_key('_t_ObjectInfoSeq'):
    _M_IceGrid._t_ObjectInfoSeq = IcePy.defineSequence('::IceGrid::ObjectInfoSeq', (), _M_IceGrid._t_ObjectInfo)

if not _M_IceGrid.__dict__.has_key('AdapterInfo'):
    _M_IceGrid.AdapterInfo = Ice.createTempClass()
    class AdapterInfo(object):
        def __init__(self, id='', proxy=None, replicaGroupId=''):
            self.id = id
            self.proxy = proxy
            self.replicaGroupId = replicaGroupId

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.id)
            _h = 5 * _h + __builtin__.hash(self.proxy)
            _h = 5 * _h + __builtin__.hash(self.replicaGroupId)
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
            if self.replicaGroupId < other.replicaGroupId:
                return -1
            elif self.replicaGroupId > other.replicaGroupId:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_AdapterInfo)

        __repr__ = __str__

    _M_IceGrid._t_AdapterInfo = IcePy.defineStruct('::IceGrid::AdapterInfo', AdapterInfo, (), (
        ('id', (), IcePy._t_string),
        ('proxy', (), IcePy._t_ObjectPrx),
        ('replicaGroupId', (), IcePy._t_string)
    ))

    _M_IceGrid.AdapterInfo = AdapterInfo
    del AdapterInfo

if not _M_IceGrid.__dict__.has_key('_t_AdapterInfoSeq'):
    _M_IceGrid._t_AdapterInfoSeq = IcePy.defineSequence('::IceGrid::AdapterInfoSeq', (), _M_IceGrid._t_AdapterInfo)

if not _M_IceGrid.__dict__.has_key('ServerInfo'):
    _M_IceGrid.ServerInfo = Ice.createTempClass()
    class ServerInfo(object):
        def __init__(self, application='', uuid='', revision=0, node='', descriptor=None, sessionId=''):
            self.application = application
            self.uuid = uuid
            self.revision = revision
            self.node = node
            self.descriptor = descriptor
            self.sessionId = sessionId

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.application)
            _h = 5 * _h + __builtin__.hash(self.uuid)
            _h = 5 * _h + __builtin__.hash(self.revision)
            _h = 5 * _h + __builtin__.hash(self.node)
            _h = 5 * _h + __builtin__.hash(self.descriptor)
            _h = 5 * _h + __builtin__.hash(self.sessionId)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.application < other.application:
                return -1
            elif self.application > other.application:
                return 1
            if self.uuid < other.uuid:
                return -1
            elif self.uuid > other.uuid:
                return 1
            if self.revision < other.revision:
                return -1
            elif self.revision > other.revision:
                return 1
            if self.node < other.node:
                return -1
            elif self.node > other.node:
                return 1
            if self.descriptor < other.descriptor:
                return -1
            elif self.descriptor > other.descriptor:
                return 1
            if self.sessionId < other.sessionId:
                return -1
            elif self.sessionId > other.sessionId:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ServerInfo)

        __repr__ = __str__

    _M_IceGrid._t_ServerInfo = IcePy.defineStruct('::IceGrid::ServerInfo', ServerInfo, (), (
        ('application', (), IcePy._t_string),
        ('uuid', (), IcePy._t_string),
        ('revision', (), IcePy._t_int),
        ('node', (), IcePy._t_string),
        ('descriptor', (), _M_IceGrid._t_ServerDescriptor),
        ('sessionId', (), IcePy._t_string)
    ))

    _M_IceGrid.ServerInfo = ServerInfo
    del ServerInfo

if not _M_IceGrid.__dict__.has_key('NodeInfo'):
    _M_IceGrid.NodeInfo = Ice.createTempClass()
    class NodeInfo(object):
        def __init__(self, name='', os='', hostname='', release='', version='', machine='', nProcessors=0, dataDir=''):
            self.name = name
            self.os = os
            self.hostname = hostname
            self.release = release
            self.version = version
            self.machine = machine
            self.nProcessors = nProcessors
            self.dataDir = dataDir

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.name)
            _h = 5 * _h + __builtin__.hash(self.os)
            _h = 5 * _h + __builtin__.hash(self.hostname)
            _h = 5 * _h + __builtin__.hash(self.release)
            _h = 5 * _h + __builtin__.hash(self.version)
            _h = 5 * _h + __builtin__.hash(self.machine)
            _h = 5 * _h + __builtin__.hash(self.nProcessors)
            _h = 5 * _h + __builtin__.hash(self.dataDir)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            if self.os < other.os:
                return -1
            elif self.os > other.os:
                return 1
            if self.hostname < other.hostname:
                return -1
            elif self.hostname > other.hostname:
                return 1
            if self.release < other.release:
                return -1
            elif self.release > other.release:
                return 1
            if self.version < other.version:
                return -1
            elif self.version > other.version:
                return 1
            if self.machine < other.machine:
                return -1
            elif self.machine > other.machine:
                return 1
            if self.nProcessors < other.nProcessors:
                return -1
            elif self.nProcessors > other.nProcessors:
                return 1
            if self.dataDir < other.dataDir:
                return -1
            elif self.dataDir > other.dataDir:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_NodeInfo)

        __repr__ = __str__

    _M_IceGrid._t_NodeInfo = IcePy.defineStruct('::IceGrid::NodeInfo', NodeInfo, (), (
        ('name', (), IcePy._t_string),
        ('os', (), IcePy._t_string),
        ('hostname', (), IcePy._t_string),
        ('release', (), IcePy._t_string),
        ('version', (), IcePy._t_string),
        ('machine', (), IcePy._t_string),
        ('nProcessors', (), IcePy._t_int),
        ('dataDir', (), IcePy._t_string)
    ))

    _M_IceGrid.NodeInfo = NodeInfo
    del NodeInfo

if not _M_IceGrid.__dict__.has_key('RegistryInfo'):
    _M_IceGrid.RegistryInfo = Ice.createTempClass()
    class RegistryInfo(object):
        def __init__(self, name='', hostname=''):
            self.name = name
            self.hostname = hostname

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.name)
            _h = 5 * _h + __builtin__.hash(self.hostname)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            if self.hostname < other.hostname:
                return -1
            elif self.hostname > other.hostname:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_RegistryInfo)

        __repr__ = __str__

    _M_IceGrid._t_RegistryInfo = IcePy.defineStruct('::IceGrid::RegistryInfo', RegistryInfo, (), (
        ('name', (), IcePy._t_string),
        ('hostname', (), IcePy._t_string)
    ))

    _M_IceGrid.RegistryInfo = RegistryInfo
    del RegistryInfo

if not _M_IceGrid.__dict__.has_key('_t_RegistryInfoSeq'):
    _M_IceGrid._t_RegistryInfoSeq = IcePy.defineSequence('::IceGrid::RegistryInfoSeq', (), _M_IceGrid._t_RegistryInfo)

if not _M_IceGrid.__dict__.has_key('LoadInfo'):
    _M_IceGrid.LoadInfo = Ice.createTempClass()
    class LoadInfo(object):
        def __init__(self, avg1=0.0, avg5=0.0, avg15=0.0):
            self.avg1 = avg1
            self.avg5 = avg5
            self.avg15 = avg15

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.avg1)
            _h = 5 * _h + __builtin__.hash(self.avg5)
            _h = 5 * _h + __builtin__.hash(self.avg15)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.avg1 < other.avg1:
                return -1
            elif self.avg1 > other.avg1:
                return 1
            if self.avg5 < other.avg5:
                return -1
            elif self.avg5 > other.avg5:
                return 1
            if self.avg15 < other.avg15:
                return -1
            elif self.avg15 > other.avg15:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_LoadInfo)

        __repr__ = __str__

    _M_IceGrid._t_LoadInfo = IcePy.defineStruct('::IceGrid::LoadInfo', LoadInfo, (), (
        ('avg1', (), IcePy._t_float),
        ('avg5', (), IcePy._t_float),
        ('avg15', (), IcePy._t_float)
    ))

    _M_IceGrid.LoadInfo = LoadInfo
    del LoadInfo

if not _M_IceGrid.__dict__.has_key('ApplicationInfo'):
    _M_IceGrid.ApplicationInfo = Ice.createTempClass()
    class ApplicationInfo(object):
        def __init__(self, uuid='', createTime=0, createUser='', updateTime=0, updateUser='', revision=0, descriptor=Ice._struct_marker):
            self.uuid = uuid
            self.createTime = createTime
            self.createUser = createUser
            self.updateTime = updateTime
            self.updateUser = updateUser
            self.revision = revision
            if descriptor is Ice._struct_marker:
                self.descriptor = _M_IceGrid.ApplicationDescriptor()
            else:
                self.descriptor = descriptor

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.uuid)
            _h = 5 * _h + __builtin__.hash(self.createTime)
            _h = 5 * _h + __builtin__.hash(self.createUser)
            _h = 5 * _h + __builtin__.hash(self.updateTime)
            _h = 5 * _h + __builtin__.hash(self.updateUser)
            _h = 5 * _h + __builtin__.hash(self.revision)
            _h = 5 * _h + __builtin__.hash(self.descriptor)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.uuid < other.uuid:
                return -1
            elif self.uuid > other.uuid:
                return 1
            if self.createTime < other.createTime:
                return -1
            elif self.createTime > other.createTime:
                return 1
            if self.createUser < other.createUser:
                return -1
            elif self.createUser > other.createUser:
                return 1
            if self.updateTime < other.updateTime:
                return -1
            elif self.updateTime > other.updateTime:
                return 1
            if self.updateUser < other.updateUser:
                return -1
            elif self.updateUser > other.updateUser:
                return 1
            if self.revision < other.revision:
                return -1
            elif self.revision > other.revision:
                return 1
            if self.descriptor < other.descriptor:
                return -1
            elif self.descriptor > other.descriptor:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ApplicationInfo)

        __repr__ = __str__

    _M_IceGrid._t_ApplicationInfo = IcePy.defineStruct('::IceGrid::ApplicationInfo', ApplicationInfo, (), (
        ('uuid', (), IcePy._t_string),
        ('createTime', (), IcePy._t_long),
        ('createUser', (), IcePy._t_string),
        ('updateTime', (), IcePy._t_long),
        ('updateUser', (), IcePy._t_string),
        ('revision', (), IcePy._t_int),
        ('descriptor', (), _M_IceGrid._t_ApplicationDescriptor)
    ))

    _M_IceGrid.ApplicationInfo = ApplicationInfo
    del ApplicationInfo

if not _M_IceGrid.__dict__.has_key('_t_ApplicationInfoSeq'):
    _M_IceGrid._t_ApplicationInfoSeq = IcePy.defineSequence('::IceGrid::ApplicationInfoSeq', (), _M_IceGrid._t_ApplicationInfo)

if not _M_IceGrid.__dict__.has_key('ApplicationUpdateInfo'):
    _M_IceGrid.ApplicationUpdateInfo = Ice.createTempClass()
    class ApplicationUpdateInfo(object):
        def __init__(self, updateTime=0, updateUser='', revision=0, descriptor=Ice._struct_marker):
            self.updateTime = updateTime
            self.updateUser = updateUser
            self.revision = revision
            if descriptor is Ice._struct_marker:
                self.descriptor = _M_IceGrid.ApplicationUpdateDescriptor()
            else:
                self.descriptor = descriptor

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.updateTime)
            _h = 5 * _h + __builtin__.hash(self.updateUser)
            _h = 5 * _h + __builtin__.hash(self.revision)
            _h = 5 * _h + __builtin__.hash(self.descriptor)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.updateTime < other.updateTime:
                return -1
            elif self.updateTime > other.updateTime:
                return 1
            if self.updateUser < other.updateUser:
                return -1
            elif self.updateUser > other.updateUser:
                return 1
            if self.revision < other.revision:
                return -1
            elif self.revision > other.revision:
                return 1
            if self.descriptor < other.descriptor:
                return -1
            elif self.descriptor > other.descriptor:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ApplicationUpdateInfo)

        __repr__ = __str__

    _M_IceGrid._t_ApplicationUpdateInfo = IcePy.defineStruct('::IceGrid::ApplicationUpdateInfo', ApplicationUpdateInfo, (), (
        ('updateTime', (), IcePy._t_long),
        ('updateUser', (), IcePy._t_string),
        ('revision', (), IcePy._t_int),
        ('descriptor', (), _M_IceGrid._t_ApplicationUpdateDescriptor)
    ))

    _M_IceGrid.ApplicationUpdateInfo = ApplicationUpdateInfo
    del ApplicationUpdateInfo

if not _M_IceGrid.__dict__.has_key('Admin'):
    _M_IceGrid.Admin = Ice.createTempClass()
    class Admin(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.Admin:
                raise RuntimeError('IceGrid.Admin is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::Admin')

        def ice_id(self, current=None):
            return '::IceGrid::Admin'

        def ice_staticId():
            return '::IceGrid::Admin'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def addApplication(self, descriptor, current=None):
        # def syncApplication(self, descriptor, current=None):
        # def updateApplication(self, descriptor, current=None):
        # def removeApplication(self, name, current=None):
        # def instantiateServer(self, application, node, desc, current=None):
        # def patchApplication_async(self, _cb, name, shutdown, current=None):
        # def getApplicationInfo(self, name, current=None):
        # def getDefaultApplicationDescriptor(self, current=None):
        # def getAllApplicationNames(self, current=None):
        # def getServerInfo(self, id, current=None):
        # def getServerState(self, id, current=None):
        # def getServerPid(self, id, current=None):
        # def getServerAdminCategory(self, current=None):
        # def getServerAdmin(self, id, current=None):
        # def enableServer(self, id, enabled, current=None):
        # def isServerEnabled(self, id, current=None):
        # def startServer_async(self, _cb, id, current=None):
        # def stopServer_async(self, _cb, id, current=None):
        # def patchServer_async(self, _cb, id, shutdown, current=None):
        # def sendSignal(self, id, signal, current=None):
        # def writeMessage(self, id, message, fd, current=None):
        # def getAllServerIds(self, current=None):
        # def getAdapterInfo(self, id, current=None):
        # def removeAdapter(self, adapterId, current=None):
        # def getAllAdapterIds(self, current=None):
        # def addObject(self, obj, current=None):
        # def updateObject(self, obj, current=None):
        # def addObjectWithType(self, obj, type, current=None):
        # def removeObject(self, id, current=None):
        # def getObjectInfo(self, id, current=None):
        # def getObjectInfosByType(self, type, current=None):
        # def getAllObjectInfos(self, expr, current=None):
        # def pingNode(self, name, current=None):
        # def getNodeLoad(self, name, current=None):
        # def getNodeInfo(self, name, current=None):
        # def shutdownNode(self, name, current=None):
        # def getNodeHostname(self, name, current=None):
        # def getAllNodeNames(self, current=None):
        # def pingRegistry(self, name, current=None):
        # def getRegistryInfo(self, name, current=None):
        # def shutdownRegistry(self, name, current=None):
        # def getAllRegistryNames(self, current=None):
        # def shutdown(self, current=None):
        # def getSliceChecksums(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_Admin)

        __repr__ = __str__

    _M_IceGrid.AdminPrx = Ice.createTempClass()
    class AdminPrx(Ice.ObjectPrx):

        def addApplication(self, descriptor, _ctx=None):
            return _M_IceGrid.Admin._op_addApplication.invoke(self, ((descriptor, ), _ctx))

        def addApplication_async(self, _cb, descriptor, _ctx=None):
            return _M_IceGrid.Admin._op_addApplication.invokeAsync(self, (_cb, (descriptor, ), _ctx))

        def syncApplication(self, descriptor, _ctx=None):
            return _M_IceGrid.Admin._op_syncApplication.invoke(self, ((descriptor, ), _ctx))

        def syncApplication_async(self, _cb, descriptor, _ctx=None):
            return _M_IceGrid.Admin._op_syncApplication.invokeAsync(self, (_cb, (descriptor, ), _ctx))

        def updateApplication(self, descriptor, _ctx=None):
            return _M_IceGrid.Admin._op_updateApplication.invoke(self, ((descriptor, ), _ctx))

        def updateApplication_async(self, _cb, descriptor, _ctx=None):
            return _M_IceGrid.Admin._op_updateApplication.invokeAsync(self, (_cb, (descriptor, ), _ctx))

        def removeApplication(self, name, _ctx=None):
            return _M_IceGrid.Admin._op_removeApplication.invoke(self, ((name, ), _ctx))

        def removeApplication_async(self, _cb, name, _ctx=None):
            return _M_IceGrid.Admin._op_removeApplication.invokeAsync(self, (_cb, (name, ), _ctx))

        def instantiateServer(self, application, node, desc, _ctx=None):
            return _M_IceGrid.Admin._op_instantiateServer.invoke(self, ((application, node, desc), _ctx))

        def patchApplication(self, name, shutdown, _ctx=None):
            return _M_IceGrid.Admin._op_patchApplication.invoke(self, ((name, shutdown), _ctx))

        def patchApplication_async(self, _cb, name, shutdown, _ctx=None):
            return _M_IceGrid.Admin._op_patchApplication.invokeAsync(self, (_cb, (name, shutdown), _ctx))

        def getApplicationInfo(self, name, _ctx=None):
            return _M_IceGrid.Admin._op_getApplicationInfo.invoke(self, ((name, ), _ctx))

        def getDefaultApplicationDescriptor(self, _ctx=None):
            return _M_IceGrid.Admin._op_getDefaultApplicationDescriptor.invoke(self, ((), _ctx))

        def getAllApplicationNames(self, _ctx=None):
            return _M_IceGrid.Admin._op_getAllApplicationNames.invoke(self, ((), _ctx))

        def getServerInfo(self, id, _ctx=None):
            return _M_IceGrid.Admin._op_getServerInfo.invoke(self, ((id, ), _ctx))

        def getServerState(self, id, _ctx=None):
            return _M_IceGrid.Admin._op_getServerState.invoke(self, ((id, ), _ctx))

        def getServerPid(self, id, _ctx=None):
            return _M_IceGrid.Admin._op_getServerPid.invoke(self, ((id, ), _ctx))

        def getServerAdminCategory(self, _ctx=None):
            return _M_IceGrid.Admin._op_getServerAdminCategory.invoke(self, ((), _ctx))

        def getServerAdmin(self, id, _ctx=None):
            return _M_IceGrid.Admin._op_getServerAdmin.invoke(self, ((id, ), _ctx))

        def enableServer(self, id, enabled, _ctx=None):
            return _M_IceGrid.Admin._op_enableServer.invoke(self, ((id, enabled), _ctx))

        def enableServer_async(self, _cb, id, enabled, _ctx=None):
            return _M_IceGrid.Admin._op_enableServer.invokeAsync(self, (_cb, (id, enabled), _ctx))

        def isServerEnabled(self, id, _ctx=None):
            return _M_IceGrid.Admin._op_isServerEnabled.invoke(self, ((id, ), _ctx))

        def startServer(self, id, _ctx=None):
            return _M_IceGrid.Admin._op_startServer.invoke(self, ((id, ), _ctx))

        def startServer_async(self, _cb, id, _ctx=None):
            return _M_IceGrid.Admin._op_startServer.invokeAsync(self, (_cb, (id, ), _ctx))

        def stopServer(self, id, _ctx=None):
            return _M_IceGrid.Admin._op_stopServer.invoke(self, ((id, ), _ctx))

        def stopServer_async(self, _cb, id, _ctx=None):
            return _M_IceGrid.Admin._op_stopServer.invokeAsync(self, (_cb, (id, ), _ctx))

        def patchServer(self, id, shutdown, _ctx=None):
            return _M_IceGrid.Admin._op_patchServer.invoke(self, ((id, shutdown), _ctx))

        def patchServer_async(self, _cb, id, shutdown, _ctx=None):
            return _M_IceGrid.Admin._op_patchServer.invokeAsync(self, (_cb, (id, shutdown), _ctx))

        def sendSignal(self, id, signal, _ctx=None):
            return _M_IceGrid.Admin._op_sendSignal.invoke(self, ((id, signal), _ctx))

        def sendSignal_async(self, _cb, id, signal, _ctx=None):
            return _M_IceGrid.Admin._op_sendSignal.invokeAsync(self, (_cb, (id, signal), _ctx))

        def writeMessage(self, id, message, fd, _ctx=None):
            return _M_IceGrid.Admin._op_writeMessage.invoke(self, ((id, message, fd), _ctx))

        def writeMessage_async(self, _cb, id, message, fd, _ctx=None):
            return _M_IceGrid.Admin._op_writeMessage.invokeAsync(self, (_cb, (id, message, fd), _ctx))

        def getAllServerIds(self, _ctx=None):
            return _M_IceGrid.Admin._op_getAllServerIds.invoke(self, ((), _ctx))

        def getAdapterInfo(self, id, _ctx=None):
            return _M_IceGrid.Admin._op_getAdapterInfo.invoke(self, ((id, ), _ctx))

        def removeAdapter(self, adapterId, _ctx=None):
            return _M_IceGrid.Admin._op_removeAdapter.invoke(self, ((adapterId, ), _ctx))

        def removeAdapter_async(self, _cb, adapterId, _ctx=None):
            return _M_IceGrid.Admin._op_removeAdapter.invokeAsync(self, (_cb, (adapterId, ), _ctx))

        def getAllAdapterIds(self, _ctx=None):
            return _M_IceGrid.Admin._op_getAllAdapterIds.invoke(self, ((), _ctx))

        def addObject(self, obj, _ctx=None):
            return _M_IceGrid.Admin._op_addObject.invoke(self, ((obj, ), _ctx))

        def addObject_async(self, _cb, obj, _ctx=None):
            return _M_IceGrid.Admin._op_addObject.invokeAsync(self, (_cb, (obj, ), _ctx))

        def updateObject(self, obj, _ctx=None):
            return _M_IceGrid.Admin._op_updateObject.invoke(self, ((obj, ), _ctx))

        def addObjectWithType(self, obj, type, _ctx=None):
            return _M_IceGrid.Admin._op_addObjectWithType.invoke(self, ((obj, type), _ctx))

        def addObjectWithType_async(self, _cb, obj, type, _ctx=None):
            return _M_IceGrid.Admin._op_addObjectWithType.invokeAsync(self, (_cb, (obj, type), _ctx))

        def removeObject(self, id, _ctx=None):
            return _M_IceGrid.Admin._op_removeObject.invoke(self, ((id, ), _ctx))

        def removeObject_async(self, _cb, id, _ctx=None):
            return _M_IceGrid.Admin._op_removeObject.invokeAsync(self, (_cb, (id, ), _ctx))

        def getObjectInfo(self, id, _ctx=None):
            return _M_IceGrid.Admin._op_getObjectInfo.invoke(self, ((id, ), _ctx))

        def getObjectInfosByType(self, type, _ctx=None):
            return _M_IceGrid.Admin._op_getObjectInfosByType.invoke(self, ((type, ), _ctx))

        def getAllObjectInfos(self, expr, _ctx=None):
            return _M_IceGrid.Admin._op_getAllObjectInfos.invoke(self, ((expr, ), _ctx))

        def pingNode(self, name, _ctx=None):
            return _M_IceGrid.Admin._op_pingNode.invoke(self, ((name, ), _ctx))

        def getNodeLoad(self, name, _ctx=None):
            return _M_IceGrid.Admin._op_getNodeLoad.invoke(self, ((name, ), _ctx))

        def getNodeLoad_async(self, _cb, name, _ctx=None):
            return _M_IceGrid.Admin._op_getNodeLoad.invokeAsync(self, (_cb, (name, ), _ctx))

        def getNodeInfo(self, name, _ctx=None):
            return _M_IceGrid.Admin._op_getNodeInfo.invoke(self, ((name, ), _ctx))

        def shutdownNode(self, name, _ctx=None):
            return _M_IceGrid.Admin._op_shutdownNode.invoke(self, ((name, ), _ctx))

        def shutdownNode_async(self, _cb, name, _ctx=None):
            return _M_IceGrid.Admin._op_shutdownNode.invokeAsync(self, (_cb, (name, ), _ctx))

        def getNodeHostname(self, name, _ctx=None):
            return _M_IceGrid.Admin._op_getNodeHostname.invoke(self, ((name, ), _ctx))

        def getAllNodeNames(self, _ctx=None):
            return _M_IceGrid.Admin._op_getAllNodeNames.invoke(self, ((), _ctx))

        def pingRegistry(self, name, _ctx=None):
            return _M_IceGrid.Admin._op_pingRegistry.invoke(self, ((name, ), _ctx))

        def getRegistryInfo(self, name, _ctx=None):
            return _M_IceGrid.Admin._op_getRegistryInfo.invoke(self, ((name, ), _ctx))

        def shutdownRegistry(self, name, _ctx=None):
            return _M_IceGrid.Admin._op_shutdownRegistry.invoke(self, ((name, ), _ctx))

        def shutdownRegistry_async(self, _cb, name, _ctx=None):
            return _M_IceGrid.Admin._op_shutdownRegistry.invokeAsync(self, (_cb, (name, ), _ctx))

        def getAllRegistryNames(self, _ctx=None):
            return _M_IceGrid.Admin._op_getAllRegistryNames.invoke(self, ((), _ctx))

        def shutdown(self, _ctx=None):
            return _M_IceGrid.Admin._op_shutdown.invoke(self, ((), _ctx))

        def getSliceChecksums(self, _ctx=None):
            return _M_IceGrid.Admin._op_getSliceChecksums.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.AdminPrx.ice_checkedCast(proxy, '::IceGrid::Admin', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.AdminPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_AdminPrx = IcePy.defineProxy('::IceGrid::Admin', AdminPrx)

    _M_IceGrid._t_Admin = IcePy.defineClass('::IceGrid::Admin', Admin, (), True, None, (), ())
    Admin.ice_type = _M_IceGrid._t_Admin

    Admin._op_addApplication = IcePy.Operation('addApplication', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_ApplicationDescriptor),), (), None, (_M_IceGrid._t_AccessDeniedException, _M_IceGrid._t_DeploymentException))
    Admin._op_syncApplication = IcePy.Operation('syncApplication', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_ApplicationDescriptor),), (), None, (_M_IceGrid._t_AccessDeniedException, _M_IceGrid._t_DeploymentException, _M_IceGrid._t_ApplicationNotExistException))
    Admin._op_updateApplication = IcePy.Operation('updateApplication', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceGrid._t_ApplicationUpdateDescriptor),), (), None, (_M_IceGrid._t_AccessDeniedException, _M_IceGrid._t_DeploymentException, _M_IceGrid._t_ApplicationNotExistException))
    Admin._op_removeApplication = IcePy.Operation('removeApplication', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, (_M_IceGrid._t_AccessDeniedException, _M_IceGrid._t_DeploymentException, _M_IceGrid._t_ApplicationNotExistException))
    Admin._op_instantiateServer = IcePy.Operation('instantiateServer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string), ((), _M_IceGrid._t_ServerInstanceDescriptor)), (), None, (_M_IceGrid._t_AccessDeniedException, _M_IceGrid._t_ApplicationNotExistException, _M_IceGrid._t_DeploymentException))
    Admin._op_patchApplication = IcePy.Operation('patchApplication', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), IcePy._t_string), ((), IcePy._t_bool)), (), None, (_M_IceGrid._t_ApplicationNotExistException, _M_IceGrid._t_PatchException))
    Admin._op_getApplicationInfo = IcePy.Operation('getApplicationInfo', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), _M_IceGrid._t_ApplicationInfo, (_M_IceGrid._t_ApplicationNotExistException,))
    Admin._op_getDefaultApplicationDescriptor = IcePy.Operation('getDefaultApplicationDescriptor', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_IceGrid._t_ApplicationDescriptor, (_M_IceGrid._t_DeploymentException,))
    Admin._op_getAllApplicationNames = IcePy.Operation('getAllApplicationNames', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_StringSeq, ())
    Admin._op_getServerInfo = IcePy.Operation('getServerInfo', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), _M_IceGrid._t_ServerInfo, (_M_IceGrid._t_ServerNotExistException,))
    Admin._op_getServerState = IcePy.Operation('getServerState', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), _M_IceGrid._t_ServerState, (_M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    Admin._op_getServerPid = IcePy.Operation('getServerPid', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), IcePy._t_int, (_M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    Admin._op_getServerAdminCategory = IcePy.Operation('getServerAdminCategory', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), IcePy._t_string, ())
    Admin._op_getServerAdmin = IcePy.Operation('getServerAdmin', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_string),), (), IcePy._t_ObjectPrx, (_M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    Admin._op_enableServer = IcePy.Operation('enableServer', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_string), ((), IcePy._t_bool)), (), None, (_M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    Admin._op_isServerEnabled = IcePy.Operation('isServerEnabled', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), IcePy._t_bool, (_M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    Admin._op_startServer = IcePy.Operation('startServer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), IcePy._t_string),), (), None, (_M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_ServerStartException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    Admin._op_stopServer = IcePy.Operation('stopServer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), IcePy._t_string),), (), None, (_M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_ServerStopException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    Admin._op_patchServer = IcePy.Operation('patchServer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), IcePy._t_string), ((), IcePy._t_bool)), (), None, (_M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException, _M_IceGrid._t_PatchException))
    Admin._op_sendSignal = IcePy.Operation('sendSignal', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), None, (_M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException, _M_IceGrid._t_BadSignalException))
    Admin._op_writeMessage = IcePy.Operation('writeMessage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string), ((), IcePy._t_int)), (), None, (_M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    Admin._op_writeMessage.deprecate("writeMessage is deprecated, use instead the Process facet of the server Admin object.")
    Admin._op_getAllServerIds = IcePy.Operation('getAllServerIds', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_StringSeq, ())
    Admin._op_getAdapterInfo = IcePy.Operation('getAdapterInfo', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), _M_IceGrid._t_AdapterInfoSeq, (_M_IceGrid._t_AdapterNotExistException,))
    Admin._op_removeAdapter = IcePy.Operation('removeAdapter', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, (_M_IceGrid._t_AdapterNotExistException, _M_IceGrid._t_DeploymentException))
    Admin._op_getAllAdapterIds = IcePy.Operation('getAllAdapterIds', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_StringSeq, ())
    Admin._op_addObject = IcePy.Operation('addObject', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_ObjectPrx),), (), None, (_M_IceGrid._t_ObjectExistsException, _M_IceGrid._t_DeploymentException))
    Admin._op_updateObject = IcePy.Operation('updateObject', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_ObjectPrx),), (), None, (_M_IceGrid._t_ObjectNotRegisteredException, _M_IceGrid._t_DeploymentException))
    Admin._op_addObjectWithType = IcePy.Operation('addObjectWithType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_ObjectPrx), ((), IcePy._t_string)), (), None, (_M_IceGrid._t_ObjectExistsException, _M_IceGrid._t_DeploymentException))
    Admin._op_removeObject = IcePy.Operation('removeObject', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_Ice._t_Identity),), (), None, (_M_IceGrid._t_ObjectNotRegisteredException, _M_IceGrid._t_DeploymentException))
    Admin._op_getObjectInfo = IcePy.Operation('getObjectInfo', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), _M_Ice._t_Identity),), (), _M_IceGrid._t_ObjectInfo, (_M_IceGrid._t_ObjectNotRegisteredException,))
    Admin._op_getObjectInfosByType = IcePy.Operation('getObjectInfosByType', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), _M_IceGrid._t_ObjectInfoSeq, ())
    Admin._op_getAllObjectInfos = IcePy.Operation('getAllObjectInfos', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), _M_IceGrid._t_ObjectInfoSeq, ())
    Admin._op_pingNode = IcePy.Operation('pingNode', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), IcePy._t_bool, (_M_IceGrid._t_NodeNotExistException,))
    Admin._op_getNodeLoad = IcePy.Operation('getNodeLoad', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), _M_IceGrid._t_LoadInfo, (_M_IceGrid._t_NodeNotExistException, _M_IceGrid._t_NodeUnreachableException))
    Admin._op_getNodeInfo = IcePy.Operation('getNodeInfo', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), _M_IceGrid._t_NodeInfo, (_M_IceGrid._t_NodeNotExistException, _M_IceGrid._t_NodeUnreachableException))
    Admin._op_shutdownNode = IcePy.Operation('shutdownNode', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, (_M_IceGrid._t_NodeNotExistException, _M_IceGrid._t_NodeUnreachableException))
    Admin._op_getNodeHostname = IcePy.Operation('getNodeHostname', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), IcePy._t_string, (_M_IceGrid._t_NodeNotExistException, _M_IceGrid._t_NodeUnreachableException))
    Admin._op_getAllNodeNames = IcePy.Operation('getAllNodeNames', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_StringSeq, ())
    Admin._op_pingRegistry = IcePy.Operation('pingRegistry', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_string),), (), IcePy._t_bool, (_M_IceGrid._t_RegistryNotExistException,))
    Admin._op_getRegistryInfo = IcePy.Operation('getRegistryInfo', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_string),), (), _M_IceGrid._t_RegistryInfo, (_M_IceGrid._t_RegistryNotExistException, _M_IceGrid._t_RegistryUnreachableException))
    Admin._op_shutdownRegistry = IcePy.Operation('shutdownRegistry', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_string),), (), None, (_M_IceGrid._t_RegistryNotExistException, _M_IceGrid._t_RegistryUnreachableException))
    Admin._op_getAllRegistryNames = IcePy.Operation('getAllRegistryNames', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), _M_Ice._t_StringSeq, ())
    Admin._op_shutdown = IcePy.Operation('shutdown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())
    Admin._op_getSliceChecksums = IcePy.Operation('getSliceChecksums', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_SliceChecksumDict, ())

    _M_IceGrid.Admin = Admin
    del Admin

    _M_IceGrid.AdminPrx = AdminPrx
    del AdminPrx

if not _M_IceGrid.__dict__.has_key('FileIterator'):
    _M_IceGrid.FileIterator = Ice.createTempClass()
    class FileIterator(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.FileIterator:
                raise RuntimeError('IceGrid.FileIterator is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::FileIterator')

        def ice_id(self, current=None):
            return '::IceGrid::FileIterator'

        def ice_staticId():
            return '::IceGrid::FileIterator'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def read(self, size, current=None):
        # def destroy(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_FileIterator)

        __repr__ = __str__

    _M_IceGrid.FileIteratorPrx = Ice.createTempClass()
    class FileIteratorPrx(Ice.ObjectPrx):

        def read(self, size, _ctx=None):
            return _M_IceGrid.FileIterator._op_read.invoke(self, ((size, ), _ctx))

        def destroy(self, _ctx=None):
            return _M_IceGrid.FileIterator._op_destroy.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.FileIteratorPrx.ice_checkedCast(proxy, '::IceGrid::FileIterator', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.FileIteratorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_FileIteratorPrx = IcePy.defineProxy('::IceGrid::FileIterator', FileIteratorPrx)

    _M_IceGrid._t_FileIterator = IcePy.defineClass('::IceGrid::FileIterator', FileIterator, (), True, None, (), ())
    FileIterator.ice_type = _M_IceGrid._t_FileIterator

    FileIterator._op_read = IcePy.Operation('read', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_int),), (((), _M_Ice._t_StringSeq),), IcePy._t_bool, (_M_IceGrid._t_FileNotAvailableException,))
    FileIterator._op_destroy = IcePy.Operation('destroy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())

    _M_IceGrid.FileIterator = FileIterator
    del FileIterator

    _M_IceGrid.FileIteratorPrx = FileIteratorPrx
    del FileIteratorPrx

if not _M_IceGrid.__dict__.has_key('RegistryObserver'):
    _M_IceGrid._t_RegistryObserver = IcePy.declareClass('::IceGrid::RegistryObserver')
    _M_IceGrid._t_RegistryObserverPrx = IcePy.declareProxy('::IceGrid::RegistryObserver')

if not _M_IceGrid.__dict__.has_key('NodeObserver'):
    _M_IceGrid._t_NodeObserver = IcePy.declareClass('::IceGrid::NodeObserver')
    _M_IceGrid._t_NodeObserverPrx = IcePy.declareProxy('::IceGrid::NodeObserver')

if not _M_IceGrid.__dict__.has_key('ApplicationObserver'):
    _M_IceGrid._t_ApplicationObserver = IcePy.declareClass('::IceGrid::ApplicationObserver')
    _M_IceGrid._t_ApplicationObserverPrx = IcePy.declareProxy('::IceGrid::ApplicationObserver')

if not _M_IceGrid.__dict__.has_key('AdapterObserver'):
    _M_IceGrid._t_AdapterObserver = IcePy.declareClass('::IceGrid::AdapterObserver')
    _M_IceGrid._t_AdapterObserverPrx = IcePy.declareProxy('::IceGrid::AdapterObserver')

if not _M_IceGrid.__dict__.has_key('ObjectObserver'):
    _M_IceGrid._t_ObjectObserver = IcePy.declareClass('::IceGrid::ObjectObserver')
    _M_IceGrid._t_ObjectObserverPrx = IcePy.declareProxy('::IceGrid::ObjectObserver')

if not _M_IceGrid.__dict__.has_key('AdminSession'):
    _M_IceGrid.AdminSession = Ice.createTempClass()
    class AdminSession(_M_Glacier2.Session):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.AdminSession:
                raise RuntimeError('IceGrid.AdminSession is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::Session', '::Ice::Object', '::IceGrid::AdminSession')

        def ice_id(self, current=None):
            return '::IceGrid::AdminSession'

        def ice_staticId():
            return '::IceGrid::AdminSession'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def keepAlive(self, current=None):
        # def getAdmin(self, current=None):
        # def getAdminCallbackTemplate(self, current=None):
        # def setObservers(self, registryObs, nodeObs, appObs, adptObs, objObs, current=None):
        # def setObserversByIdentity(self, registryObs, nodeObs, appObs, adptObs, objObs, current=None):
        # def startUpdate(self, current=None):
        # def finishUpdate(self, current=None):
        # def getReplicaName(self, current=None):
        # def openServerLog(self, id, path, count, current=None):
        # def openServerStdErr(self, id, count, current=None):
        # def openServerStdOut(self, id, count, current=None):
        # def openNodeStdErr(self, name, count, current=None):
        # def openNodeStdOut(self, name, count, current=None):
        # def openRegistryStdErr(self, name, count, current=None):
        # def openRegistryStdOut(self, name, count, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_AdminSession)

        __repr__ = __str__

    _M_IceGrid.AdminSessionPrx = Ice.createTempClass()
    class AdminSessionPrx(_M_Glacier2.SessionPrx):

        def keepAlive(self, _ctx=None):
            return _M_IceGrid.AdminSession._op_keepAlive.invoke(self, ((), _ctx))

        def getAdmin(self, _ctx=None):
            return _M_IceGrid.AdminSession._op_getAdmin.invoke(self, ((), _ctx))

        def getAdminCallbackTemplate(self, _ctx=None):
            return _M_IceGrid.AdminSession._op_getAdminCallbackTemplate.invoke(self, ((), _ctx))

        def setObservers(self, registryObs, nodeObs, appObs, adptObs, objObs, _ctx=None):
            return _M_IceGrid.AdminSession._op_setObservers.invoke(self, ((registryObs, nodeObs, appObs, adptObs, objObs), _ctx))

        def setObserversByIdentity(self, registryObs, nodeObs, appObs, adptObs, objObs, _ctx=None):
            return _M_IceGrid.AdminSession._op_setObserversByIdentity.invoke(self, ((registryObs, nodeObs, appObs, adptObs, objObs), _ctx))

        def startUpdate(self, _ctx=None):
            return _M_IceGrid.AdminSession._op_startUpdate.invoke(self, ((), _ctx))

        def finishUpdate(self, _ctx=None):
            return _M_IceGrid.AdminSession._op_finishUpdate.invoke(self, ((), _ctx))

        def getReplicaName(self, _ctx=None):
            return _M_IceGrid.AdminSession._op_getReplicaName.invoke(self, ((), _ctx))

        def openServerLog(self, id, path, count, _ctx=None):
            return _M_IceGrid.AdminSession._op_openServerLog.invoke(self, ((id, path, count), _ctx))

        def openServerStdErr(self, id, count, _ctx=None):
            return _M_IceGrid.AdminSession._op_openServerStdErr.invoke(self, ((id, count), _ctx))

        def openServerStdOut(self, id, count, _ctx=None):
            return _M_IceGrid.AdminSession._op_openServerStdOut.invoke(self, ((id, count), _ctx))

        def openNodeStdErr(self, name, count, _ctx=None):
            return _M_IceGrid.AdminSession._op_openNodeStdErr.invoke(self, ((name, count), _ctx))

        def openNodeStdOut(self, name, count, _ctx=None):
            return _M_IceGrid.AdminSession._op_openNodeStdOut.invoke(self, ((name, count), _ctx))

        def openRegistryStdErr(self, name, count, _ctx=None):
            return _M_IceGrid.AdminSession._op_openRegistryStdErr.invoke(self, ((name, count), _ctx))

        def openRegistryStdOut(self, name, count, _ctx=None):
            return _M_IceGrid.AdminSession._op_openRegistryStdOut.invoke(self, ((name, count), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.AdminSessionPrx.ice_checkedCast(proxy, '::IceGrid::AdminSession', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.AdminSessionPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_AdminSessionPrx = IcePy.defineProxy('::IceGrid::AdminSession', AdminSessionPrx)

    _M_IceGrid._t_AdminSession = IcePy.defineClass('::IceGrid::AdminSession', AdminSession, (), True, None, (_M_Glacier2._t_Session,), ())
    AdminSession.ice_type = _M_IceGrid._t_AdminSession

    AdminSession._op_keepAlive = IcePy.Operation('keepAlive', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), None, ())
    AdminSession._op_getAdmin = IcePy.Operation('getAdmin', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_IceGrid._t_AdminPrx, ())
    AdminSession._op_getAdminCallbackTemplate = IcePy.Operation('getAdminCallbackTemplate', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), IcePy._t_ObjectPrx, ())
    AdminSession._op_setObservers = IcePy.Operation('setObservers', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), _M_IceGrid._t_RegistryObserverPrx), ((), _M_IceGrid._t_NodeObserverPrx), ((), _M_IceGrid._t_ApplicationObserverPrx), ((), _M_IceGrid._t_AdapterObserverPrx), ((), _M_IceGrid._t_ObjectObserverPrx)), (), None, (_M_IceGrid._t_ObserverAlreadyRegisteredException,))
    AdminSession._op_setObserversByIdentity = IcePy.Operation('setObserversByIdentity', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), _M_Ice._t_Identity), ((), _M_Ice._t_Identity), ((), _M_Ice._t_Identity), ((), _M_Ice._t_Identity), ((), _M_Ice._t_Identity)), (), None, (_M_IceGrid._t_ObserverAlreadyRegisteredException,))
    AdminSession._op_startUpdate = IcePy.Operation('startUpdate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), IcePy._t_int, (_M_IceGrid._t_AccessDeniedException,))
    AdminSession._op_finishUpdate = IcePy.Operation('finishUpdate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, (_M_IceGrid._t_AccessDeniedException,))
    AdminSession._op_getReplicaName = IcePy.Operation('getReplicaName', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), IcePy._t_string, ())
    AdminSession._op_openServerLog = IcePy.Operation('openServerLog', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string), ((), IcePy._t_int)), (), _M_IceGrid._t_FileIteratorPrx, (_M_IceGrid._t_FileNotAvailableException, _M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    AdminSession._op_openServerStdErr = IcePy.Operation('openServerStdErr', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_int)), (), _M_IceGrid._t_FileIteratorPrx, (_M_IceGrid._t_FileNotAvailableException, _M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    AdminSession._op_openServerStdOut = IcePy.Operation('openServerStdOut', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_int)), (), _M_IceGrid._t_FileIteratorPrx, (_M_IceGrid._t_FileNotAvailableException, _M_IceGrid._t_ServerNotExistException, _M_IceGrid._t_NodeUnreachableException, _M_IceGrid._t_DeploymentException))
    AdminSession._op_openNodeStdErr = IcePy.Operation('openNodeStdErr', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_int)), (), _M_IceGrid._t_FileIteratorPrx, (_M_IceGrid._t_FileNotAvailableException, _M_IceGrid._t_NodeNotExistException, _M_IceGrid._t_NodeUnreachableException))
    AdminSession._op_openNodeStdOut = IcePy.Operation('openNodeStdOut', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_int)), (), _M_IceGrid._t_FileIteratorPrx, (_M_IceGrid._t_FileNotAvailableException, _M_IceGrid._t_NodeNotExistException, _M_IceGrid._t_NodeUnreachableException))
    AdminSession._op_openRegistryStdErr = IcePy.Operation('openRegistryStdErr', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_int)), (), _M_IceGrid._t_FileIteratorPrx, (_M_IceGrid._t_FileNotAvailableException, _M_IceGrid._t_RegistryNotExistException, _M_IceGrid._t_RegistryUnreachableException))
    AdminSession._op_openRegistryStdOut = IcePy.Operation('openRegistryStdOut', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_int)), (), _M_IceGrid._t_FileIteratorPrx, (_M_IceGrid._t_FileNotAvailableException, _M_IceGrid._t_RegistryNotExistException, _M_IceGrid._t_RegistryUnreachableException))

    _M_IceGrid.AdminSession = AdminSession
    del AdminSession

    _M_IceGrid.AdminSessionPrx = AdminSessionPrx
    del AdminSessionPrx

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::AdapterInfo"] = "a22de437e0d82d91cca7d476992b2a43"
Ice.sliceChecksums["::IceGrid::AdapterInfoSeq"] = "9fdbbb3c2d938b4e5f3bf5a21f234147"
Ice.sliceChecksums["::IceGrid::Admin"] = "66889fc8dedc10569f69bc8abc3fd385"
Ice.sliceChecksums["::IceGrid::AdminSession"] = "ca6f21e8ff4210158f382cdbc66c2566"
Ice.sliceChecksums["::IceGrid::ApplicationInfo"] = "44ab5928481a1441216f93965f9e6c5"
Ice.sliceChecksums["::IceGrid::ApplicationInfoSeq"] = "dc7429d6b923c3e66eea573eccc1598"
Ice.sliceChecksums["::IceGrid::ApplicationUpdateInfo"] = "c21c8cfe85e332fd9ad194e611bc6b7f"
Ice.sliceChecksums["::IceGrid::FileIterator"] = "54341a38932f89d199f28ffc4712c7"
Ice.sliceChecksums["::IceGrid::LoadInfo"] = "c28c339f5af52a46ac64c33864ae6"
Ice.sliceChecksums["::IceGrid::NodeInfo"] = "f348b389deb653ac28b2b991e23d63b9"
Ice.sliceChecksums["::IceGrid::ObjectInfo"] = "6c8a382c348df5cbda50e58d87189e33"
Ice.sliceChecksums["::IceGrid::ObjectInfoSeq"] = "1491c01cb93b575c602baed26ed0f989"
Ice.sliceChecksums["::IceGrid::RegistryInfo"] = "60e64fc1e37ce59ecbeed4a0e276ba"
Ice.sliceChecksums["::IceGrid::RegistryInfoSeq"] = "fabb868b9f2164f68bc9eb68240c8a6"
Ice.sliceChecksums["::IceGrid::ServerInfo"] = "7f99dc872345b2c3c741c8b4c23440da"
Ice.sliceChecksums["::IceGrid::ServerState"] = "21e8ecba86a4678f3b783de286583093"
Ice.sliceChecksums["::IceGrid::StringObjectProxyDict"] = "978c325e58cebefb212e5ebde28acdc"
