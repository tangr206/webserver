# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `LocalException.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_Identity_ice
import Ice_BuiltinSequences_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('InitializationException'):
    _M_Ice.InitializationException = Ice.createTempClass()
    class InitializationException(Ice.LocalException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'Ice::InitializationException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_InitializationException = IcePy.defineException('::Ice::InitializationException', InitializationException, (), None, (('reason', (), IcePy._t_string),))
    InitializationException.ice_type = _M_Ice._t_InitializationException

    _M_Ice.InitializationException = InitializationException
    del InitializationException

if not _M_Ice.__dict__.has_key('PluginInitializationException'):
    _M_Ice.PluginInitializationException = Ice.createTempClass()
    class PluginInitializationException(Ice.LocalException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'Ice::PluginInitializationException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_PluginInitializationException = IcePy.defineException('::Ice::PluginInitializationException', PluginInitializationException, (), None, (('reason', (), IcePy._t_string),))
    PluginInitializationException.ice_type = _M_Ice._t_PluginInitializationException

    _M_Ice.PluginInitializationException = PluginInitializationException
    del PluginInitializationException

if not _M_Ice.__dict__.has_key('CollocationOptimizationException'):
    _M_Ice.CollocationOptimizationException = Ice.createTempClass()
    class CollocationOptimizationException(Ice.LocalException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::CollocationOptimizationException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_CollocationOptimizationException = IcePy.defineException('::Ice::CollocationOptimizationException', CollocationOptimizationException, (), None, ())
    CollocationOptimizationException.ice_type = _M_Ice._t_CollocationOptimizationException

    _M_Ice.CollocationOptimizationException = CollocationOptimizationException
    del CollocationOptimizationException

if not _M_Ice.__dict__.has_key('AlreadyRegisteredException'):
    _M_Ice.AlreadyRegisteredException = Ice.createTempClass()
    class AlreadyRegisteredException(Ice.LocalException):
        def __init__(self, kindOfObject='', id=''):
            self.kindOfObject = kindOfObject
            self.id = id

        def ice_name(self):
            return 'Ice::AlreadyRegisteredException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_AlreadyRegisteredException = IcePy.defineException('::Ice::AlreadyRegisteredException', AlreadyRegisteredException, (), None, (
        ('kindOfObject', (), IcePy._t_string),
        ('id', (), IcePy._t_string)
    ))
    AlreadyRegisteredException.ice_type = _M_Ice._t_AlreadyRegisteredException

    _M_Ice.AlreadyRegisteredException = AlreadyRegisteredException
    del AlreadyRegisteredException

if not _M_Ice.__dict__.has_key('NotRegisteredException'):
    _M_Ice.NotRegisteredException = Ice.createTempClass()
    class NotRegisteredException(Ice.LocalException):
        def __init__(self, kindOfObject='', id=''):
            self.kindOfObject = kindOfObject
            self.id = id

        def ice_name(self):
            return 'Ice::NotRegisteredException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_NotRegisteredException = IcePy.defineException('::Ice::NotRegisteredException', NotRegisteredException, (), None, (
        ('kindOfObject', (), IcePy._t_string),
        ('id', (), IcePy._t_string)
    ))
    NotRegisteredException.ice_type = _M_Ice._t_NotRegisteredException

    _M_Ice.NotRegisteredException = NotRegisteredException
    del NotRegisteredException

if not _M_Ice.__dict__.has_key('TwowayOnlyException'):
    _M_Ice.TwowayOnlyException = Ice.createTempClass()
    class TwowayOnlyException(Ice.LocalException):
        def __init__(self, operation=''):
            self.operation = operation

        def ice_name(self):
            return 'Ice::TwowayOnlyException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_TwowayOnlyException = IcePy.defineException('::Ice::TwowayOnlyException', TwowayOnlyException, (), None, (('operation', (), IcePy._t_string),))
    TwowayOnlyException.ice_type = _M_Ice._t_TwowayOnlyException

    _M_Ice.TwowayOnlyException = TwowayOnlyException
    del TwowayOnlyException

