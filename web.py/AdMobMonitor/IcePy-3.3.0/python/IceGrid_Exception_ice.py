# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Exception.ice'

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

if not _M_IceGrid.__dict__.has_key('ApplicationNotExistException'):
    _M_IceGrid.ApplicationNotExistException = Ice.createTempClass()
    class ApplicationNotExistException(Ice.UserException):
        def __init__(self, name=''):
            self.name = name

        def ice_name(self):
            return 'IceGrid::ApplicationNotExistException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_ApplicationNotExistException = IcePy.defineException('::IceGrid::ApplicationNotExistException', ApplicationNotExistException, (), None, (('name', (), IcePy._t_string),))
    ApplicationNotExistException.ice_type = _M_IceGrid._t_ApplicationNotExistException

    _M_IceGrid.ApplicationNotExistException = ApplicationNotExistException
    del ApplicationNotExistException

if not _M_IceGrid.__dict__.has_key('ServerNotExistException'):
    _M_IceGrid.ServerNotExistException = Ice.createTempClass()
    class ServerNotExistException(Ice.UserException):
        def __init__(self, id=''):
            self.id = id

        def ice_name(self):
            return 'IceGrid::ServerNotExistException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_ServerNotExistException = IcePy.defineException('::IceGrid::ServerNotExistException', ServerNotExistException, (), None, (('id', (), IcePy._t_string),))
    ServerNotExistException.ice_type = _M_IceGrid._t_ServerNotExistException

    _M_IceGrid.ServerNotExistException = ServerNotExistException
    del ServerNotExistException

if not _M_IceGrid.__dict__.has_key('ServerStartException'):
    _M_IceGrid.ServerStartException = Ice.createTempClass()
    class ServerStartException(Ice.UserException):
        def __init__(self, id='', reason=''):
            self.id = id
            self.reason = reason

        def ice_name(self):
            return 'IceGrid::ServerStartException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_ServerStartException = IcePy.defineException('::IceGrid::ServerStartException', ServerStartException, (), None, (
        ('id', (), IcePy._t_string),
        ('reason', (), IcePy._t_string)
    ))
    ServerStartException.ice_type = _M_IceGrid._t_ServerStartException

    _M_IceGrid.ServerStartException = ServerStartException
    del ServerStartException

if not _M_IceGrid.__dict__.has_key('ServerStopException'):
    _M_IceGrid.ServerStopException = Ice.createTempClass()
    class ServerStopException(Ice.UserException):
        def __init__(self, id='', reason=''):
            self.id = id
            self.reason = reason

        def ice_name(self):
            return 'IceGrid::ServerStopException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_ServerStopException = IcePy.defineException('::IceGrid::ServerStopException', ServerStopException, (), None, (
        ('id', (), IcePy._t_string),
        ('reason', (), IcePy._t_string)
    ))
    ServerStopException.ice_type = _M_IceGrid._t_ServerStopException

    _M_IceGrid.ServerStopException = ServerStopException
    del ServerStopException

if not _M_IceGrid.__dict__.has_key('AdapterNotExistException'):
    _M_IceGrid.AdapterNotExistException = Ice.createTempClass()
    class AdapterNotExistException(Ice.UserException):
        def __init__(self, id=''):
            self.id = id

        def ice_name(self):
            return 'IceGrid::AdapterNotExistException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_AdapterNotExistException = IcePy.defineException('::IceGrid::AdapterNotExistException', AdapterNotExistException, (), None, (('id', (), IcePy._t_string),))
    AdapterNotExistException.ice_type = _M_IceGrid._t_AdapterNotExistException

    _M_IceGrid.AdapterNotExistException = AdapterNotExistException
    del AdapterNotExistException

if not _M_IceGrid.__dict__.has_key('ObjectExistsException'):
    _M_IceGrid.ObjectExistsException = Ice.createTempClass()
    class ObjectExistsException(Ice.UserException):
        def __init__(self, id=Ice._struct_marker):
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id

        def ice_name(self):
            return 'IceGrid::ObjectExistsException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_ObjectExistsException = IcePy.defineException('::IceGrid::ObjectExistsException', ObjectExistsException, (), None, (('id', (), _M_Ice._t_Identity),))
    ObjectExistsException.ice_type = _M_IceGrid._t_ObjectExistsException

    _M_IceGrid.ObjectExistsException = ObjectExistsException
    del ObjectExistsException

