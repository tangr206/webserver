# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Descriptor.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_Identity_ice
import Ice_BuiltinSequences_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')
__name__ = 'IceGrid'

if not _M_IceGrid.__dict__.has_key('_t_StringStringDict'):
    _M_IceGrid._t_StringStringDict = IcePy.defineDictionary('::IceGrid::StringStringDict', (), IcePy._t_string, IcePy._t_string)

if not _M_IceGrid.__dict__.has_key('PropertyDescriptor'):
    _M_IceGrid.PropertyDescriptor = Ice.createTempClass()
    class PropertyDescriptor(object):
        def __init__(self, name='', value=''):
            self.name = name
            self.value = value

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.name)
            _h = 5 * _h + __builtin__.hash(self.value)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            if self.value < other.value:
                return -1
            elif self.value > other.value:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_PropertyDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_PropertyDescriptor = IcePy.defineStruct('::IceGrid::PropertyDescriptor', PropertyDescriptor, (), (
        ('name', (), IcePy._t_string),
        ('value', (), IcePy._t_string)
    ))

    _M_IceGrid.PropertyDescriptor = PropertyDescriptor
    del PropertyDescriptor

if not _M_IceGrid.__dict__.has_key('_t_PropertyDescriptorSeq'):
    _M_IceGrid._t_PropertyDescriptorSeq = IcePy.defineSequence('::IceGrid::PropertyDescriptorSeq', (), _M_IceGrid._t_PropertyDescriptor)

if not _M_IceGrid.__dict__.has_key('PropertySetDescriptor'):
    _M_IceGrid.PropertySetDescriptor = Ice.createTempClass()
    class PropertySetDescriptor(object):
        def __init__(self, references=None, properties=None):
            self.references = references
            self.properties = properties

        def __hash__(self):
            _h = 0
            if self.references:
                for _i0 in self.references:
                    _h = 5 * _h + __builtin__.hash(_i0)
            if self.properties:
                for _i1 in self.properties:
                    _h = 5 * _h + __builtin__.hash(_i1)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.references < other.references:
                return -1
            elif self.references > other.references:
                return 1
            if self.properties < other.properties:
                return -1
            elif self.properties > other.properties:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_PropertySetDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_PropertySetDescriptor = IcePy.defineStruct('::IceGrid::PropertySetDescriptor', PropertySetDescriptor, (), (
        ('references', (), _M_Ice._t_StringSeq),
        ('properties', (), _M_IceGrid._t_PropertyDescriptorSeq)
    ))

    _M_IceGrid.PropertySetDescriptor = PropertySetDescriptor
    del PropertySetDescriptor

if not _M_IceGrid.__dict__.has_key('_t_PropertySetDescriptorDict'):
    _M_IceGrid._t_PropertySetDescriptorDict = IcePy.defineDictionary('::IceGrid::PropertySetDescriptorDict', (), IcePy._t_string, _M_IceGrid._t_PropertySetDescriptor)

if not _M_IceGrid.__dict__.has_key('ObjectDescriptor'):
    _M_IceGrid.ObjectDescriptor = Ice.createTempClass()
    class ObjectDescriptor(object):
        def __init__(self, id=Ice._struct_marker, type=''):
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id
            self.type = type

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.id)
            _h = 5 * _h + __builtin__.hash(self.type)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.id < other.id:
                return -1
            elif self.id > other.id:
                return 1
            if self.type < other.type:
                return -1
            elif self.type > other.type:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ObjectDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_ObjectDescriptor = IcePy.defineStruct('::IceGrid::ObjectDescriptor', ObjectDescriptor, (), (
        ('id', (), _M_Ice._t_Identity),
        ('type', (), IcePy._t_string)
    ))

    _M_IceGrid.ObjectDescriptor = ObjectDescriptor
    del ObjectDescriptor

if not _M_IceGrid.__dict__.has_key('_t_ObjectDescriptorSeq'):
    _M_IceGrid._t_ObjectDescriptorSeq = IcePy.defineSequence('::IceGrid::ObjectDescriptorSeq', (), _M_IceGrid._t_ObjectDescriptor)

if not _M_IceGrid.__dict__.has_key('AdapterDescriptor'):
    _M_IceGrid.AdapterDescriptor = Ice.createTempClass()
    class AdapterDescriptor(object):
        def __init__(self, name='', description='', id='', replicaGroupId='', priority='', registerProcess=False, serverLifetime=False, objects=None, allocatables=None):
            self.name = name
            self.description = description
            self.id = id
            self.replicaGroupId = replicaGroupId
            self.priority = priority
            self.registerProcess = registerProcess
            self.serverLifetime = serverLifetime
            self.objects = objects
            self.allocatables = allocatables

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.name)
            _h = 5 * _h + __builtin__.hash(self.description)
            _h = 5 * _h + __builtin__.hash(self.id)
            _h = 5 * _h + __builtin__.hash(self.replicaGroupId)
            _h = 5 * _h + __builtin__.hash(self.priority)
            _h = 5 * _h + __builtin__.hash(self.registerProcess)
            _h = 5 * _h + __builtin__.hash(self.serverLifetime)
            if self.objects:
                for _i0 in self.objects:
                    _h = 5 * _h + __builtin__.hash(_i0)
            if self.allocatables:
                for _i1 in self.allocatables:
                    _h = 5 * _h + __builtin__.hash(_i1)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            if self.description < other.description:
                return -1
            elif self.description > other.description:
                return 1
            if self.id < other.id:
                return -1
            elif self.id > other.id:
                return 1
            if self.replicaGroupId < other.replicaGroupId:
                return -1
            elif self.replicaGroupId > other.replicaGroupId:
                return 1
            if self.priority < other.priority:
                return -1
            elif self.priority > other.priority:
                return 1
            if self.registerProcess < other.registerProcess:
                return -1
            elif self.registerProcess > other.registerProcess:
                return 1
            if self.serverLifetime < other.serverLifetime:
                return -1
            elif self.serverLifetime > other.serverLifetime:
                return 1
            if self.objects < other.objects:
                return -1
            elif self.objects > other.objects:
                return 1
            if self.allocatables < other.allocatables:
                return -1
            elif self.allocatables > other.allocatables:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_AdapterDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_AdapterDescriptor = IcePy.defineStruct('::IceGrid::AdapterDescriptor', AdapterDescriptor, (), (
        ('name', (), IcePy._t_string),
        ('description', (), IcePy._t_string),
        ('id', (), IcePy._t_string),
        ('replicaGroupId', (), IcePy._t_string),
        ('priority', (), IcePy._t_string),
        ('registerProcess', (), IcePy._t_bool),
        ('serverLifetime', (), IcePy._t_bool),
        ('objects', (), _M_IceGrid._t_ObjectDescriptorSeq),
        ('allocatables', (), _M_IceGrid._t_ObjectDescriptorSeq)
    ))

    _M_IceGrid.AdapterDescriptor = AdapterDescriptor
    del AdapterDescriptor

if not _M_IceGrid.__dict__.has_key('_t_AdapterDescriptorSeq'):
    _M_IceGrid._t_AdapterDescriptorSeq = IcePy.defineSequence('::IceGrid::AdapterDescriptorSeq', (), _M_IceGrid._t_AdapterDescriptor)

if not _M_IceGrid.__dict__.has_key('DbEnvDescriptor'):
    _M_IceGrid.DbEnvDescriptor = Ice.createTempClass()
    class DbEnvDescriptor(object):
        def __init__(self, name='', description='', dbHome='', properties=None):
            self.name = name
            self.description = description
            self.dbHome = dbHome
            self.properties = properties

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.name)
            _h = 5 * _h + __builtin__.hash(self.description)
            _h = 5 * _h + __builtin__.hash(self.dbHome)
            if self.properties:
                for _i0 in self.properties:
                    _h = 5 * _h + __builtin__.hash(_i0)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            if self.description < other.description:
                return -1
            elif self.description > other.description:
                return 1
            if self.dbHome < other.dbHome:
                return -1
            elif self.dbHome > other.dbHome:
                return 1
            if self.properties < other.properties:
                return -1
            elif self.properties > other.properties:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_DbEnvDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_DbEnvDescriptor = IcePy.defineStruct('::IceGrid::DbEnvDescriptor', DbEnvDescriptor, (), (
        ('name', (), IcePy._t_string),
        ('description', (), IcePy._t_string),
        ('dbHome', (), IcePy._t_string),
        ('properties', (), _M_IceGrid._t_PropertyDescriptorSeq)
    ))

    _M_IceGrid.DbEnvDescriptor = DbEnvDescriptor
    del DbEnvDescriptor