if not _M_Ice.__dict__.has_key('CloneNotImplementedException'):
    _M_Ice.CloneNotImplementedException = Ice.createTempClass()
    class CloneNotImplementedException(Ice.LocalException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::CloneNotImplementedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_CloneNotImplementedException = IcePy.defineException('::Ice::CloneNotImplementedException', CloneNotImplementedException, (), None, ())
    CloneNotImplementedException.ice_type = _M_Ice._t_CloneNotImplementedException

    _M_Ice.CloneNotImplementedException = CloneNotImplementedException
    del CloneNotImplementedException

if not _M_Ice.__dict__.has_key('UnknownException'):
    _M_Ice.UnknownException = Ice.createTempClass()
    class UnknownException(Ice.LocalException):
        def __init__(self, unknown=''):
            self.unknown = unknown

        def ice_name(self):
            return 'Ice::UnknownException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_UnknownException = IcePy.defineException('::Ice::UnknownException', UnknownException, (), None, (('unknown', (), IcePy._t_string),))
    UnknownException.ice_type = _M_Ice._t_UnknownException

    _M_Ice.UnknownException = UnknownException
    del UnknownException

if not _M_Ice.__dict__.has_key('UnknownLocalException'):
    _M_Ice.UnknownLocalException = Ice.createTempClass()
    class UnknownLocalException(_M_Ice.UnknownException):
        def __init__(self, unknown=''):
            _M_Ice.UnknownException.__init__(self, unknown)

        def ice_name(self):
            return 'Ice::UnknownLocalException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_UnknownLocalException = IcePy.defineException('::Ice::UnknownLocalException', UnknownLocalException, (), _M_Ice._t_UnknownException, ())
    UnknownLocalException.ice_type = _M_Ice._t_UnknownLocalException

    _M_Ice.UnknownLocalException = UnknownLocalException
    del UnknownLocalException

if not _M_Ice.__dict__.has_key('UnknownUserException'):
    _M_Ice.UnknownUserException = Ice.createTempClass()
    class UnknownUserException(_M_Ice.UnknownException):
        def __init__(self, unknown=''):
            _M_Ice.UnknownException.__init__(self, unknown)

        def ice_name(self):
            return 'Ice::UnknownUserException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_UnknownUserException = IcePy.defineException('::Ice::UnknownUserException', UnknownUserException, (), _M_Ice._t_UnknownException, ())
    UnknownUserException.ice_type = _M_Ice._t_UnknownUserException

    _M_Ice.UnknownUserException = UnknownUserException
    del UnknownUserException

if not _M_Ice.__dict__.has_key('VersionMismatchException'):
    _M_Ice.VersionMismatchException = Ice.createTempClass()
    class VersionMismatchException(Ice.LocalException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::VersionMismatchException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_VersionMismatchException = IcePy.defineException('::Ice::VersionMismatchException', VersionMismatchException, (), None, ())
    VersionMismatchException.ice_type = _M_Ice._t_VersionMismatchException

    _M_Ice.VersionMismatchException = VersionMismatchException
    del VersionMismatchException

if not _M_Ice.__dict__.has_key('CommunicatorDestroyedException'):
    _M_Ice.CommunicatorDestroyedException = Ice.createTempClass()
    class CommunicatorDestroyedException(Ice.LocalException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::CommunicatorDestroyedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_CommunicatorDestroyedException = IcePy.defineException('::Ice::CommunicatorDestroyedException', CommunicatorDestroyedException, (), None, ())
    CommunicatorDestroyedException.ice_type = _M_Ice._t_CommunicatorDestroyedException

    _M_Ice.CommunicatorDestroyedException = CommunicatorDestroyedException
    del CommunicatorDestroyedException

if not _M_Ice.__dict__.has_key('ObjectAdapterDeactivatedException'):
    _M_Ice.ObjectAdapterDeactivatedException = Ice.createTempClass()
    class ObjectAdapterDeactivatedException(Ice.LocalException):
        def __init__(self, name=''):
            self.name = name

        def ice_name(self):
            return 'Ice::ObjectAdapterDeactivatedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ObjectAdapterDeactivatedException = IcePy.defineException('::Ice::ObjectAdapterDeactivatedException', ObjectAdapterDeactivatedException, (), None, (('name', (), IcePy._t_string),))
    ObjectAdapterDeactivatedException.ice_type = _M_Ice._t_ObjectAdapterDeactivatedException

    _M_Ice.ObjectAdapterDeactivatedException = ObjectAdapterDeactivatedException
    del ObjectAdapterDeactivatedException

if not _M_Ice.__dict__.has_key('ObjectAdapterIdInUseException'):
    _M_Ice.ObjectAdapterIdInUseException = Ice.createTempClass()
    class ObjectAdapterIdInUseException(Ice.LocalException):
        def __init__(self, id=''):
            self.id = id

        def ice_name(self):
            return 'Ice::ObjectAdapterIdInUseException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ObjectAdapterIdInUseException = IcePy.defineException('::Ice::ObjectAdapterIdInUseException', ObjectAdapterIdInUseException, (), None, (('id', (), IcePy._t_string),))
    ObjectAdapterIdInUseException.ice_type = _M_Ice._t_ObjectAdapterIdInUseException

    _M_Ice.ObjectAdapterIdInUseException = ObjectAdapterIdInUseException
    del ObjectAdapterIdInUseException

if not _M_Ice.__dict__.has_key('NoEndpointException'):
    _M_Ice.NoEndpointException = Ice.createTempClass()
    class NoEndpointException(Ice.LocalException):
        def __init__(self, proxy=''):
            self.proxy = proxy

        def ice_name(self):
            return 'Ice::NoEndpointException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_NoEndpointException = IcePy.defineException('::Ice::NoEndpointException', NoEndpointException, (), None, (('proxy', (), IcePy._t_string),))
    NoEndpointException.ice_type = _M_Ice._t_NoEndpointException

    _M_Ice.NoEndpointException = NoEndpointException
    del NoEndpointException

if not _M_Ice.__dict__.has_key('EndpointParseException'):
    _M_Ice.EndpointParseException = Ice.createTempClass()
    class EndpointParseException(Ice.LocalException):
        def __init__(self, str=''):
            self.str = str

        def ice_name(self):
            return 'Ice::EndpointParseException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_EndpointParseException = IcePy.defineException('::Ice::EndpointParseException', EndpointParseException, (), None, (('str', (), IcePy._t_string),))
    EndpointParseException.ice_type = _M_Ice._t_EndpointParseException

    _M_Ice.EndpointParseException = EndpointParseException
    del EndpointParseException

if not _M_Ice.__dict__.has_key('EndpointSelectionTypeParseException'):
    _M_Ice.EndpointSelectionTypeParseException = Ice.createTempClass()
    class EndpointSelectionTypeParseException(Ice.LocalException):
        def __init__(self, str=''):
            self.str = str

        def ice_name(self):
            return 'Ice::EndpointSelectionTypeParseException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_EndpointSelectionTypeParseException = IcePy.defineException('::Ice::EndpointSelectionTypeParseException', EndpointSelectionTypeParseException, (), None, (('str', (), IcePy._t_string),))
    EndpointSelectionTypeParseException.ice_type = _M_Ice._t_EndpointSelectionTypeParseException

    _M_Ice.EndpointSelectionTypeParseException = EndpointSelectionTypeParseException
    del EndpointSelectionTypeParseException

if not _M_Ice.__dict__.has_key('IdentityParseException'):
    _M_Ice.IdentityParseException = Ice.createTempClass()
    class IdentityParseException(Ice.LocalException):
        def __init__(self, str=''):
            self.str = str

        def ice_name(self):
            return 'Ice::IdentityParseException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_IdentityParseException = IcePy.defineException('::Ice::IdentityParseException', IdentityParseException, (), None, (('str', (), IcePy._t_string),))
    IdentityParseException.ice_type = _M_Ice._t_IdentityParseException

    _M_Ice.IdentityParseException = IdentityParseException
    del IdentityParseException

if not _M_Ice.__dict__.has_key('ProxyParseException'):
    _M_Ice.ProxyParseException = Ice.createTempClass()
    class ProxyParseException(Ice.LocalException):
        def __init__(self, str=''):
            self.str = str

        def ice_name(self):
            return 'Ice::ProxyParseException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ProxyParseException = IcePy.defineException('::Ice::ProxyParseException', ProxyParseException, (), None, (('str', (), IcePy._t_string),))
    ProxyParseException.ice_type = _M_Ice._t_ProxyParseException

    _M_Ice.ProxyParseException = ProxyParseException
    del ProxyParseException

if not _M_Ice.__dict__.has_key('IllegalIdentityException'):
    _M_Ice.IllegalIdentityException = Ice.createTempClass()
    class IllegalIdentityException(Ice.LocalException):
        def __init__(self, id=Ice._struct_marker):
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id

        def ice_name(self):
            return 'Ice::IllegalIdentityException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_IllegalIdentityException = IcePy.defineException('::Ice::IllegalIdentityException', IllegalIdentityException, (), None, (('id', (), _M_Ice._t_Identity),))
    IllegalIdentityException.ice_type = _M_Ice._t_IllegalIdentityException

    _M_Ice.IllegalIdentityException = IllegalIdentityException
    del IllegalIdentityException

if not _M_Ice.__dict__.has_key('RequestFailedException'):
    _M_Ice.RequestFailedException = Ice.createTempClass()
    class RequestFailedException(Ice.LocalException):
        def __init__(self, id=Ice._struct_marker, facet='', operation=''):
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id
            self.facet = facet
            self.operation = operation

        def ice_name(self):
            return 'Ice::RequestFailedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_RequestFailedException = IcePy.defineException('::Ice::RequestFailedException', RequestFailedException, (), None, (
        ('id', (), _M_Ice._t_Identity),
        ('facet', (), IcePy._t_string),
        ('operation', (), IcePy._t_string)
    ))
    RequestFailedException.ice_type = _M_Ice._t_RequestFailedException

    _M_Ice.RequestFailedException = RequestFailedException
    del RequestFailedException

if not _M_Ice.__dict__.has_key('ObjectNotExistException'):
    _M_Ice.ObjectNotExistException = Ice.createTempClass()
    class ObjectNotExistException(_M_Ice.RequestFailedException):
        def __init__(self, id=Ice._struct_marker, facet='', operation=''):
            _M_Ice.RequestFailedException.__init__(self, id, facet, operation)

        def ice_name(self):
            return 'Ice::ObjectNotExistException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ObjectNotExistException = IcePy.defineException('::Ice::ObjectNotExistException', ObjectNotExistException, (), _M_Ice._t_RequestFailedException, ())
    ObjectNotExistException.ice_type = _M_Ice._t_ObjectNotExistException

    _M_Ice.ObjectNotExistException = ObjectNotExistException
    del ObjectNotExistException

if not _M_Ice.__dict__.has_key('FacetNotExistException'):
    _M_Ice.FacetNotExistException = Ice.createTempClass()
    class FacetNotExistException(_M_Ice.RequestFailedException):
        def __init__(self, id=Ice._struct_marker, facet='', operation=''):
            _M_Ice.RequestFailedException.__init__(self, id, facet, operation)

        def ice_name(self):
            return 'Ice::FacetNotExistException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_FacetNotExistException = IcePy.defineException('::Ice::FacetNotExistException', FacetNotExistException, (), _M_Ice._t_RequestFailedException, ())
    FacetNotExistException.ice_type = _M_Ice._t_FacetNotExistException

    _M_Ice.FacetNotExistException = FacetNotExistException
    del FacetNotExistException

if not _M_Ice.__dict__.has_key('OperationNotExistException'):
    _M_Ice.OperationNotExistException = Ice.createTempClass()
    class OperationNotExistException(_M_Ice.RequestFailedException):
        def __init__(self, id=Ice._struct_marker, facet='', operation=''):
            _M_Ice.RequestFailedException.__init__(self, id, facet, operation)

        def ice_name(self):
            return 'Ice::OperationNotExistException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_OperationNotExistException = IcePy.defineException('::Ice::OperationNotExistException', OperationNotExistException, (), _M_Ice._t_RequestFailedException, ())
    OperationNotExistException.ice_type = _M_Ice._t_OperationNotExistException

    _M_Ice.OperationNotExistException = OperationNotExistException
    del OperationNotExistException

if not _M_Ice.__dict__.has_key('SyscallException'):
    _M_Ice.SyscallException = Ice.createTempClass()
    class SyscallException(Ice.LocalException):
        def __init__(self, error=0):
            self.error = error

        def ice_name(self):
            return 'Ice::SyscallException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_SyscallException = IcePy.defineException('::Ice::SyscallException', SyscallException, (), None, (('error', (), IcePy._t_int),))
    SyscallException.ice_type = _M_Ice._t_SyscallException

    _M_Ice.SyscallException = SyscallException
    del SyscallException

if not _M_Ice.__dict__.has_key('SocketException'):
    _M_Ice.SocketException = Ice.createTempClass()
    class SocketException(_M_Ice.SyscallException):
        def __init__(self, error=0):
            _M_Ice.SyscallException.__init__(self, error)

        def ice_name(self):
            return 'Ice::SocketException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_SocketException = IcePy.defineException('::Ice::SocketException', SocketException, (), _M_Ice._t_SyscallException, ())
    SocketException.ice_type = _M_Ice._t_SocketException

    _M_Ice.SocketException = SocketException
    del SocketException

if not _M_Ice.__dict__.has_key('FileException'):
    _M_Ice.FileException = Ice.createTempClass()
    class FileException(_M_Ice.SyscallException):
        def __init__(self, error=0, path=''):
            _M_Ice.SyscallException.__init__(self, error)
            self.path = path

        def ice_name(self):
            return 'Ice::FileException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_FileException = IcePy.defineException('::Ice::FileException', FileException, (), _M_Ice._t_SyscallException, (('path', (), IcePy._t_string),))
    FileException.ice_type = _M_Ice._t_FileException

    _M_Ice.FileException = FileException
    del FileException

if not _M_Ice.__dict__.has_key('ConnectFailedException'):
    _M_Ice.ConnectFailedException = Ice.createTempClass()
    class ConnectFailedException(_M_Ice.SocketException):
        def __init__(self, error=0):
            _M_Ice.SocketException.__init__(self, error)

        def ice_name(self):
            return 'Ice::ConnectFailedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ConnectFailedException = IcePy.defineException('::Ice::ConnectFailedException', ConnectFailedException, (), _M_Ice._t_SocketException, ())
    ConnectFailedException.ice_type = _M_Ice._t_ConnectFailedException

    _M_Ice.ConnectFailedException = ConnectFailedException
    del ConnectFailedException

if not _M_Ice.__dict__.has_key('ConnectionRefusedException'):
    _M_Ice.ConnectionRefusedException = Ice.createTempClass()
    class ConnectionRefusedException(_M_Ice.ConnectFailedException):
        def __init__(self, error=0):
            _M_Ice.ConnectFailedException.__init__(self, error)

        def ice_name(self):
            return 'Ice::ConnectionRefusedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ConnectionRefusedException = IcePy.defineException('::Ice::ConnectionRefusedException', ConnectionRefusedException, (), _M_Ice._t_ConnectFailedException, ())
    ConnectionRefusedException.ice_type = _M_Ice._t_ConnectionRefusedException

    _M_Ice.ConnectionRefusedException = ConnectionRefusedException
    del ConnectionRefusedException

if not _M_Ice.__dict__.has_key('ConnectionLostException'):
    _M_Ice.ConnectionLostException = Ice.createTempClass()
    class ConnectionLostException(_M_Ice.SocketException):
        def __init__(self, error=0):
            _M_Ice.SocketException.__init__(self, error)

        def ice_name(self):
            return 'Ice::ConnectionLostException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ConnectionLostException = IcePy.defineException('::Ice::ConnectionLostException', ConnectionLostException, (), _M_Ice._t_SocketException, ())
    ConnectionLostException.ice_type = _M_Ice._t_ConnectionLostException

    _M_Ice.ConnectionLostException = ConnectionLostException
    del ConnectionLostException

if not _M_Ice.__dict__.has_key('DNSException'):
    _M_Ice.DNSException = Ice.createTempClass()
    class DNSException(Ice.LocalException):
        def __init__(self, error=0, host=''):
            self.error = error
            self.host = host

        def ice_name(self):
            return 'Ice::DNSException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_DNSException = IcePy.defineException('::Ice::DNSException', DNSException, (), None, (
        ('error', (), IcePy._t_int),
        ('host', (), IcePy._t_string)
    ))
    DNSException.ice_type = _M_Ice._t_DNSException

    _M_Ice.DNSException = DNSException
    del DNSException

