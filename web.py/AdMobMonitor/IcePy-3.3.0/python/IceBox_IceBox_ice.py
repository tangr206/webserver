# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `IceBox.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_BuiltinSequences_ice
import Ice_CommunicatorF_ice
import Ice_PropertiesF_ice
import Ice_SliceChecksumDict_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module IceBox
_M_IceBox = Ice.openModule('IceBox')
__name__ = 'IceBox'

if not _M_IceBox.__dict__.has_key('FailureException'):
    _M_IceBox.FailureException = Ice.createTempClass()
    class FailureException(Ice.LocalException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'IceBox::FailureException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceBox._t_FailureException = IcePy.defineException('::IceBox::FailureException', FailureException, (), None, (('reason', (), IcePy._t_string),))
    FailureException.ice_type = _M_IceBox._t_FailureException

    _M_IceBox.FailureException = FailureException
    del FailureException

if not _M_IceBox.__dict__.has_key('AlreadyStartedException'):
    _M_IceBox.AlreadyStartedException = Ice.createTempClass()
    class AlreadyStartedException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'IceBox::AlreadyStartedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceBox._t_AlreadyStartedException = IcePy.defineException('::IceBox::AlreadyStartedException', AlreadyStartedException, (), None, ())
    AlreadyStartedException.ice_type = _M_IceBox._t_AlreadyStartedException

    _M_IceBox.AlreadyStartedException = AlreadyStartedException
    del AlreadyStartedException

if not _M_IceBox.__dict__.has_key('AlreadyStoppedException'):
    _M_IceBox.AlreadyStoppedException = Ice.createTempClass()
    class AlreadyStoppedException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'IceBox::AlreadyStoppedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceBox._t_AlreadyStoppedException = IcePy.defineException('::IceBox::AlreadyStoppedException', AlreadyStoppedException, (), None, ())
    AlreadyStoppedException.ice_type = _M_IceBox._t_AlreadyStoppedException

    _M_IceBox.AlreadyStoppedException = AlreadyStoppedException
    del AlreadyStoppedException

if not _M_IceBox.__dict__.has_key('NoSuchServiceException'):
    _M_IceBox.NoSuchServiceException = Ice.createTempClass()
    class NoSuchServiceException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'IceBox::NoSuchServiceException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceBox._t_NoSuchServiceException = IcePy.defineException('::IceBox::NoSuchServiceException', NoSuchServiceException, (), None, ())
    NoSuchServiceException.ice_type = _M_IceBox._t_NoSuchServiceException

    _M_IceBox.NoSuchServiceException = NoSuchServiceException
    del NoSuchServiceException

if not _M_IceBox.__dict__.has_key('Service'):
    _M_IceBox.Service = Ice.createTempClass()
    class Service(object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceBox.Service:
                raise RuntimeError('IceBox.Service is an abstract class')

        #
        # Operation signatures.
        #
        # def start(self, name, communicator, args):
        # def stop(self):

        def __str__(self):
            return IcePy.stringify(self, _M_IceBox._t_Service)

        __repr__ = __str__

    _M_IceBox._t_Service = IcePy.defineClass('::IceBox::Service', Service, (), True, None, (), ())
    Service.ice_type = _M_IceBox._t_Service

    _M_IceBox.Service = Service
    del Service

if not _M_IceBox.__dict__.has_key('ServiceObserver'):
    _M_IceBox.ServiceObserver = Ice.createTempClass()
    class ServiceObserver(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceBox.ServiceObserver:
                raise RuntimeError('IceBox.ServiceObserver is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceBox::ServiceObserver')

        def ice_id(self, current=None):
            return '::IceBox::ServiceObserver'

        def ice_staticId():
            return '::IceBox::ServiceObserver'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def servicesStarted(self, services, current=None):
        # def servicesStopped(self, services, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceBox._t_ServiceObserver)

        __repr__ = __str__

    _M_IceBox.ServiceObserverPrx = Ice.createTempClass()
    class ServiceObserverPrx(Ice.ObjectPrx):

        def servicesStarted(self, services, _ctx=None):
            return _M_IceBox.ServiceObserver._op_servicesStarted.invoke(self, ((services, ), _ctx))

        def servicesStarted_async(self, _cb, services, _ctx=None):
            return _M_IceBox.ServiceObserver._op_servicesStarted.invokeAsync(self, (_cb, (services, ), _ctx))

        def servicesStopped(self, services, _ctx=None):
            return _M_IceBox.ServiceObserver._op_servicesStopped.invoke(self, ((services, ), _ctx))

        def servicesStopped_async(self, _cb, services, _ctx=None):
            return _M_IceBox.ServiceObserver._op_servicesStopped.invokeAsync(self, (_cb, (services, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceBox.ServiceObserverPrx.ice_checkedCast(proxy, '::IceBox::ServiceObserver', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceBox.ServiceObserverPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceBox._t_ServiceObserverPrx = IcePy.defineProxy('::IceBox::ServiceObserver', ServiceObserverPrx)

    _M_IceBox._t_ServiceObserver = IcePy.defineClass('::IceBox::ServiceObserver', ServiceObserver, (), True, None, (), ())
    ServiceObserver.ice_type = _M_IceBox._t_ServiceObserver

    ServiceObserver._op_servicesStarted = IcePy.Operation('servicesStarted', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_Ice._t_StringSeq),), (), None, ())
    ServiceObserver._op_servicesStopped = IcePy.Operation('servicesStopped', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_Ice._t_StringSeq),), (), None, ())

    _M_IceBox.ServiceObserver = ServiceObserver
    del ServiceObserver

    _M_IceBox.ServiceObserverPrx = ServiceObserverPrx
    del ServiceObserverPrx

if not _M_IceBox.__dict__.has_key('ServiceManager'):
    _M_IceBox.ServiceManager = Ice.createTempClass()
    class ServiceManager(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceBox.ServiceManager:
                raise RuntimeError('IceBox.ServiceManager is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceBox::ServiceManager')

        def ice_id(self, current=None):
            return '::IceBox::ServiceManager'

        def ice_staticId():
            return '::IceBox::ServiceManager'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def getSliceChecksums(self, current=None):
        # def startService(self, service, current=None):
        # def stopService(self, service, current=None):
        # def addObserver(self, observer, current=None):
        # def shutdown(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceBox._t_ServiceManager)

        __repr__ = __str__

    _M_IceBox.ServiceManagerPrx = Ice.createTempClass()
    class ServiceManagerPrx(Ice.ObjectPrx):

        def getSliceChecksums(self, _ctx=None):
            return _M_IceBox.ServiceManager._op_getSliceChecksums.invoke(self, ((), _ctx))

        def startService(self, service, _ctx=None):
            return _M_IceBox.ServiceManager._op_startService.invoke(self, ((service, ), _ctx))

        def startService_async(self, _cb, service, _ctx=None):
            return _M_IceBox.ServiceManager._op_startService.invokeAsync(self, (_cb, (service, ), _ctx))

        def stopService(self, service, _ctx=None):
            return _M_IceBox.ServiceManager._op_stopService.invoke(self, ((service, ), _ctx))

        def stopService_async(self, _cb, service, _ctx=None):
            return _M_IceBox.ServiceManager._op_stopService.invokeAsync(self, (_cb, (service, ), _ctx))

        def addObserver(self, observer, _ctx=None):
            return _M_IceBox.ServiceManager._op_addObserver.invoke(self, ((observer, ), _ctx))

        def addObserver_async(self, _cb, observer, _ctx=None):
            return _M_IceBox.ServiceManager._op_addObserver.invokeAsync(self, (_cb, (observer, ), _ctx))

        def shutdown(self, _ctx=None):
            return _M_IceBox.ServiceManager._op_shutdown.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceBox.ServiceManagerPrx.ice_checkedCast(proxy, '::IceBox::ServiceManager', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceBox.ServiceManagerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceBox._t_ServiceManagerPrx = IcePy.defineProxy('::IceBox::ServiceManager', ServiceManagerPrx)

    _M_IceBox._t_ServiceManager = IcePy.defineClass('::IceBox::ServiceManager', ServiceManager, (), True, None, (), ())
    ServiceManager.ice_type = _M_IceBox._t_ServiceManager

    ServiceManager._op_getSliceChecksums = IcePy.Operation('getSliceChecksums', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_SliceChecksumDict, ())
    ServiceManager._op_startService = IcePy.Operation('startService', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, (_M_IceBox._t_AlreadyStartedException, _M_IceBox._t_NoSuchServiceException))
    ServiceManager._op_stopService = IcePy.Operation('stopService', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, (_M_IceBox._t_AlreadyStoppedException, _M_IceBox._t_NoSuchServiceException))
    ServiceManager._op_addObserver = IcePy.Operation('addObserver', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceBox._t_ServiceObserverPrx),), (), None, ())
    ServiceManager._op_shutdown = IcePy.Operation('shutdown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())

    _M_IceBox.ServiceManager = ServiceManager
    del ServiceManager

    _M_IceBox.ServiceManagerPrx = ServiceManagerPrx
    del ServiceManagerPrx

# End of module IceBox

Ice.sliceChecksums["::IceBox::AlreadyStartedException"] = "d5b097af3221b37482d5f175502abf62"
Ice.sliceChecksums["::IceBox::AlreadyStoppedException"] = "281d493a84d674b3a4335d6afc2c16"
Ice.sliceChecksums["::IceBox::NoSuchServiceException"] = "5957f1c582d9aebad557cbdb7820d4"
Ice.sliceChecksums["::IceBox::ServiceManager"] = "df3a42670c3ce4ef67d6125a5d04d4c"
Ice.sliceChecksums["::IceBox::ServiceObserver"] = "f657781cda7438532a6c33e95988479c"