if not _M_IceGrid.__dict__.has_key('_t_DbEnvDescriptorSeq'):
    _M_IceGrid._t_DbEnvDescriptorSeq = IcePy.defineSequence('::IceGrid::DbEnvDescriptorSeq', (), _M_IceGrid._t_DbEnvDescriptor)

if not _M_IceGrid.__dict__.has_key('CommunicatorDescriptor'):
    _M_IceGrid.CommunicatorDescriptor = Ice.createTempClass()
    class CommunicatorDescriptor(Ice.Object):
        def __init__(self, adapters=None, propertySet=Ice._struct_marker, dbEnvs=None, logs=None, description=''):
            self.adapters = adapters
            if propertySet is Ice._struct_marker:
                self.propertySet = _M_IceGrid.PropertySetDescriptor()
            else:
                self.propertySet = propertySet
            self.dbEnvs = dbEnvs
            self.logs = logs
            self.description = description

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::CommunicatorDescriptor')

        def ice_id(self, current=None):
            return '::IceGrid::CommunicatorDescriptor'

        def ice_staticId():
            return '::IceGrid::CommunicatorDescriptor'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_CommunicatorDescriptor)

        __repr__ = __str__

    _M_IceGrid.CommunicatorDescriptorPrx = Ice.createTempClass()
    class CommunicatorDescriptorPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.CommunicatorDescriptorPrx.ice_checkedCast(proxy, '::IceGrid::CommunicatorDescriptor', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.CommunicatorDescriptorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_CommunicatorDescriptorPrx = IcePy.defineProxy('::IceGrid::CommunicatorDescriptor', CommunicatorDescriptorPrx)

    _M_IceGrid._t_CommunicatorDescriptor = IcePy.defineClass('::IceGrid::CommunicatorDescriptor', CommunicatorDescriptor, (), False, None, (), (
        ('adapters', (), _M_IceGrid._t_AdapterDescriptorSeq),
        ('propertySet', (), _M_IceGrid._t_PropertySetDescriptor),
        ('dbEnvs', (), _M_IceGrid._t_DbEnvDescriptorSeq),
        ('logs', (), _M_Ice._t_StringSeq),
        ('description', (), IcePy._t_string)
    ))
    CommunicatorDescriptor.ice_type = _M_IceGrid._t_CommunicatorDescriptor

    _M_IceGrid.CommunicatorDescriptor = CommunicatorDescriptor
    del CommunicatorDescriptor

    _M_IceGrid.CommunicatorDescriptorPrx = CommunicatorDescriptorPrx
    del CommunicatorDescriptorPrx

if not _M_IceGrid.__dict__.has_key('DistributionDescriptor'):
    _M_IceGrid.DistributionDescriptor = Ice.createTempClass()
    class DistributionDescriptor(object):
        def __init__(self, icepatch='', directories=None):
            self.icepatch = icepatch
            self.directories = directories

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.icepatch)
            if self.directories:
                for _i0 in self.directories:
                    _h = 5 * _h + __builtin__.hash(_i0)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.icepatch < other.icepatch:
                return -1
            elif self.icepatch > other.icepatch:
                return 1
            if self.directories < other.directories:
                return -1
            elif self.directories > other.directories:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_DistributionDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_DistributionDescriptor = IcePy.defineStruct('::IceGrid::DistributionDescriptor', DistributionDescriptor, (), (
        ('icepatch', (), IcePy._t_string),
        ('directories', (), _M_Ice._t_StringSeq)
    ))

    _M_IceGrid.DistributionDescriptor = DistributionDescriptor
    del DistributionDescriptor