if not _M_Ice.__dict__.has_key('TimeoutException'):
    _M_Ice.TimeoutException = Ice.createTempClass()
    class TimeoutException(Ice.LocalException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::TimeoutException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_TimeoutException = IcePy.defineException('::Ice::TimeoutException', TimeoutException, (), None, ())
    TimeoutException.ice_type = _M_Ice._t_TimeoutException

    _M_Ice.TimeoutException = TimeoutException
    del TimeoutException

if not _M_Ice.__dict__.has_key('ConnectTimeoutException'):
    _M_Ice.ConnectTimeoutException = Ice.createTempClass()
    class ConnectTimeoutException(_M_Ice.TimeoutException):
        def __init__(self):
            _M_Ice.TimeoutException.__init__(self)

        def ice_name(self):
            return 'Ice::ConnectTimeoutException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ConnectTimeoutException = IcePy.defineException('::Ice::ConnectTimeoutException', ConnectTimeoutException, (), _M_Ice._t_TimeoutException, ())
    ConnectTimeoutException.ice_type = _M_Ice._t_ConnectTimeoutException

    _M_Ice.ConnectTimeoutException = ConnectTimeoutException
    del ConnectTimeoutException

if not _M_Ice.__dict__.has_key('CloseTimeoutException'):
    _M_Ice.CloseTimeoutException = Ice.createTempClass()
    class CloseTimeoutException(_M_Ice.TimeoutException):
        def __init__(self):
            _M_Ice.TimeoutException.__init__(self)

        def ice_name(self):
            return 'Ice::CloseTimeoutException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_CloseTimeoutException = IcePy.defineException('::Ice::CloseTimeoutException', CloseTimeoutException, (), _M_Ice._t_TimeoutException, ())
    CloseTimeoutException.ice_type = _M_Ice._t_CloseTimeoutException

    _M_Ice.CloseTimeoutException = CloseTimeoutException
    del CloseTimeoutException

if not _M_Ice.__dict__.has_key('ConnectionTimeoutException'):
    _M_Ice.ConnectionTimeoutException = Ice.createTempClass()
    class ConnectionTimeoutException(_M_Ice.TimeoutException):
        def __init__(self):
            _M_Ice.TimeoutException.__init__(self)

        def ice_name(self):
            return 'Ice::ConnectionTimeoutException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ConnectionTimeoutException = IcePy.defineException('::Ice::ConnectionTimeoutException', ConnectionTimeoutException, (), _M_Ice._t_TimeoutException, ())
    ConnectionTimeoutException.ice_type = _M_Ice._t_ConnectionTimeoutException

    _M_Ice.ConnectionTimeoutException = ConnectionTimeoutException
    del ConnectionTimeoutException

if not _M_Ice.__dict__.has_key('ProtocolException'):
    _M_Ice.ProtocolException = Ice.createTempClass()
    class ProtocolException(Ice.LocalException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'Ice::ProtocolException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ProtocolException = IcePy.defineException('::Ice::ProtocolException', ProtocolException, (), None, (('reason', (), IcePy._t_string),))
    ProtocolException.ice_type = _M_Ice._t_ProtocolException

    _M_Ice.ProtocolException = ProtocolException
    del ProtocolException

if not _M_Ice.__dict__.has_key('BadMagicException'):
    _M_Ice.BadMagicException = Ice.createTempClass()
    class BadMagicException(_M_Ice.ProtocolException):
        def __init__(self, reason='', badMagic=None):
            _M_Ice.ProtocolException.__init__(self, reason)
            self.badMagic = badMagic

        def ice_name(self):
            return 'Ice::BadMagicException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_BadMagicException = IcePy.defineException('::Ice::BadMagicException', BadMagicException, (), _M_Ice._t_ProtocolException, (('badMagic', (), _M_Ice._t_ByteSeq),))
    BadMagicException.ice_type = _M_Ice._t_BadMagicException

    _M_Ice.BadMagicException = BadMagicException
    del BadMagicException

if not _M_Ice.__dict__.has_key('UnsupportedProtocolException'):
    _M_Ice.UnsupportedProtocolException = Ice.createTempClass()
    class UnsupportedProtocolException(_M_Ice.ProtocolException):
        def __init__(self, reason='', badMajor=0, badMinor=0, major=0, minor=0):
            _M_Ice.ProtocolException.__init__(self, reason)
            self.badMajor = badMajor
            self.badMinor = badMinor
            self.major = major
            self.minor = minor

        def ice_name(self):
            return 'Ice::UnsupportedProtocolException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_UnsupportedProtocolException = IcePy.defineException('::Ice::UnsupportedProtocolException', UnsupportedProtocolException, (), _M_Ice._t_ProtocolException, (
        ('badMajor', (), IcePy._t_int),
        ('badMinor', (), IcePy._t_int),
        ('major', (), IcePy._t_int),
        ('minor', (), IcePy._t_int)
    ))
    UnsupportedProtocolException.ice_type = _M_Ice._t_UnsupportedProtocolException

    _M_Ice.UnsupportedProtocolException = UnsupportedProtocolException
    del UnsupportedProtocolException