if not _M_IceGrid.__dict__.has_key('ObjectNotRegisteredException'):
    _M_IceGrid.ObjectNotRegisteredException = Ice.createTempClass()
    class ObjectNotRegisteredException(Ice.UserException):
        def __init__(self, id=Ice._struct_marker):
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id

        def ice_name(self):
            return 'IceGrid::ObjectNotRegisteredException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_ObjectNotRegisteredException = IcePy.defineException('::IceGrid::ObjectNotRegisteredException', ObjectNotRegisteredException, (), None, (('id', (), _M_Ice._t_Identity),))
    ObjectNotRegisteredException.ice_type = _M_IceGrid._t_ObjectNotRegisteredException

    _M_IceGrid.ObjectNotRegisteredException = ObjectNotRegisteredException
    del ObjectNotRegisteredException

if not _M_IceGrid.__dict__.has_key('NodeNotExistException'):
    _M_IceGrid.NodeNotExistException = Ice.createTempClass()
    class NodeNotExistException(Ice.UserException):
        def __init__(self, name=''):
            self.name = name

        def ice_name(self):
            return 'IceGrid::NodeNotExistException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_NodeNotExistException = IcePy.defineException('::IceGrid::NodeNotExistException', NodeNotExistException, (), None, (('name', (), IcePy._t_string),))
    NodeNotExistException.ice_type = _M_IceGrid._t_NodeNotExistException

    _M_IceGrid.NodeNotExistException = NodeNotExistException
    del NodeNotExistException

if not _M_IceGrid.__dict__.has_key('RegistryNotExistException'):
    _M_IceGrid.RegistryNotExistException = Ice.createTempClass()
    class RegistryNotExistException(Ice.UserException):
        def __init__(self, name=''):
            self.name = name

        def ice_name(self):
            return 'IceGrid::RegistryNotExistException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_RegistryNotExistException = IcePy.defineException('::IceGrid::RegistryNotExistException', RegistryNotExistException, (), None, (('name', (), IcePy._t_string),))
    RegistryNotExistException.ice_type = _M_IceGrid._t_RegistryNotExistException

    _M_IceGrid.RegistryNotExistException = RegistryNotExistException
    del RegistryNotExistException

if not _M_IceGrid.__dict__.has_key('DeploymentException'):
    _M_IceGrid.DeploymentException = Ice.createTempClass()
    class DeploymentException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'IceGrid::DeploymentException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_DeploymentException = IcePy.defineException('::IceGrid::DeploymentException', DeploymentException, (), None, (('reason', (), IcePy._t_string),))
    DeploymentException.ice_type = _M_IceGrid._t_DeploymentException

    _M_IceGrid.DeploymentException = DeploymentException
    del DeploymentException

if not _M_IceGrid.__dict__.has_key('NodeUnreachableException'):
    _M_IceGrid.NodeUnreachableException = Ice.createTempClass()
    class NodeUnreachableException(Ice.UserException):
        def __init__(self, name='', reason=''):
            self.name = name
            self.reason = reason

        def ice_name(self):
            return 'IceGrid::NodeUnreachableException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_NodeUnreachableException = IcePy.defineException('::IceGrid::NodeUnreachableException', NodeUnreachableException, (), None, (
        ('name', (), IcePy._t_string),
        ('reason', (), IcePy._t_string)
    ))
    NodeUnreachableException.ice_type = _M_IceGrid._t_NodeUnreachableException

    _M_IceGrid.NodeUnreachableException = NodeUnreachableException
    del NodeUnreachableException

if not _M_IceGrid.__dict__.has_key('ServerUnreachableException'):
    _M_IceGrid.ServerUnreachableException = Ice.createTempClass()
    class ServerUnreachableException(Ice.UserException):
        def __init__(self, name='', reason=''):
            self.name = name
            self.reason = reason

        def ice_name(self):
            return 'IceGrid::ServerUnreachableException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_ServerUnreachableException = IcePy.defineException('::IceGrid::ServerUnreachableException', ServerUnreachableException, (), None, (
        ('name', (), IcePy._t_string),
        ('reason', (), IcePy._t_string)
    ))
    ServerUnreachableException.ice_type = _M_IceGrid._t_ServerUnreachableException

    _M_IceGrid.ServerUnreachableException = ServerUnreachableException
    del ServerUnreachableException