if not _M_IceGrid.__dict__.has_key('ServerDescriptor'):
    _M_IceGrid.ServerDescriptor = Ice.createTempClass()
    class ServerDescriptor(_M_IceGrid.CommunicatorDescriptor):
        def __init__(self, adapters=None, propertySet=Ice._struct_marker, dbEnvs=None, logs=None, description='', id='', exe='', iceVersion='', pwd='', options=None, envs=None, activation='', activationTimeout='', deactivationTimeout='', applicationDistrib=False, distrib=Ice._struct_marker, allocatable=False, user=''):
            _M_IceGrid.CommunicatorDescriptor.__init__(self, adapters, propertySet, dbEnvs, logs, description)
            self.id = id
            self.exe = exe
            self.iceVersion = iceVersion
            self.pwd = pwd
            self.options = options
            self.envs = envs
            self.activation = activation
            self.activationTimeout = activationTimeout
            self.deactivationTimeout = deactivationTimeout
            self.applicationDistrib = applicationDistrib
            if distrib is Ice._struct_marker:
                self.distrib = _M_IceGrid.DistributionDescriptor()
            else:
                self.distrib = distrib
            self.allocatable = allocatable
            self.user = user

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::CommunicatorDescriptor', '::IceGrid::ServerDescriptor')

        def ice_id(self, current=None):
            return '::IceGrid::ServerDescriptor'

        def ice_staticId():
            return '::IceGrid::ServerDescriptor'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ServerDescriptor)

        __repr__ = __str__

    _M_IceGrid.ServerDescriptorPrx = Ice.createTempClass()
    class ServerDescriptorPrx(_M_IceGrid.CommunicatorDescriptorPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.ServerDescriptorPrx.ice_checkedCast(proxy, '::IceGrid::ServerDescriptor', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.ServerDescriptorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_ServerDescriptorPrx = IcePy.defineProxy('::IceGrid::ServerDescriptor', ServerDescriptorPrx)

    _M_IceGrid._t_ServerDescriptor = IcePy.defineClass('::IceGrid::ServerDescriptor', ServerDescriptor, (), False, _M_IceGrid._t_CommunicatorDescriptor, (), (
        ('id', (), IcePy._t_string),
        ('exe', (), IcePy._t_string),
        ('iceVersion', (), IcePy._t_string),
        ('pwd', (), IcePy._t_string),
        ('options', (), _M_Ice._t_StringSeq),
        ('envs', (), _M_Ice._t_StringSeq),
        ('activation', (), IcePy._t_string),
        ('activationTimeout', (), IcePy._t_string),
        ('deactivationTimeout', (), IcePy._t_string),
        ('applicationDistrib', (), IcePy._t_bool),
        ('distrib', (), _M_IceGrid._t_DistributionDescriptor),
        ('allocatable', (), IcePy._t_bool),
        ('user', (), IcePy._t_string)
    ))
    ServerDescriptor.ice_type = _M_IceGrid._t_ServerDescriptor

    _M_IceGrid.ServerDescriptor = ServerDescriptor
    del ServerDescriptor

    _M_IceGrid.ServerDescriptorPrx = ServerDescriptorPrx
    del ServerDescriptorPrx

if not _M_IceGrid.__dict__.has_key('_t_ServerDescriptorSeq'):
    _M_IceGrid._t_ServerDescriptorSeq = IcePy.defineSequence('::IceGrid::ServerDescriptorSeq', (), _M_IceGrid._t_ServerDescriptor)

if not _M_IceGrid.__dict__.has_key('ServiceDescriptor'):
    _M_IceGrid.ServiceDescriptor = Ice.createTempClass()
    class ServiceDescriptor(_M_IceGrid.CommunicatorDescriptor):
        def __init__(self, adapters=None, propertySet=Ice._struct_marker, dbEnvs=None, logs=None, description='', name='', entry=''):
            _M_IceGrid.CommunicatorDescriptor.__init__(self, adapters, propertySet, dbEnvs, logs, description)
            self.name = name
            self.entry = entry

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::CommunicatorDescriptor', '::IceGrid::ServiceDescriptor')

        def ice_id(self, current=None):
            return '::IceGrid::ServiceDescriptor'

        def ice_staticId():
            return '::IceGrid::ServiceDescriptor'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ServiceDescriptor)

        __repr__ = __str__

    _M_IceGrid.ServiceDescriptorPrx = Ice.createTempClass()
    class ServiceDescriptorPrx(_M_IceGrid.CommunicatorDescriptorPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.ServiceDescriptorPrx.ice_checkedCast(proxy, '::IceGrid::ServiceDescriptor', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.ServiceDescriptorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_ServiceDescriptorPrx = IcePy.defineProxy('::IceGrid::ServiceDescriptor', ServiceDescriptorPrx)

    _M_IceGrid._t_ServiceDescriptor = IcePy.defineClass('::IceGrid::ServiceDescriptor', ServiceDescriptor, (), False, _M_IceGrid._t_CommunicatorDescriptor, (), (
        ('name', (), IcePy._t_string),
        ('entry', (), IcePy._t_string)
    ))
    ServiceDescriptor.ice_type = _M_IceGrid._t_ServiceDescriptor

    _M_IceGrid.ServiceDescriptor = ServiceDescriptor
    del ServiceDescriptor

    _M_IceGrid.ServiceDescriptorPrx = ServiceDescriptorPrx
    del ServiceDescriptorPrx

if not _M_IceGrid.__dict__.has_key('_t_ServiceDescriptorSeq'):
    _M_IceGrid._t_ServiceDescriptorSeq = IcePy.defineSequence('::IceGrid::ServiceDescriptorSeq', (), _M_IceGrid._t_ServiceDescriptor)

if not _M_IceGrid.__dict__.has_key('ServerInstanceDescriptor'):
    _M_IceGrid.ServerInstanceDescriptor = Ice.createTempClass()
    class ServerInstanceDescriptor(object):
        def __init__(self, template='', parameterValues=None, propertySet=Ice._struct_marker, servicePropertySets=None):
            self.template = template
            self.parameterValues = parameterValues
            if propertySet is Ice._struct_marker:
                self.propertySet = _M_IceGrid.PropertySetDescriptor()
            else:
                self.propertySet = propertySet
            self.servicePropertySets = servicePropertySets

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.template)
            if self.parameterValues:
                for _i0 in self.parameterValues:
                    _h = 5 * _h + __builtin__.hash(_i0)
                    _h = 5 * _h + __builtin__.hash(self.parameterValues[_i0])
            _h = 5 * _h + __builtin__.hash(self.propertySet)
            if self.servicePropertySets:
                for _i1 in self.servicePropertySets:
                    _h = 5 * _h + __builtin__.hash(_i1)
                    _h = 5 * _h + __builtin__.hash(self.servicePropertySets[_i1])
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.template < other.template:
                return -1
            elif self.template > other.template:
                return 1
            if self.parameterValues < other.parameterValues:
                return -1
            elif self.parameterValues > other.parameterValues:
                return 1
            if self.propertySet < other.propertySet:
                return -1
            elif self.propertySet > other.propertySet:
                return 1
            if self.servicePropertySets < other.servicePropertySets:
                return -1
            elif self.servicePropertySets > other.servicePropertySets:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ServerInstanceDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_ServerInstanceDescriptor = IcePy.defineStruct('::IceGrid::ServerInstanceDescriptor', ServerInstanceDescriptor, (), (
        ('template', (), IcePy._t_string),
        ('parameterValues', (), _M_IceGrid._t_StringStringDict),
        ('propertySet', (), _M_IceGrid._t_PropertySetDescriptor),
        ('servicePropertySets', (), _M_IceGrid._t_PropertySetDescriptorDict)
    ))

    _M_IceGrid.ServerInstanceDescriptor = ServerInstanceDescriptor
    del ServerInstanceDescriptor

if not _M_IceGrid.__dict__.has_key('_t_ServerInstanceDescriptorSeq'):
    _M_IceGrid._t_ServerInstanceDescriptorSeq = IcePy.defineSequence('::IceGrid::ServerInstanceDescriptorSeq', (), _M_IceGrid._t_ServerInstanceDescriptor)

if not _M_IceGrid.__dict__.has_key('TemplateDescriptor'):
    _M_IceGrid.TemplateDescriptor = Ice.createTempClass()
    class TemplateDescriptor(object):
        def __init__(self, descriptor=None, parameters=None, parameterDefaults=None):
            self.descriptor = descriptor
            self.parameters = parameters
            self.parameterDefaults = parameterDefaults

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.descriptor)
            if self.parameters:
                for _i0 in self.parameters:
                    _h = 5 * _h + __builtin__.hash(_i0)
            if self.parameterDefaults:
                for _i1 in self.parameterDefaults:
                    _h = 5 * _h + __builtin__.hash(_i1)
                    _h = 5 * _h + __builtin__.hash(self.parameterDefaults[_i1])
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.descriptor < other.descriptor:
                return -1
            elif self.descriptor > other.descriptor:
                return 1
            if self.parameters < other.parameters:
                return -1
            elif self.parameters > other.parameters:
                return 1
            if self.parameterDefaults < other.parameterDefaults:
                return -1
            elif self.parameterDefaults > other.parameterDefaults:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_TemplateDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_TemplateDescriptor = IcePy.defineStruct('::IceGrid::TemplateDescriptor', TemplateDescriptor, (), (
        ('descriptor', (), _M_IceGrid._t_CommunicatorDescriptor),
        ('parameters', (), _M_Ice._t_StringSeq),
        ('parameterDefaults', (), _M_IceGrid._t_StringStringDict)
    ))

    _M_IceGrid.TemplateDescriptor = TemplateDescriptor
    del TemplateDescriptor

if not _M_IceGrid.__dict__.has_key('_t_TemplateDescriptorDict'):
    _M_IceGrid._t_TemplateDescriptorDict = IcePy.defineDictionary('::IceGrid::TemplateDescriptorDict', (), IcePy._t_string, _M_IceGrid._t_TemplateDescriptor)

if not _M_IceGrid.__dict__.has_key('ServiceInstanceDescriptor'):
    _M_IceGrid.ServiceInstanceDescriptor = Ice.createTempClass()
    class ServiceInstanceDescriptor(object):
        def __init__(self, template='', parameterValues=None, descriptor=None, propertySet=Ice._struct_marker):
            self.template = template
            self.parameterValues = parameterValues
            self.descriptor = descriptor
            if propertySet is Ice._struct_marker:
                self.propertySet = _M_IceGrid.PropertySetDescriptor()
            else:
                self.propertySet = propertySet

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.template)
            if self.parameterValues:
                for _i0 in self.parameterValues:
                    _h = 5 * _h + __builtin__.hash(_i0)
                    _h = 5 * _h + __builtin__.hash(self.parameterValues[_i0])
            _h = 5 * _h + __builtin__.hash(self.descriptor)
            _h = 5 * _h + __builtin__.hash(self.propertySet)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.template < other.template:
                return -1
            elif self.template > other.template:
                return 1
            if self.parameterValues < other.parameterValues:
                return -1
            elif self.parameterValues > other.parameterValues:
                return 1
            if self.descriptor < other.descriptor:
                return -1
            elif self.descriptor > other.descriptor:
                return 1
            if self.propertySet < other.propertySet:
                return -1
            elif self.propertySet > other.propertySet:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ServiceInstanceDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_ServiceInstanceDescriptor = IcePy.defineStruct('::IceGrid::ServiceInstanceDescriptor', ServiceInstanceDescriptor, (), (
        ('template', (), IcePy._t_string),
        ('parameterValues', (), _M_IceGrid._t_StringStringDict),
        ('descriptor', (), _M_IceGrid._t_ServiceDescriptor),
        ('propertySet', (), _M_IceGrid._t_PropertySetDescriptor)
    ))

    _M_IceGrid.ServiceInstanceDescriptor = ServiceInstanceDescriptor
    del ServiceInstanceDescriptor

if not _M_IceGrid.__dict__.has_key('_t_ServiceInstanceDescriptorSeq'):
    _M_IceGrid._t_ServiceInstanceDescriptorSeq = IcePy.defineSequence('::IceGrid::ServiceInstanceDescriptorSeq', (), _M_IceGrid._t_ServiceInstanceDescriptor)