if not _M_Ice.__dict__.has_key('UnsupportedEncodingException'):
    _M_Ice.UnsupportedEncodingException = Ice.createTempClass()
    class UnsupportedEncodingException(_M_Ice.ProtocolException):
        def __init__(self, reason='', badMajor=0, badMinor=0, major=0, minor=0):
            _M_Ice.ProtocolException.__init__(self, reason)
            self.badMajor = badMajor
            self.badMinor = badMinor
            self.major = major
            self.minor = minor

        def ice_name(self):
            return 'Ice::UnsupportedEncodingException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_UnsupportedEncodingException = IcePy.defineException('::Ice::UnsupportedEncodingException', UnsupportedEncodingException, (), _M_Ice._t_ProtocolException, (
        ('badMajor', (), IcePy._t_int),
        ('badMinor', (), IcePy._t_int),
        ('major', (), IcePy._t_int),
        ('minor', (), IcePy._t_int)
    ))
    UnsupportedEncodingException.ice_type = _M_Ice._t_UnsupportedEncodingException

    _M_Ice.UnsupportedEncodingException = UnsupportedEncodingException
    del UnsupportedEncodingException

if not _M_Ice.__dict__.has_key('UnknownMessageException'):
    _M_Ice.UnknownMessageException = Ice.createTempClass()
    class UnknownMessageException(_M_Ice.ProtocolException):
        def __init__(self, reason=''):
            _M_Ice.ProtocolException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::UnknownMessageException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_UnknownMessageException = IcePy.defineException('::Ice::UnknownMessageException', UnknownMessageException, (), _M_Ice._t_ProtocolException, ())
    UnknownMessageException.ice_type = _M_Ice._t_UnknownMessageException

    _M_Ice.UnknownMessageException = UnknownMessageException
    del UnknownMessageException