if not _M_IceGrid.__dict__.has_key('RegistryUnreachableException'):
    _M_IceGrid.RegistryUnreachableException = Ice.createTempClass()
    class RegistryUnreachableException(Ice.UserException):
        def __init__(self, name='', reason=''):
            self.name = name
            self.reason = reason

        def ice_name(self):
            return 'IceGrid::RegistryUnreachableException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_RegistryUnreachableException = IcePy.defineException('::IceGrid::RegistryUnreachableException', RegistryUnreachableException, (), None, (
        ('name', (), IcePy._t_string),
        ('reason', (), IcePy._t_string)
    ))
    RegistryUnreachableException.ice_type = _M_IceGrid._t_RegistryUnreachableException

    _M_IceGrid.RegistryUnreachableException = RegistryUnreachableException
    del RegistryUnreachableException

if not _M_IceGrid.__dict__.has_key('BadSignalException'):
    _M_IceGrid.BadSignalException = Ice.createTempClass()
    class BadSignalException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'IceGrid::BadSignalException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_BadSignalException = IcePy.defineException('::IceGrid::BadSignalException', BadSignalException, (), None, (('reason', (), IcePy._t_string),))
    BadSignalException.ice_type = _M_IceGrid._t_BadSignalException

    _M_IceGrid.BadSignalException = BadSignalException
    del BadSignalException

if not _M_IceGrid.__dict__.has_key('PatchException'):
    _M_IceGrid.PatchException = Ice.createTempClass()
    class PatchException(Ice.UserException):
        def __init__(self, reasons=None):
            self.reasons = reasons

        def ice_name(self):
            return 'IceGrid::PatchException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_PatchException = IcePy.defineException('::IceGrid::PatchException', PatchException, (), None, (('reasons', (), _M_Ice._t_StringSeq),))
    PatchException.ice_type = _M_IceGrid._t_PatchException

    _M_IceGrid.PatchException = PatchException
    del PatchException

if not _M_IceGrid.__dict__.has_key('AccessDeniedException'):
    _M_IceGrid.AccessDeniedException = Ice.createTempClass()
    class AccessDeniedException(Ice.UserException):
        def __init__(self, lockUserId=''):
            self.lockUserId = lockUserId

        def ice_name(self):
            return 'IceGrid::AccessDeniedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_AccessDeniedException = IcePy.defineException('::IceGrid::AccessDeniedException', AccessDeniedException, (), None, (('lockUserId', (), IcePy._t_string),))
    AccessDeniedException.ice_type = _M_IceGrid._t_AccessDeniedException

    _M_IceGrid.AccessDeniedException = AccessDeniedException
    del AccessDeniedException

if not _M_IceGrid.__dict__.has_key('AllocationException'):
    _M_IceGrid.AllocationException = Ice.createTempClass()
    class AllocationException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'IceGrid::AllocationException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_AllocationException = IcePy.defineException('::IceGrid::AllocationException', AllocationException, (), None, (('reason', (), IcePy._t_string),))
    AllocationException.ice_type = _M_IceGrid._t_AllocationException

    _M_IceGrid.AllocationException = AllocationException
    del AllocationException

if not _M_IceGrid.__dict__.has_key('AllocationTimeoutException'):
    _M_IceGrid.AllocationTimeoutException = Ice.createTempClass()
    class AllocationTimeoutException(_M_IceGrid.AllocationException):
        def __init__(self, reason=''):
            _M_IceGrid.AllocationException.__init__(self, reason)

        def ice_name(self):
            return 'IceGrid::AllocationTimeoutException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_AllocationTimeoutException = IcePy.defineException('::IceGrid::AllocationTimeoutException', AllocationTimeoutException, (), _M_IceGrid._t_AllocationException, ())
    AllocationTimeoutException.ice_type = _M_IceGrid._t_AllocationTimeoutException

    _M_IceGrid.AllocationTimeoutException = AllocationTimeoutException
    del AllocationTimeoutException

if not _M_IceGrid.__dict__.has_key('PermissionDeniedException'):
    _M_IceGrid.PermissionDeniedException = Ice.createTempClass()
    class PermissionDeniedException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'IceGrid::PermissionDeniedException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_PermissionDeniedException = IcePy.defineException('::IceGrid::PermissionDeniedException', PermissionDeniedException, (), None, (('reason', (), IcePy._t_string),))
    PermissionDeniedException.ice_type = _M_IceGrid._t_PermissionDeniedException

    _M_IceGrid.PermissionDeniedException = PermissionDeniedException
    del PermissionDeniedException