if not _M_IceGrid.__dict__.has_key('IceBoxDescriptor'):
    _M_IceGrid.IceBoxDescriptor = Ice.createTempClass()
    class IceBoxDescriptor(_M_IceGrid.ServerDescriptor):
        def __init__(self, adapters=None, propertySet=Ice._struct_marker, dbEnvs=None, logs=None, description='', id='', exe='', iceVersion='', pwd='', options=None, envs=None, activation='', activationTimeout='', deactivationTimeout='', applicationDistrib=False, distrib=Ice._struct_marker, allocatable=False, user='', services=None):
            _M_IceGrid.ServerDescriptor.__init__(self, adapters, propertySet, dbEnvs, logs, description, id, exe, iceVersion, pwd, options, envs, activation, activationTimeout, deactivationTimeout, applicationDistrib, distrib, allocatable, user)
            self.services = services

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::CommunicatorDescriptor', '::IceGrid::IceBoxDescriptor', '::IceGrid::ServerDescriptor')

        def ice_id(self, current=None):
            return '::IceGrid::IceBoxDescriptor'

        def ice_staticId():
            return '::IceGrid::IceBoxDescriptor'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_IceBoxDescriptor)

        __repr__ = __str__

    _M_IceGrid.IceBoxDescriptorPrx = Ice.createTempClass()
    class IceBoxDescriptorPrx(_M_IceGrid.ServerDescriptorPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.IceBoxDescriptorPrx.ice_checkedCast(proxy, '::IceGrid::IceBoxDescriptor', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.IceBoxDescriptorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_IceBoxDescriptorPrx = IcePy.defineProxy('::IceGrid::IceBoxDescriptor', IceBoxDescriptorPrx)

    _M_IceGrid._t_IceBoxDescriptor = IcePy.declareClass('::IceGrid::IceBoxDescriptor')

    _M_IceGrid._t_IceBoxDescriptor = IcePy.defineClass('::IceGrid::IceBoxDescriptor', IceBoxDescriptor, (), False, _M_IceGrid._t_ServerDescriptor, (), (('services', (), _M_IceGrid._t_ServiceInstanceDescriptorSeq),))
    IceBoxDescriptor.ice_type = _M_IceGrid._t_IceBoxDescriptor

    _M_IceGrid.IceBoxDescriptor = IceBoxDescriptor
    del IceBoxDescriptor

    _M_IceGrid.IceBoxDescriptorPrx = IceBoxDescriptorPrx
    del IceBoxDescriptorPrx

if not _M_IceGrid.__dict__.has_key('NodeDescriptor'):
    _M_IceGrid.NodeDescriptor = Ice.createTempClass()
    class NodeDescriptor(object):
        def __init__(self, variables=None, serverInstances=None, servers=None, loadFactor='', description='', propertySets=None):
            self.variables = variables
            self.serverInstances = serverInstances
            self.servers = servers
            self.loadFactor = loadFactor
            self.description = description
            self.propertySets = propertySets

        def __hash__(self):
            _h = 0
            if self.variables:
                for _i0 in self.variables:
                    _h = 5 * _h + __builtin__.hash(_i0)
                    _h = 5 * _h + __builtin__.hash(self.variables[_i0])
            if self.serverInstances:
                for _i1 in self.serverInstances:
                    _h = 5 * _h + __builtin__.hash(_i1)
            if self.servers:
                for _i2 in self.servers:
                    _h = 5 * _h + __builtin__.hash(_i2)
            _h = 5 * _h + __builtin__.hash(self.loadFactor)
            _h = 5 * _h + __builtin__.hash(self.description)
            if self.propertySets:
                for _i3 in self.propertySets:
                    _h = 5 * _h + __builtin__.hash(_i3)
                    _h = 5 * _h + __builtin__.hash(self.propertySets[_i3])
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.variables < other.variables:
                return -1
            elif self.variables > other.variables:
                return 1
            if self.serverInstances < other.serverInstances:
                return -1
            elif self.serverInstances > other.serverInstances:
                return 1
            if self.servers < other.servers:
                return -1
            elif self.servers > other.servers:
                return 1
            if self.loadFactor < other.loadFactor:
                return -1
            elif self.loadFactor > other.loadFactor:
                return 1
            if self.description < other.description:
                return -1
            elif self.description > other.description:
                return 1
            if self.propertySets < other.propertySets:
                return -1
            elif self.propertySets > other.propertySets:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_NodeDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_NodeDescriptor = IcePy.defineStruct('::IceGrid::NodeDescriptor', NodeDescriptor, (), (
        ('variables', (), _M_IceGrid._t_StringStringDict),
        ('serverInstances', (), _M_IceGrid._t_ServerInstanceDescriptorSeq),
        ('servers', (), _M_IceGrid._t_ServerDescriptorSeq),
        ('loadFactor', (), IcePy._t_string),
        ('description', (), IcePy._t_string),
        ('propertySets', (), _M_IceGrid._t_PropertySetDescriptorDict)
    ))

    _M_IceGrid.NodeDescriptor = NodeDescriptor
    del NodeDescriptor

if not _M_IceGrid.__dict__.has_key('_t_NodeDescriptorDict'):
    _M_IceGrid._t_NodeDescriptorDict = IcePy.defineDictionary('::IceGrid::NodeDescriptorDict', (), IcePy._t_string, _M_IceGrid._t_NodeDescriptor)

if not _M_IceGrid.__dict__.has_key('LoadBalancingPolicy'):
    _M_IceGrid.LoadBalancingPolicy = Ice.createTempClass()
    class LoadBalancingPolicy(Ice.Object):
        def __init__(self, nReplicas=''):
            self.nReplicas = nReplicas

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::LoadBalancingPolicy')

        def ice_id(self, current=None):
            return '::IceGrid::LoadBalancingPolicy'

        def ice_staticId():
            return '::IceGrid::LoadBalancingPolicy'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_LoadBalancingPolicy)

        __repr__ = __str__

    _M_IceGrid.LoadBalancingPolicyPrx = Ice.createTempClass()
    class LoadBalancingPolicyPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.LoadBalancingPolicyPrx.ice_checkedCast(proxy, '::IceGrid::LoadBalancingPolicy', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.LoadBalancingPolicyPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_LoadBalancingPolicyPrx = IcePy.defineProxy('::IceGrid::LoadBalancingPolicy', LoadBalancingPolicyPrx)

    _M_IceGrid._t_LoadBalancingPolicy = IcePy.defineClass('::IceGrid::LoadBalancingPolicy', LoadBalancingPolicy, (), False, None, (), (('nReplicas', (), IcePy._t_string),))
    LoadBalancingPolicy.ice_type = _M_IceGrid._t_LoadBalancingPolicy

    _M_IceGrid.LoadBalancingPolicy = LoadBalancingPolicy
    del LoadBalancingPolicy

    _M_IceGrid.LoadBalancingPolicyPrx = LoadBalancingPolicyPrx
    del LoadBalancingPolicyPrx

if not _M_IceGrid.__dict__.has_key('RandomLoadBalancingPolicy'):
    _M_IceGrid.RandomLoadBalancingPolicy = Ice.createTempClass()
    class RandomLoadBalancingPolicy(_M_IceGrid.LoadBalancingPolicy):
        def __init__(self, nReplicas=''):
            _M_IceGrid.LoadBalancingPolicy.__init__(self, nReplicas)

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::LoadBalancingPolicy', '::IceGrid::RandomLoadBalancingPolicy')

        def ice_id(self, current=None):
            return '::IceGrid::RandomLoadBalancingPolicy'

        def ice_staticId():
            return '::IceGrid::RandomLoadBalancingPolicy'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_RandomLoadBalancingPolicy)

        __repr__ = __str__

    _M_IceGrid.RandomLoadBalancingPolicyPrx = Ice.createTempClass()
    class RandomLoadBalancingPolicyPrx(_M_IceGrid.LoadBalancingPolicyPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.RandomLoadBalancingPolicyPrx.ice_checkedCast(proxy, '::IceGrid::RandomLoadBalancingPolicy', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.RandomLoadBalancingPolicyPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_RandomLoadBalancingPolicyPrx = IcePy.defineProxy('::IceGrid::RandomLoadBalancingPolicy', RandomLoadBalancingPolicyPrx)

    _M_IceGrid._t_RandomLoadBalancingPolicy = IcePy.defineClass('::IceGrid::RandomLoadBalancingPolicy', RandomLoadBalancingPolicy, (), False, _M_IceGrid._t_LoadBalancingPolicy, (), ())
    RandomLoadBalancingPolicy.ice_type = _M_IceGrid._t_RandomLoadBalancingPolicy

    _M_IceGrid.RandomLoadBalancingPolicy = RandomLoadBalancingPolicy
    del RandomLoadBalancingPolicy

    _M_IceGrid.RandomLoadBalancingPolicyPrx = RandomLoadBalancingPolicyPrx
    del RandomLoadBalancingPolicyPrx

if not _M_IceGrid.__dict__.has_key('OrderedLoadBalancingPolicy'):
    _M_IceGrid.OrderedLoadBalancingPolicy = Ice.createTempClass()
    class OrderedLoadBalancingPolicy(_M_IceGrid.LoadBalancingPolicy):
        def __init__(self, nReplicas=''):
            _M_IceGrid.LoadBalancingPolicy.__init__(self, nReplicas)

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::LoadBalancingPolicy', '::IceGrid::OrderedLoadBalancingPolicy')

        def ice_id(self, current=None):
            return '::IceGrid::OrderedLoadBalancingPolicy'

        def ice_staticId():
            return '::IceGrid::OrderedLoadBalancingPolicy'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_OrderedLoadBalancingPolicy)

        __repr__ = __str__

    _M_IceGrid.OrderedLoadBalancingPolicyPrx = Ice.createTempClass()
    class OrderedLoadBalancingPolicyPrx(_M_IceGrid.LoadBalancingPolicyPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.OrderedLoadBalancingPolicyPrx.ice_checkedCast(proxy, '::IceGrid::OrderedLoadBalancingPolicy', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.OrderedLoadBalancingPolicyPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_OrderedLoadBalancingPolicyPrx = IcePy.defineProxy('::IceGrid::OrderedLoadBalancingPolicy', OrderedLoadBalancingPolicyPrx)

    _M_IceGrid._t_OrderedLoadBalancingPolicy = IcePy.defineClass('::IceGrid::OrderedLoadBalancingPolicy', OrderedLoadBalancingPolicy, (), False, _M_IceGrid._t_LoadBalancingPolicy, (), ())
    OrderedLoadBalancingPolicy.ice_type = _M_IceGrid._t_OrderedLoadBalancingPolicy

    _M_IceGrid.OrderedLoadBalancingPolicy = OrderedLoadBalancingPolicy
    del OrderedLoadBalancingPolicy

    _M_IceGrid.OrderedLoadBalancingPolicyPrx = OrderedLoadBalancingPolicyPrx
    del OrderedLoadBalancingPolicyPrx

if not _M_IceGrid.__dict__.has_key('RoundRobinLoadBalancingPolicy'):
    _M_IceGrid.RoundRobinLoadBalancingPolicy = Ice.createTempClass()
    class RoundRobinLoadBalancingPolicy(_M_IceGrid.LoadBalancingPolicy):
        def __init__(self, nReplicas=''):
            _M_IceGrid.LoadBalancingPolicy.__init__(self, nReplicas)

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::LoadBalancingPolicy', '::IceGrid::RoundRobinLoadBalancingPolicy')

        def ice_id(self, current=None):
            return '::IceGrid::RoundRobinLoadBalancingPolicy'

        def ice_staticId():
            return '::IceGrid::RoundRobinLoadBalancingPolicy'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_RoundRobinLoadBalancingPolicy)

        __repr__ = __str__

    _M_IceGrid.RoundRobinLoadBalancingPolicyPrx = Ice.createTempClass()
    class RoundRobinLoadBalancingPolicyPrx(_M_IceGrid.LoadBalancingPolicyPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.RoundRobinLoadBalancingPolicyPrx.ice_checkedCast(proxy, '::IceGrid::RoundRobinLoadBalancingPolicy', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.RoundRobinLoadBalancingPolicyPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_RoundRobinLoadBalancingPolicyPrx = IcePy.defineProxy('::IceGrid::RoundRobinLoadBalancingPolicy', RoundRobinLoadBalancingPolicyPrx)

    _M_IceGrid._t_RoundRobinLoadBalancingPolicy = IcePy.defineClass('::IceGrid::RoundRobinLoadBalancingPolicy', RoundRobinLoadBalancingPolicy, (), False, _M_IceGrid._t_LoadBalancingPolicy, (), ())
    RoundRobinLoadBalancingPolicy.ice_type = _M_IceGrid._t_RoundRobinLoadBalancingPolicy

    _M_IceGrid.RoundRobinLoadBalancingPolicy = RoundRobinLoadBalancingPolicy
    del RoundRobinLoadBalancingPolicy

    _M_IceGrid.RoundRobinLoadBalancingPolicyPrx = RoundRobinLoadBalancingPolicyPrx
    del RoundRobinLoadBalancingPolicyPrx

if not _M_IceGrid.__dict__.has_key('AdaptiveLoadBalancingPolicy'):
    _M_IceGrid.AdaptiveLoadBalancingPolicy = Ice.createTempClass()
    class AdaptiveLoadBalancingPolicy(_M_IceGrid.LoadBalancingPolicy):
        def __init__(self, nReplicas='', loadSample=''):
            _M_IceGrid.LoadBalancingPolicy.__init__(self, nReplicas)
            self.loadSample = loadSample

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::AdaptiveLoadBalancingPolicy', '::IceGrid::LoadBalancingPolicy')

        def ice_id(self, current=None):
            return '::IceGrid::AdaptiveLoadBalancingPolicy'

        def ice_staticId():
            return '::IceGrid::AdaptiveLoadBalancingPolicy'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_AdaptiveLoadBalancingPolicy)

        __repr__ = __str__

    _M_IceGrid.AdaptiveLoadBalancingPolicyPrx = Ice.createTempClass()
    class AdaptiveLoadBalancingPolicyPrx(_M_IceGrid.LoadBalancingPolicyPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.AdaptiveLoadBalancingPolicyPrx.ice_checkedCast(proxy, '::IceGrid::AdaptiveLoadBalancingPolicy', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.AdaptiveLoadBalancingPolicyPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_AdaptiveLoadBalancingPolicyPrx = IcePy.defineProxy('::IceGrid::AdaptiveLoadBalancingPolicy', AdaptiveLoadBalancingPolicyPrx)

    _M_IceGrid._t_AdaptiveLoadBalancingPolicy = IcePy.defineClass('::IceGrid::AdaptiveLoadBalancingPolicy', AdaptiveLoadBalancingPolicy, (), False, _M_IceGrid._t_LoadBalancingPolicy, (), (('loadSample', (), IcePy._t_string),))
    AdaptiveLoadBalancingPolicy.ice_type = _M_IceGrid._t_AdaptiveLoadBalancingPolicy

    _M_IceGrid.AdaptiveLoadBalancingPolicy = AdaptiveLoadBalancingPolicy
    del AdaptiveLoadBalancingPolicy

    _M_IceGrid.AdaptiveLoadBalancingPolicyPrx = AdaptiveLoadBalancingPolicyPrx
    del AdaptiveLoadBalancingPolicyPrx

if not _M_IceGrid.__dict__.has_key('ReplicaGroupDescriptor'):
    _M_IceGrid.ReplicaGroupDescriptor = Ice.createTempClass()
    class ReplicaGroupDescriptor(object):
        def __init__(self, id='', loadBalancing=None, objects=None, description=''):
            self.id = id
            self.loadBalancing = loadBalancing
            self.objects = objects
            self.description = description

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.id)
            _h = 5 * _h + __builtin__.hash(self.loadBalancing)
            if self.objects:
                for _i0 in self.objects:
                    _h = 5 * _h + __builtin__.hash(_i0)
            _h = 5 * _h + __builtin__.hash(self.description)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.id < other.id:
                return -1
            elif self.id > other.id:
                return 1
            if self.loadBalancing < other.loadBalancing:
                return -1
            elif self.loadBalancing > other.loadBalancing:
                return 1
            if self.objects < other.objects:
                return -1
            elif self.objects > other.objects:
                return 1
            if self.description < other.description:
                return -1
            elif self.description > other.description:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ReplicaGroupDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_ReplicaGroupDescriptor = IcePy.defineStruct('::IceGrid::ReplicaGroupDescriptor', ReplicaGroupDescriptor, (), (
        ('id', (), IcePy._t_string),
        ('loadBalancing', (), _M_IceGrid._t_LoadBalancingPolicy),
        ('objects', (), _M_IceGrid._t_ObjectDescriptorSeq),
        ('description', (), IcePy._t_string)
    ))

    _M_IceGrid.ReplicaGroupDescriptor = ReplicaGroupDescriptor
    del ReplicaGroupDescriptor

if not _M_IceGrid.__dict__.has_key('_t_ReplicaGroupDescriptorSeq'):
    _M_IceGrid._t_ReplicaGroupDescriptorSeq = IcePy.defineSequence('::IceGrid::ReplicaGroupDescriptorSeq', (), _M_IceGrid._t_ReplicaGroupDescriptor)

if not _M_IceGrid.__dict__.has_key('ApplicationDescriptor'):
    _M_IceGrid.ApplicationDescriptor = Ice.createTempClass()
    class ApplicationDescriptor(object):
        def __init__(self, name='', variables=None, replicaGroups=None, serverTemplates=None, serviceTemplates=None, nodes=None, distrib=Ice._struct_marker, description='', propertySets=None):
            self.name = name
            self.variables = variables
            self.replicaGroups = replicaGroups
            self.serverTemplates = serverTemplates
            self.serviceTemplates = serviceTemplates
            self.nodes = nodes
            if distrib is Ice._struct_marker:
                self.distrib = _M_IceGrid.DistributionDescriptor()
            else:
                self.distrib = distrib
            self.description = description
            self.propertySets = propertySets

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.name)
            if self.variables:
                for _i0 in self.variables:
                    _h = 5 * _h + __builtin__.hash(_i0)
                    _h = 5 * _h + __builtin__.hash(self.variables[_i0])
            if self.replicaGroups:
                for _i1 in self.replicaGroups:
                    _h = 5 * _h + __builtin__.hash(_i1)
            if self.serverTemplates:
                for _i2 in self.serverTemplates:
                    _h = 5 * _h + __builtin__.hash(_i2)
                    _h = 5 * _h + __builtin__.hash(self.serverTemplates[_i2])
            if self.serviceTemplates:
                for _i3 in self.serviceTemplates:
                    _h = 5 * _h + __builtin__.hash(_i3)
                    _h = 5 * _h + __builtin__.hash(self.serviceTemplates[_i3])
            if self.nodes:
                for _i4 in self.nodes:
                    _h = 5 * _h + __builtin__.hash(_i4)
                    _h = 5 * _h + __builtin__.hash(self.nodes[_i4])
            _h = 5 * _h + __builtin__.hash(self.distrib)
            _h = 5 * _h + __builtin__.hash(self.description)
            if self.propertySets:
                for _i5 in self.propertySets:
                    _h = 5 * _h + __builtin__.hash(_i5)
                    _h = 5 * _h + __builtin__.hash(self.propertySets[_i5])
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            if self.variables < other.variables:
                return -1
            elif self.variables > other.variables:
                return 1
            if self.replicaGroups < other.replicaGroups:
                return -1
            elif self.replicaGroups > other.replicaGroups:
                return 1
            if self.serverTemplates < other.serverTemplates:
                return -1
            elif self.serverTemplates > other.serverTemplates:
                return 1
            if self.serviceTemplates < other.serviceTemplates:
                return -1
            elif self.serviceTemplates > other.serviceTemplates:
                return 1
            if self.nodes < other.nodes:
                return -1
            elif self.nodes > other.nodes:
                return 1
            if self.distrib < other.distrib:
                return -1
            elif self.distrib > other.distrib:
                return 1
            if self.description < other.description:
                return -1
            elif self.description > other.description:
                return 1
            if self.propertySets < other.propertySets:
                return -1
            elif self.propertySets > other.propertySets:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ApplicationDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_ApplicationDescriptor = IcePy.defineStruct('::IceGrid::ApplicationDescriptor', ApplicationDescriptor, (), (
        ('name', (), IcePy._t_string),
        ('variables', (), _M_IceGrid._t_StringStringDict),
        ('replicaGroups', (), _M_IceGrid._t_ReplicaGroupDescriptorSeq),
        ('serverTemplates', (), _M_IceGrid._t_TemplateDescriptorDict),
        ('serviceTemplates', (), _M_IceGrid._t_TemplateDescriptorDict),
        ('nodes', (), _M_IceGrid._t_NodeDescriptorDict),
        ('distrib', (), _M_IceGrid._t_DistributionDescriptor),
        ('description', (), IcePy._t_string),
        ('propertySets', (), _M_IceGrid._t_PropertySetDescriptorDict)
    ))

    _M_IceGrid.ApplicationDescriptor = ApplicationDescriptor
    del ApplicationDescriptor

if not _M_IceGrid.__dict__.has_key('_t_ApplicationDescriptorSeq'):
    _M_IceGrid._t_ApplicationDescriptorSeq = IcePy.defineSequence('::IceGrid::ApplicationDescriptorSeq', (), _M_IceGrid._t_ApplicationDescriptor)

if not _M_IceGrid.__dict__.has_key('BoxedString'):
    _M_IceGrid.BoxedString = Ice.createTempClass()
    class BoxedString(Ice.Object):
        def __init__(self, value=''):
            self.value = value

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::BoxedString')

        def ice_id(self, current=None):
            return '::IceGrid::BoxedString'

        def ice_staticId():
            return '::IceGrid::BoxedString'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_BoxedString)

        __repr__ = __str__

    _M_IceGrid.BoxedStringPrx = Ice.createTempClass()
    class BoxedStringPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.BoxedStringPrx.ice_checkedCast(proxy, '::IceGrid::BoxedString', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.BoxedStringPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_BoxedStringPrx = IcePy.defineProxy('::IceGrid::BoxedString', BoxedStringPrx)

    _M_IceGrid._t_BoxedString = IcePy.defineClass('::IceGrid::BoxedString', BoxedString, (), False, None, (), (('value', (), IcePy._t_string),))
    BoxedString.ice_type = _M_IceGrid._t_BoxedString

    _M_IceGrid.BoxedString = BoxedString
    del BoxedString

    _M_IceGrid.BoxedStringPrx = BoxedStringPrx
    del BoxedStringPrx

if not _M_IceGrid.__dict__.has_key('NodeUpdateDescriptor'):
    _M_IceGrid.NodeUpdateDescriptor = Ice.createTempClass()
    class NodeUpdateDescriptor(object):
        def __init__(self, name='', description=None, variables=None, removeVariables=None, propertySets=None, removePropertySets=None, serverInstances=None, servers=None, removeServers=None, loadFactor=None):
            self.name = name
            self.description = description
            self.variables = variables
            self.removeVariables = removeVariables
            self.propertySets = propertySets
            self.removePropertySets = removePropertySets
            self.serverInstances = serverInstances
            self.servers = servers
            self.removeServers = removeServers
            self.loadFactor = loadFactor

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.name)
            _h = 5 * _h + __builtin__.hash(self.description)
            if self.variables:
                for _i0 in self.variables:
                    _h = 5 * _h + __builtin__.hash(_i0)
                    _h = 5 * _h + __builtin__.hash(self.variables[_i0])
            if self.removeVariables:
                for _i1 in self.removeVariables:
                    _h = 5 * _h + __builtin__.hash(_i1)
            if self.propertySets:
                for _i2 in self.propertySets:
                    _h = 5 * _h + __builtin__.hash(_i2)
                    _h = 5 * _h + __builtin__.hash(self.propertySets[_i2])
            if self.removePropertySets:
                for _i3 in self.removePropertySets:
                    _h = 5 * _h + __builtin__.hash(_i3)
            if self.serverInstances:
                for _i4 in self.serverInstances:
                    _h = 5 * _h + __builtin__.hash(_i4)
            if self.servers:
                for _i5 in self.servers:
                    _h = 5 * _h + __builtin__.hash(_i5)
            if self.removeServers:
                for _i6 in self.removeServers:
                    _h = 5 * _h + __builtin__.hash(_i6)
            _h = 5 * _h + __builtin__.hash(self.loadFactor)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            if self.description < other.description:
                return -1
            elif self.description > other.description:
                return 1
            if self.variables < other.variables:
                return -1
            elif self.variables > other.variables:
                return 1
            if self.removeVariables < other.removeVariables:
                return -1
            elif self.removeVariables > other.removeVariables:
                return 1
            if self.propertySets < other.propertySets:
                return -1
            elif self.propertySets > other.propertySets:
                return 1
            if self.removePropertySets < other.removePropertySets:
                return -1
            elif self.removePropertySets > other.removePropertySets:
                return 1
            if self.serverInstances < other.serverInstances:
                return -1
            elif self.serverInstances > other.serverInstances:
                return 1
            if self.servers < other.servers:
                return -1
            elif self.servers > other.servers:
                return 1
            if self.removeServers < other.removeServers:
                return -1
            elif self.removeServers > other.removeServers:
                return 1
            if self.loadFactor < other.loadFactor:
                return -1
            elif self.loadFactor > other.loadFactor:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_NodeUpdateDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_NodeUpdateDescriptor = IcePy.defineStruct('::IceGrid::NodeUpdateDescriptor', NodeUpdateDescriptor, (), (
        ('name', (), IcePy._t_string),
        ('description', (), _M_IceGrid._t_BoxedString),
        ('variables', (), _M_IceGrid._t_StringStringDict),
        ('removeVariables', (), _M_Ice._t_StringSeq),
        ('propertySets', (), _M_IceGrid._t_PropertySetDescriptorDict),
        ('removePropertySets', (), _M_Ice._t_StringSeq),
        ('serverInstances', (), _M_IceGrid._t_ServerInstanceDescriptorSeq),
        ('servers', (), _M_IceGrid._t_ServerDescriptorSeq),
        ('removeServers', (), _M_Ice._t_StringSeq),
        ('loadFactor', (), _M_IceGrid._t_BoxedString)
    ))

    _M_IceGrid.NodeUpdateDescriptor = NodeUpdateDescriptor
    del NodeUpdateDescriptor

if not _M_IceGrid.__dict__.has_key('_t_NodeUpdateDescriptorSeq'):
    _M_IceGrid._t_NodeUpdateDescriptorSeq = IcePy.defineSequence('::IceGrid::NodeUpdateDescriptorSeq', (), _M_IceGrid._t_NodeUpdateDescriptor)

if not _M_IceGrid.__dict__.has_key('BoxedDistributionDescriptor'):
    _M_IceGrid.BoxedDistributionDescriptor = Ice.createTempClass()
    class BoxedDistributionDescriptor(Ice.Object):
        def __init__(self, value=Ice._struct_marker):
            if value is Ice._struct_marker:
                self.value = _M_IceGrid.DistributionDescriptor()
            else:
                self.value = value

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::BoxedDistributionDescriptor')

        def ice_id(self, current=None):
            return '::IceGrid::BoxedDistributionDescriptor'

        def ice_staticId():
            return '::IceGrid::BoxedDistributionDescriptor'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_BoxedDistributionDescriptor)

        __repr__ = __str__

    _M_IceGrid.BoxedDistributionDescriptorPrx = Ice.createTempClass()
    class BoxedDistributionDescriptorPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.BoxedDistributionDescriptorPrx.ice_checkedCast(proxy, '::IceGrid::BoxedDistributionDescriptor', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.BoxedDistributionDescriptorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_BoxedDistributionDescriptorPrx = IcePy.defineProxy('::IceGrid::BoxedDistributionDescriptor', BoxedDistributionDescriptorPrx)

    _M_IceGrid._t_BoxedDistributionDescriptor = IcePy.defineClass('::IceGrid::BoxedDistributionDescriptor', BoxedDistributionDescriptor, (), False, None, (), (('value', (), _M_IceGrid._t_DistributionDescriptor),))
    BoxedDistributionDescriptor.ice_type = _M_IceGrid._t_BoxedDistributionDescriptor

    _M_IceGrid.BoxedDistributionDescriptor = BoxedDistributionDescriptor
    del BoxedDistributionDescriptor

    _M_IceGrid.BoxedDistributionDescriptorPrx = BoxedDistributionDescriptorPrx
    del BoxedDistributionDescriptorPrx

if not _M_IceGrid.__dict__.has_key('ApplicationUpdateDescriptor'):
    _M_IceGrid.ApplicationUpdateDescriptor = Ice.createTempClass()
    class ApplicationUpdateDescriptor(object):
        def __init__(self, name='', description=None, distrib=None, variables=None, removeVariables=None, propertySets=None, removePropertySets=None, replicaGroups=None, removeReplicaGroups=None, serverTemplates=None, removeServerTemplates=None, serviceTemplates=None, removeServiceTemplates=None, nodes=None, removeNodes=None):
            self.name = name
            self.description = description
            self.distrib = distrib
            self.variables = variables
            self.removeVariables = removeVariables
            self.propertySets = propertySets
            self.removePropertySets = removePropertySets
            self.replicaGroups = replicaGroups
            self.removeReplicaGroups = removeReplicaGroups
            self.serverTemplates = serverTemplates
            self.removeServerTemplates = removeServerTemplates
            self.serviceTemplates = serviceTemplates
            self.removeServiceTemplates = removeServiceTemplates
            self.nodes = nodes
            self.removeNodes = removeNodes

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.name)
            _h = 5 * _h + __builtin__.hash(self.description)
            _h = 5 * _h + __builtin__.hash(self.distrib)
            if self.variables:
                for _i0 in self.variables:
                    _h = 5 * _h + __builtin__.hash(_i0)
                    _h = 5 * _h + __builtin__.hash(self.variables[_i0])
            if self.removeVariables:
                for _i1 in self.removeVariables:
                    _h = 5 * _h + __builtin__.hash(_i1)
            if self.propertySets:
                for _i2 in self.propertySets:
                    _h = 5 * _h + __builtin__.hash(_i2)
                    _h = 5 * _h + __builtin__.hash(self.propertySets[_i2])
            if self.removePropertySets:
                for _i3 in self.removePropertySets:
                    _h = 5 * _h + __builtin__.hash(_i3)
            if self.replicaGroups:
                for _i4 in self.replicaGroups:
                    _h = 5 * _h + __builtin__.hash(_i4)
            if self.removeReplicaGroups:
                for _i5 in self.removeReplicaGroups:
                    _h = 5 * _h + __builtin__.hash(_i5)
            if self.serverTemplates:
                for _i6 in self.serverTemplates:
                    _h = 5 * _h + __builtin__.hash(_i6)
                    _h = 5 * _h + __builtin__.hash(self.serverTemplates[_i6])
            if self.removeServerTemplates:
                for _i7 in self.removeServerTemplates:
                    _h = 5 * _h + __builtin__.hash(_i7)
            if self.serviceTemplates:
                for _i8 in self.serviceTemplates:
                    _h = 5 * _h + __builtin__.hash(_i8)
                    _h = 5 * _h + __builtin__.hash(self.serviceTemplates[_i8])
            if self.removeServiceTemplates:
                for _i9 in self.removeServiceTemplates:
                    _h = 5 * _h + __builtin__.hash(_i9)
            if self.nodes:
                for _i10 in self.nodes:
                    _h = 5 * _h + __builtin__.hash(_i10)
            if self.removeNodes:
                for _i11 in self.removeNodes:
                    _h = 5 * _h + __builtin__.hash(_i11)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            if self.description < other.description:
                return -1
            elif self.description > other.description:
                return 1
            if self.distrib < other.distrib:
                return -1
            elif self.distrib > other.distrib:
                return 1
            if self.variables < other.variables:
                return -1
            elif self.variables > other.variables:
                return 1
            if self.removeVariables < other.removeVariables:
                return -1
            elif self.removeVariables > other.removeVariables:
                return 1
            if self.propertySets < other.propertySets:
                return -1
            elif self.propertySets > other.propertySets:
                return 1
            if self.removePropertySets < other.removePropertySets:
                return -1
            elif self.removePropertySets > other.removePropertySets:
                return 1
            if self.replicaGroups < other.replicaGroups:
                return -1
            elif self.replicaGroups > other.replicaGroups:
                return 1
            if self.removeReplicaGroups < other.removeReplicaGroups:
                return -1
            elif self.removeReplicaGroups > other.removeReplicaGroups:
                return 1
            if self.serverTemplates < other.serverTemplates:
                return -1
            elif self.serverTemplates > other.serverTemplates:
                return 1
            if self.removeServerTemplates < other.removeServerTemplates:
                return -1
            elif self.removeServerTemplates > other.removeServerTemplates:
                return 1
            if self.serviceTemplates < other.serviceTemplates:
                return -1
            elif self.serviceTemplates > other.serviceTemplates:
                return 1
            if self.removeServiceTemplates < other.removeServiceTemplates:
                return -1
            elif self.removeServiceTemplates > other.removeServiceTemplates:
                return 1
            if self.nodes < other.nodes:
                return -1
            elif self.nodes > other.nodes:
                return 1
            if self.removeNodes < other.removeNodes:
                return -1
            elif self.removeNodes > other.removeNodes:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_ApplicationUpdateDescriptor)

        __repr__ = __str__

    _M_IceGrid._t_ApplicationUpdateDescriptor = IcePy.defineStruct('::IceGrid::ApplicationUpdateDescriptor', ApplicationUpdateDescriptor, (), (
        ('name', (), IcePy._t_string),
        ('description', (), _M_IceGrid._t_BoxedString),
        ('distrib', (), _M_IceGrid._t_BoxedDistributionDescriptor),
        ('variables', (), _M_IceGrid._t_StringStringDict),
        ('removeVariables', (), _M_Ice._t_StringSeq),
        ('propertySets', (), _M_IceGrid._t_PropertySetDescriptorDict),
        ('removePropertySets', (), _M_Ice._t_StringSeq),
        ('replicaGroups', (), _M_IceGrid._t_ReplicaGroupDescriptorSeq),
        ('removeReplicaGroups', (), _M_Ice._t_StringSeq),
        ('serverTemplates', (), _M_IceGrid._t_TemplateDescriptorDict),
        ('removeServerTemplates', (), _M_Ice._t_StringSeq),
        ('serviceTemplates', (), _M_IceGrid._t_TemplateDescriptorDict),
        ('removeServiceTemplates', (), _M_Ice._t_StringSeq),
        ('nodes', (), _M_IceGrid._t_NodeUpdateDescriptorSeq),
        ('removeNodes', (), _M_Ice._t_StringSeq)
    ))

    _M_IceGrid.ApplicationUpdateDescriptor = ApplicationUpdateDescriptor
    del ApplicationUpdateDescriptor

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::AdapterDescriptor"] = "4ae12581eab9d8ecba56534d28960f0"
Ice.sliceChecksums["::IceGrid::AdapterDescriptorSeq"] = "61bb9118038552b5e80bf14cf41719c"
Ice.sliceChecksums["::IceGrid::AdaptiveLoadBalancingPolicy"] = "eae551a45bf88ecdfdcbd169e3502816"
Ice.sliceChecksums["::IceGrid::ApplicationDescriptor"] = "fc17fb9c4c7fc8f17ad10bc5da634a0"
Ice.sliceChecksums["::IceGrid::ApplicationDescriptorSeq"] = "b56d6d3091e8c0199e924bbdc074"
Ice.sliceChecksums["::IceGrid::ApplicationUpdateDescriptor"] = "9aef62072a0ecc3ee4be33bc46e0da"
Ice.sliceChecksums["::IceGrid::BoxedDistributionDescriptor"] = "bab8796f5dc33ebe6955d4bb3219c5e9"
Ice.sliceChecksums["::IceGrid::BoxedString"] = "f6bfc069c5150c34e14331c921218d7"
Ice.sliceChecksums["::IceGrid::CommunicatorDescriptor"] = "b7cdae49f8df0d1d93afb857875ec15"
Ice.sliceChecksums["::IceGrid::DbEnvDescriptor"] = "19c130dac4bf7fa2f82375a85e5f421"
Ice.sliceChecksums["::IceGrid::DbEnvDescriptorSeq"] = "d0e45f67b942541727ae69d6cda2fdd8"
Ice.sliceChecksums["::IceGrid::DistributionDescriptor"] = "109eee8e2dc57e518243806796d756"
Ice.sliceChecksums["::IceGrid::IceBoxDescriptor"] = "814eec3d42ab727f75f7b183e1b02c38"
Ice.sliceChecksums["::IceGrid::LoadBalancingPolicy"] = "dfbd5166bbdcac620f2d7f5de185afe"
Ice.sliceChecksums["::IceGrid::NodeDescriptor"] = "be38d2d0b946fea6266f7a97d493d4"
Ice.sliceChecksums["::IceGrid::NodeDescriptorDict"] = "600e78031867992f2fbd18719cb494"
Ice.sliceChecksums["::IceGrid::NodeUpdateDescriptor"] = "d1c0a29ce34753b44e54285c49c9780"
Ice.sliceChecksums["::IceGrid::NodeUpdateDescriptorSeq"] = "3416e1746e2acedfb8192d9d83d9dc3"
Ice.sliceChecksums["::IceGrid::ObjectDescriptor"] = "7df8af93b2bd6918d632115031afef9f"
Ice.sliceChecksums["::IceGrid::ObjectDescriptorSeq"] = "57236a6ef224f825849907a344412bb"
Ice.sliceChecksums["::IceGrid::OrderedLoadBalancingPolicy"] = "bef5dacddeeae0e0b58945adaea2121"
Ice.sliceChecksums["::IceGrid::PropertyDescriptor"] = "8b2145a8b1c5c8ffc9eac6a13e731798"
Ice.sliceChecksums["::IceGrid::PropertyDescriptorSeq"] = "5f4143ef7e2c87b63136a3177b7a2830"
Ice.sliceChecksums["::IceGrid::PropertySetDescriptor"] = "d07a6de61ed833b349d869bacb7d857"
Ice.sliceChecksums["::IceGrid::PropertySetDescriptorDict"] = "30fc60d722ab4ba7affa70387730322f"
Ice.sliceChecksums["::IceGrid::RandomLoadBalancingPolicy"] = "b52a26591c76fe2d6d134d954568c1a"
Ice.sliceChecksums["::IceGrid::ReplicaGroupDescriptor"] = "6e64712fedb23bb2c548916e74620c8"
Ice.sliceChecksums["::IceGrid::ReplicaGroupDescriptorSeq"] = "5a3d3e7b4dc5f21b74f7adb5a6b24ccc"
Ice.sliceChecksums["::IceGrid::RoundRobinLoadBalancingPolicy"] = "d9c7e987c732d89b7aa79621a788fcb4"
Ice.sliceChecksums["::IceGrid::ServerDescriptor"] = "45903227dd1968cedd1811b9d71bc374"
Ice.sliceChecksums["::IceGrid::ServerDescriptorSeq"] = "1bf128cadf1974b22258f66617a1ed"
Ice.sliceChecksums["::IceGrid::ServerInstanceDescriptor"] = "56938d38e0189cdbd57d16e5a6bbc0fb"
Ice.sliceChecksums["::IceGrid::ServerInstanceDescriptorSeq"] = "2a8ae55ccef7917d96691c0a84778dd"
Ice.sliceChecksums["::IceGrid::ServiceDescriptor"] = "7c2496565248aa7d9732565ee5fe7c"
Ice.sliceChecksums["::IceGrid::ServiceDescriptorSeq"] = "cc519ed2b7f626b896cdc062823166"
Ice.sliceChecksums["::IceGrid::ServiceInstanceDescriptor"] = "8581f0afc39ae7daab937244b28c1394"
Ice.sliceChecksums["::IceGrid::ServiceInstanceDescriptorSeq"] = "eb22cd2a50e79f648d803c4b54755"
Ice.sliceChecksums["::IceGrid::StringStringDict"] = "87cdc9524ba3964efc9091e5b3346f29"
Ice.sliceChecksums["::IceGrid::TemplateDescriptor"] = "d1229192d114f32db747493becd5765"
Ice.sliceChecksums["::IceGrid::TemplateDescriptorDict"] = "7b9427f03e8ce3b67decd2cc35baa1"