if not _M_Ice.__dict__.has_key('ConnectionNotValidatedException'):
    _M_Ice.ConnectionNotValidatedException = Ice.createTempClass()
    class ConnectionNotValidatedException(_M_Ice.ProtocolException):
        def __init__(self, reason=''):
            _M_Ice.ProtocolException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::ConnectionNotValidatedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ConnectionNotValidatedException = IcePy.defineException('::Ice::ConnectionNotValidatedException', ConnectionNotValidatedException, (), _M_Ice._t_ProtocolException, ())
    ConnectionNotValidatedException.ice_type = _M_Ice._t_ConnectionNotValidatedException

    _M_Ice.ConnectionNotValidatedException = ConnectionNotValidatedException
    del ConnectionNotValidatedException

if not _M_Ice.__dict__.has_key('UnknownRequestIdException'):
    _M_Ice.UnknownRequestIdException = Ice.createTempClass()
    class UnknownRequestIdException(_M_Ice.ProtocolException):
        def __init__(self, reason=''):
            _M_Ice.ProtocolException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::UnknownRequestIdException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_UnknownRequestIdException = IcePy.defineException('::Ice::UnknownRequestIdException', UnknownRequestIdException, (), _M_Ice._t_ProtocolException, ())
    UnknownRequestIdException.ice_type = _M_Ice._t_UnknownRequestIdException

    _M_Ice.UnknownRequestIdException = UnknownRequestIdException
    del UnknownRequestIdException