if not _M_IceGrid.__dict__.has_key('ObserverAlreadyRegisteredException'):
    _M_IceGrid.ObserverAlreadyRegisteredException = Ice.createTempClass()
    class ObserverAlreadyRegisteredException(Ice.UserException):
        def __init__(self, id=Ice._struct_marker):
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id

        def ice_name(self):
            return 'IceGrid::ObserverAlreadyRegisteredException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_ObserverAlreadyRegisteredException = IcePy.defineException('::IceGrid::ObserverAlreadyRegisteredException', ObserverAlreadyRegisteredException, (), None, (('id', (), _M_Ice._t_Identity),))
    ObserverAlreadyRegisteredException.ice_type = _M_IceGrid._t_ObserverAlreadyRegisteredException

    _M_IceGrid.ObserverAlreadyRegisteredException = ObserverAlreadyRegisteredException
    del ObserverAlreadyRegisteredException

if not _M_IceGrid.__dict__.has_key('FileNotAvailableException'):
    _M_IceGrid.FileNotAvailableException = Ice.createTempClass()
    class FileNotAvailableException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'IceGrid::FileNotAvailableException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_FileNotAvailableException = IcePy.defineException('::IceGrid::FileNotAvailableException', FileNotAvailableException, (), None, (('reason', (), IcePy._t_string),))
    FileNotAvailableException.ice_type = _M_IceGrid._t_FileNotAvailableException

    _M_IceGrid.FileNotAvailableException = FileNotAvailableException
    del FileNotAvailableException

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::AccessDeniedException"] = "e39e5ad60577c1e7b52e190e1d906b"
Ice.sliceChecksums["::IceGrid::AdapterNotExistException"] = "cee552cb69227f723030cd78b0cccc97"
Ice.sliceChecksums["::IceGrid::AllocationException"] = "ea85a8e5e5f281709bf6aa88d742"
Ice.sliceChecksums["::IceGrid::AllocationTimeoutException"] = "6695f5713499ac6de0626277e167f553"
Ice.sliceChecksums["::IceGrid::ApplicationNotExistException"] = "93fdaabe25dcf75485ffd4972223610"
Ice.sliceChecksums["::IceGrid::BadSignalException"] = "13e67e2d3f46a84aa73fd56d5812caf1"
Ice.sliceChecksums["::IceGrid::DeploymentException"] = "e316fdba8e93ef72d58bd61bbfe29e4"
Ice.sliceChecksums["::IceGrid::FileNotAvailableException"] = "a3e88ae3be93ecd4c82797ad26d6076"
Ice.sliceChecksums["::IceGrid::NodeNotExistException"] = "f07ddace1aa3cb1bbed37c3fbf862dff"
Ice.sliceChecksums["::IceGrid::NodeUnreachableException"] = "8f894a5022704f4dde30bb2a3ea326f9"
Ice.sliceChecksums["::IceGrid::ObjectExistsException"] = "833f69d3ebc872974a9f096352d2ddb"
Ice.sliceChecksums["::IceGrid::ObjectNotRegisteredException"] = "cb181c92b4dfb6e6b97f4ca806899e7"
Ice.sliceChecksums["::IceGrid::ObserverAlreadyRegisteredException"] = "e1267578f9666e2bda9952d7106fd12c"
Ice.sliceChecksums["::IceGrid::PatchException"] = "c28994d76c834b99b94cf4535a13d3"
Ice.sliceChecksums["::IceGrid::PermissionDeniedException"] = "27def8d4569ab203b629b9162d530ba"
Ice.sliceChecksums["::IceGrid::RegistryNotExistException"] = "9e1c1b717e9c5ef72886f16dbfce56f"
Ice.sliceChecksums["::IceGrid::RegistryUnreachableException"] = "514020cac28c588ae487a628e227699"
Ice.sliceChecksums["::IceGrid::ServerNotExistException"] = "6df151f3ce87bd522ed095f7ad97a941"
Ice.sliceChecksums["::IceGrid::ServerStartException"] = "ce92acafa218dd1d1e8aafab20d1"
Ice.sliceChecksums["::IceGrid::ServerStopException"] = "edb57abb5393b8b31b41f3a8e5bd111"
Ice.sliceChecksums["::IceGrid::ServerUnreachableException"] = "f3233583ef7ad8eac2f961aedafdd64"
