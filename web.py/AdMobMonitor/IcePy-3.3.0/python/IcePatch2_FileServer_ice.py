# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `FileServer.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import IcePatch2_FileInfo_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module IcePatch2
_M_IcePatch2 = Ice.openModule('IcePatch2')

# Start of module IcePatch2
__name__ = 'IcePatch2'

if not _M_IcePatch2.__dict__.has_key('_t_ByteSeqSeq'):
    _M_IcePatch2._t_ByteSeqSeq = IcePy.defineSequence('::IcePatch2::ByteSeqSeq', (), _M_Ice._t_ByteSeq)

if not _M_IcePatch2.__dict__.has_key('PartitionOutOfRangeException'):
    _M_IcePatch2.PartitionOutOfRangeException = Ice.createTempClass()
    class PartitionOutOfRangeException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'IcePatch2::PartitionOutOfRangeException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IcePatch2._t_PartitionOutOfRangeException = IcePy.defineException('::IcePatch2::PartitionOutOfRangeException', PartitionOutOfRangeException, (), None, ())
    PartitionOutOfRangeException.ice_type = _M_IcePatch2._t_PartitionOutOfRangeException

    _M_IcePatch2.PartitionOutOfRangeException = PartitionOutOfRangeException
    del PartitionOutOfRangeException

if not _M_IcePatch2.__dict__.has_key('FileAccessException'):
    _M_IcePatch2.FileAccessException = Ice.createTempClass()
    class FileAccessException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'IcePatch2::FileAccessException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IcePatch2._t_FileAccessException = IcePy.defineException('::IcePatch2::FileAccessException', FileAccessException, (), None, (('reason', (), IcePy._t_string),))
    FileAccessException.ice_type = _M_IcePatch2._t_FileAccessException

    _M_IcePatch2.FileAccessException = FileAccessException
    del FileAccessException

if not _M_IcePatch2.__dict__.has_key('FileServer'):
    _M_IcePatch2.FileServer = Ice.createTempClass()
    class FileServer(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IcePatch2.FileServer:
                raise RuntimeError('IcePatch2.FileServer is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IcePatch2::FileServer')

        def ice_id(self, current=None):
            return '::IcePatch2::FileServer'

        def ice_staticId():
            return '::IcePatch2::FileServer'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def getFileInfoSeq(self, partition, current=None):
        # def getChecksumSeq(self, current=None):
        # def getChecksum(self, current=None):
        # def getFileCompressed_async(self, _cb, path, pos, num, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IcePatch2._t_FileServer)

        __repr__ = __str__

    _M_IcePatch2.FileServerPrx = Ice.createTempClass()
    class FileServerPrx(Ice.ObjectPrx):

        def getFileInfoSeq(self, partition, _ctx=None):
            return _M_IcePatch2.FileServer._op_getFileInfoSeq.invoke(self, ((partition, ), _ctx))

        def getFileInfoSeq_async(self, _cb, partition, _ctx=None):
            return _M_IcePatch2.FileServer._op_getFileInfoSeq.invokeAsync(self, (_cb, (partition, ), _ctx))

        def getChecksumSeq(self, _ctx=None):
            return _M_IcePatch2.FileServer._op_getChecksumSeq.invoke(self, ((), _ctx))

        def getChecksum(self, _ctx=None):
            return _M_IcePatch2.FileServer._op_getChecksum.invoke(self, ((), _ctx))

        def getFileCompressed(self, path, pos, num, _ctx=None):
            return _M_IcePatch2.FileServer._op_getFileCompressed.invoke(self, ((path, pos, num), _ctx))

        def getFileCompressed_async(self, _cb, path, pos, num, _ctx=None):
            return _M_IcePatch2.FileServer._op_getFileCompressed.invokeAsync(self, (_cb, (path, pos, num), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IcePatch2.FileServerPrx.ice_checkedCast(proxy, '::IcePatch2::FileServer', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IcePatch2.FileServerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IcePatch2._t_FileServerPrx = IcePy.defineProxy('::IcePatch2::FileServer', FileServerPrx)

    _M_IcePatch2._t_FileServer = IcePy.defineClass('::IcePatch2::FileServer', FileServer, (), True, None, (), ())
    FileServer.ice_type = _M_IcePatch2._t_FileServer

    FileServer._op_getFileInfoSeq = IcePy.Operation('getFileInfoSeq', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_int),), (), _M_IcePatch2._t_FileInfoSeq, (_M_IcePatch2._t_PartitionOutOfRangeException,))
    FileServer._op_getChecksumSeq = IcePy.Operation('getChecksumSeq', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_IcePatch2._t_ByteSeqSeq, ())
    FileServer._op_getChecksum = IcePy.Operation('getChecksum', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_ByteSeq, ())
    FileServer._op_getFileCompressed = IcePy.Operation('getFileCompressed', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, True, (), (((), IcePy._t_string), ((), IcePy._t_int), ((), IcePy._t_int)), (), _M_Ice._t_ByteSeq, (_M_IcePatch2._t_FileAccessException,))

    _M_IcePatch2.FileServer = FileServer
    del FileServer

    _M_IcePatch2.FileServerPrx = FileServerPrx
    del FileServerPrx

if not _M_IcePatch2.__dict__.has_key('Admin'):
    _M_IcePatch2.Admin = Ice.createTempClass()
    class Admin(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IcePatch2.Admin:
                raise RuntimeError('IcePatch2.Admin is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IcePatch2::Admin')

        def ice_id(self, current=None):
            return '::IcePatch2::Admin'

        def ice_staticId():
            return '::IcePatch2::Admin'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def shutdown(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IcePatch2._t_Admin)

        __repr__ = __str__

    _M_IcePatch2.AdminPrx = Ice.createTempClass()
    class AdminPrx(Ice.ObjectPrx):

        def shutdown(self, _ctx=None):
            return _M_IcePatch2.Admin._op_shutdown.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IcePatch2.AdminPrx.ice_checkedCast(proxy, '::IcePatch2::Admin', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IcePatch2.AdminPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IcePatch2._t_AdminPrx = IcePy.defineProxy('::IcePatch2::Admin', AdminPrx)

    _M_IcePatch2._t_Admin = IcePy.defineClass('::IcePatch2::Admin', Admin, (), True, None, (), ())
    Admin.ice_type = _M_IcePatch2._t_Admin

    Admin._op_shutdown = IcePy.Operation('shutdown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())

    _M_IcePatch2.Admin = Admin
    del Admin

    _M_IcePatch2.AdminPrx = AdminPrx
    del AdminPrx

# End of module IcePatch2

Ice.sliceChecksums["::IcePatch2::Admin"] = "a2df2d4165d639f36f3adadca59f154b"
Ice.sliceChecksums["::IcePatch2::ByteSeqSeq"] = "4bef9684e41babda8aa55f759a854c"
Ice.sliceChecksums["::IcePatch2::FileAccessException"] = "e94ba15e1b6a3639c2358d2f384648"
Ice.sliceChecksums["::IcePatch2::FileServer"] = "c8413cf63b7a104b4b1fb9822ce2f88"
Ice.sliceChecksums["::IcePatch2::PartitionOutOfRangeException"] = "edd324eb399a3f6fecc1a28c2296d8"