if not _M_Ice.__dict__.has_key('UnknownReplyStatusException'):
    _M_Ice.UnknownReplyStatusException = Ice.createTempClass()
    class UnknownReplyStatusException(_M_Ice.ProtocolException):
        def __init__(self, reason=''):
            _M_Ice.ProtocolException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::UnknownReplyStatusException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_UnknownReplyStatusException = IcePy.defineException('::Ice::UnknownReplyStatusException', UnknownReplyStatusException, (), _M_Ice._t_ProtocolException, ())
    UnknownReplyStatusException.ice_type = _M_Ice._t_UnknownReplyStatusException

    _M_Ice.UnknownReplyStatusException = UnknownReplyStatusException
    del UnknownReplyStatusException

if not _M_Ice.__dict__.has_key('CloseConnectionException'):
    _M_Ice.CloseConnectionException = Ice.createTempClass()
    class CloseConnectionException(_M_Ice.ProtocolException):
        def __init__(self, reason=''):
            _M_Ice.ProtocolException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::CloseConnectionException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_CloseConnectionException = IcePy.defineException('::Ice::CloseConnectionException', CloseConnectionException, (), _M_Ice._t_ProtocolException, ())
    CloseConnectionException.ice_type = _M_Ice._t_CloseConnectionException

    _M_Ice.CloseConnectionException = CloseConnectionException
    del CloseConnectionException

if not _M_Ice.__dict__.has_key('ForcedCloseConnectionException'):
    _M_Ice.ForcedCloseConnectionException = Ice.createTempClass()
    class ForcedCloseConnectionException(_M_Ice.ProtocolException):
        def __init__(self, reason=''):
            _M_Ice.ProtocolException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::ForcedCloseConnectionException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ForcedCloseConnectionException = IcePy.defineException('::Ice::ForcedCloseConnectionException', ForcedCloseConnectionException, (), _M_Ice._t_ProtocolException, ())
    ForcedCloseConnectionException.ice_type = _M_Ice._t_ForcedCloseConnectionException

    _M_Ice.ForcedCloseConnectionException = ForcedCloseConnectionException
    del ForcedCloseConnectionException

if not _M_Ice.__dict__.has_key('IllegalMessageSizeException'):
    _M_Ice.IllegalMessageSizeException = Ice.createTempClass()
    class IllegalMessageSizeException(_M_Ice.ProtocolException):
        def __init__(self, reason=''):
            _M_Ice.ProtocolException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::IllegalMessageSizeException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_IllegalMessageSizeException = IcePy.defineException('::Ice::IllegalMessageSizeException', IllegalMessageSizeException, (), _M_Ice._t_ProtocolException, ())
    IllegalMessageSizeException.ice_type = _M_Ice._t_IllegalMessageSizeException

    _M_Ice.IllegalMessageSizeException = IllegalMessageSizeException
    del IllegalMessageSizeException

if not _M_Ice.__dict__.has_key('CompressionException'):
    _M_Ice.CompressionException = Ice.createTempClass()
    class CompressionException(_M_Ice.ProtocolException):
        def __init__(self, reason=''):
            _M_Ice.ProtocolException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::CompressionException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_CompressionException = IcePy.defineException('::Ice::CompressionException', CompressionException, (), _M_Ice._t_ProtocolException, ())
    CompressionException.ice_type = _M_Ice._t_CompressionException

    _M_Ice.CompressionException = CompressionException
    del CompressionException

if not _M_Ice.__dict__.has_key('DatagramLimitException'):
    _M_Ice.DatagramLimitException = Ice.createTempClass()
    class DatagramLimitException(_M_Ice.ProtocolException):
        def __init__(self, reason=''):
            _M_Ice.ProtocolException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::DatagramLimitException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_DatagramLimitException = IcePy.defineException('::Ice::DatagramLimitException', DatagramLimitException, (), _M_Ice._t_ProtocolException, ())
    DatagramLimitException.ice_type = _M_Ice._t_DatagramLimitException

    _M_Ice.DatagramLimitException = DatagramLimitException
    del DatagramLimitException

if not _M_Ice.__dict__.has_key('MarshalException'):
    _M_Ice.MarshalException = Ice.createTempClass()
    class MarshalException(_M_Ice.ProtocolException):
        def __init__(self, reason=''):
            _M_Ice.ProtocolException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::MarshalException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_MarshalException = IcePy.defineException('::Ice::MarshalException', MarshalException, (), _M_Ice._t_ProtocolException, ())
    MarshalException.ice_type = _M_Ice._t_MarshalException

    _M_Ice.MarshalException = MarshalException
    del MarshalException

if not _M_Ice.__dict__.has_key('ProxyUnmarshalException'):
    _M_Ice.ProxyUnmarshalException = Ice.createTempClass()
    class ProxyUnmarshalException(_M_Ice.MarshalException):
        def __init__(self, reason=''):
            _M_Ice.MarshalException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::ProxyUnmarshalException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ProxyUnmarshalException = IcePy.defineException('::Ice::ProxyUnmarshalException', ProxyUnmarshalException, (), _M_Ice._t_MarshalException, ())
    ProxyUnmarshalException.ice_type = _M_Ice._t_ProxyUnmarshalException

    _M_Ice.ProxyUnmarshalException = ProxyUnmarshalException
    del ProxyUnmarshalException

if not _M_Ice.__dict__.has_key('UnmarshalOutOfBoundsException'):
    _M_Ice.UnmarshalOutOfBoundsException = Ice.createTempClass()
    class UnmarshalOutOfBoundsException(_M_Ice.MarshalException):
        def __init__(self, reason=''):
            _M_Ice.MarshalException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::UnmarshalOutOfBoundsException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_UnmarshalOutOfBoundsException = IcePy.defineException('::Ice::UnmarshalOutOfBoundsException', UnmarshalOutOfBoundsException, (), _M_Ice._t_MarshalException, ())
    UnmarshalOutOfBoundsException.ice_type = _M_Ice._t_UnmarshalOutOfBoundsException

    _M_Ice.UnmarshalOutOfBoundsException = UnmarshalOutOfBoundsException
    del UnmarshalOutOfBoundsException

if not _M_Ice.__dict__.has_key('IllegalIndirectionException'):
    _M_Ice.IllegalIndirectionException = Ice.createTempClass()
    class IllegalIndirectionException(_M_Ice.MarshalException):
        def __init__(self, reason=''):
            _M_Ice.MarshalException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::IllegalIndirectionException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_IllegalIndirectionException = IcePy.defineException('::Ice::IllegalIndirectionException', IllegalIndirectionException, (), _M_Ice._t_MarshalException, ())
    IllegalIndirectionException.ice_type = _M_Ice._t_IllegalIndirectionException

    _M_Ice.IllegalIndirectionException = IllegalIndirectionException
    del IllegalIndirectionException

if not _M_Ice.__dict__.has_key('NoObjectFactoryException'):
    _M_Ice.NoObjectFactoryException = Ice.createTempClass()
    class NoObjectFactoryException(_M_Ice.MarshalException):
        def __init__(self, reason='', type=''):
            _M_Ice.MarshalException.__init__(self, reason)
            self.type = type

        def ice_name(self):
            return 'Ice::NoObjectFactoryException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_NoObjectFactoryException = IcePy.defineException('::Ice::NoObjectFactoryException', NoObjectFactoryException, (), _M_Ice._t_MarshalException, (('type', (), IcePy._t_string),))
    NoObjectFactoryException.ice_type = _M_Ice._t_NoObjectFactoryException

    _M_Ice.NoObjectFactoryException = NoObjectFactoryException
    del NoObjectFactoryException

if not _M_Ice.__dict__.has_key('UnexpectedObjectException'):
    _M_Ice.UnexpectedObjectException = Ice.createTempClass()
    class UnexpectedObjectException(_M_Ice.MarshalException):
        def __init__(self, reason='', type='', expectedType=''):
            _M_Ice.MarshalException.__init__(self, reason)
            self.type = type
            self.expectedType = expectedType

        def ice_name(self):
            return 'Ice::UnexpectedObjectException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_UnexpectedObjectException = IcePy.defineException('::Ice::UnexpectedObjectException', UnexpectedObjectException, (), _M_Ice._t_MarshalException, (
        ('type', (), IcePy._t_string),
        ('expectedType', (), IcePy._t_string)
    ))
    UnexpectedObjectException.ice_type = _M_Ice._t_UnexpectedObjectException

    _M_Ice.UnexpectedObjectException = UnexpectedObjectException
    del UnexpectedObjectException

if not _M_Ice.__dict__.has_key('MemoryLimitException'):
    _M_Ice.MemoryLimitException = Ice.createTempClass()
    class MemoryLimitException(_M_Ice.MarshalException):
        def __init__(self, reason=''):
            _M_Ice.MarshalException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::MemoryLimitException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_MemoryLimitException = IcePy.defineException('::Ice::MemoryLimitException', MemoryLimitException, (), _M_Ice._t_MarshalException, ())
    MemoryLimitException.ice_type = _M_Ice._t_MemoryLimitException

    _M_Ice.MemoryLimitException = MemoryLimitException
    del MemoryLimitException

if not _M_Ice.__dict__.has_key('StringConversionException'):
    _M_Ice.StringConversionException = Ice.createTempClass()
    class StringConversionException(_M_Ice.MarshalException):
        def __init__(self, reason=''):
            _M_Ice.MarshalException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::StringConversionException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_StringConversionException = IcePy.defineException('::Ice::StringConversionException', StringConversionException, (), _M_Ice._t_MarshalException, ())
    StringConversionException.ice_type = _M_Ice._t_StringConversionException

    _M_Ice.StringConversionException = StringConversionException
    del StringConversionException

if not _M_Ice.__dict__.has_key('EncapsulationException'):
    _M_Ice.EncapsulationException = Ice.createTempClass()
    class EncapsulationException(_M_Ice.MarshalException):
        def __init__(self, reason=''):
            _M_Ice.MarshalException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::EncapsulationException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_EncapsulationException = IcePy.defineException('::Ice::EncapsulationException', EncapsulationException, (), _M_Ice._t_MarshalException, ())
    EncapsulationException.ice_type = _M_Ice._t_EncapsulationException

    _M_Ice.EncapsulationException = EncapsulationException
    del EncapsulationException

if not _M_Ice.__dict__.has_key('NegativeSizeException'):
    _M_Ice.NegativeSizeException = Ice.createTempClass()
    class NegativeSizeException(_M_Ice.MarshalException):
        def __init__(self, reason=''):
            _M_Ice.MarshalException.__init__(self, reason)

        def ice_name(self):
            return 'Ice::NegativeSizeException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_NegativeSizeException = IcePy.defineException('::Ice::NegativeSizeException', NegativeSizeException, (), _M_Ice._t_MarshalException, ())
    NegativeSizeException.ice_type = _M_Ice._t_NegativeSizeException

    _M_Ice.NegativeSizeException = NegativeSizeException
    del NegativeSizeException

if not _M_Ice.__dict__.has_key('FeatureNotSupportedException'):
    _M_Ice.FeatureNotSupportedException = Ice.createTempClass()
    class FeatureNotSupportedException(Ice.LocalException):
        def __init__(self, unsupportedFeature=''):
            self.unsupportedFeature = unsupportedFeature

        def ice_name(self):
            return 'Ice::FeatureNotSupportedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_FeatureNotSupportedException = IcePy.defineException('::Ice::FeatureNotSupportedException', FeatureNotSupportedException, (), None, (('unsupportedFeature', (), IcePy._t_string),))
    FeatureNotSupportedException.ice_type = _M_Ice._t_FeatureNotSupportedException

    _M_Ice.FeatureNotSupportedException = FeatureNotSupportedException
    del FeatureNotSupportedException

if not _M_Ice.__dict__.has_key('SecurityException'):
    _M_Ice.SecurityException = Ice.createTempClass()
    class SecurityException(Ice.LocalException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'Ice::SecurityException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_SecurityException = IcePy.defineException('::Ice::SecurityException', SecurityException, (), None, (('reason', (), IcePy._t_string),))
    SecurityException.ice_type = _M_Ice._t_SecurityException

    _M_Ice.SecurityException = SecurityException
    del SecurityException

if not _M_Ice.__dict__.has_key('FixedProxyException'):
    _M_Ice.FixedProxyException = Ice.createTempClass()
    class FixedProxyException(Ice.LocalException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::FixedProxyException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_FixedProxyException = IcePy.defineException('::Ice::FixedProxyException', FixedProxyException, (), None, ())
    FixedProxyException.ice_type = _M_Ice._t_FixedProxyException

    _M_Ice.FixedProxyException = FixedProxyException
    del FixedProxyException

if not _M_Ice.__dict__.has_key('ResponseSentException'):
    _M_Ice.ResponseSentException = Ice.createTempClass()
    class ResponseSentException(Ice.LocalException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'Ice::ResponseSentException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_Ice._t_ResponseSentException = IcePy.defineException('::Ice::ResponseSentException', ResponseSentException, (), None, ())
    ResponseSentException.ice_type = _M_Ice._t_ResponseSentException

    _M_Ice.ResponseSentException = ResponseSentException
    del ResponseSentException

# End of module Ice
