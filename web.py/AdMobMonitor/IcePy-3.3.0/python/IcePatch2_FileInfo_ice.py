# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `FileInfo.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_BuiltinSequences_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module IcePatch2
_M_IcePatch2 = Ice.openModule('IcePatch2')
__name__ = 'IcePatch2'

if not _M_IcePatch2.__dict__.has_key('FileInfo'):
    _M_IcePatch2.FileInfo = Ice.createTempClass()
    class FileInfo(object):
        def __init__(self, path='', checksum=None, size=0, executable=False):
            self.path = path
            self.checksum = checksum
            self.size = size
            self.executable = executable

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.path)
            if self.checksum:
                for _i0 in self.checksum:
                    _h = 5 * _h + __builtin__.hash(_i0)
            _h = 5 * _h + __builtin__.hash(self.size)
            _h = 5 * _h + __builtin__.hash(self.executable)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.path < other.path:
                return -1
            elif self.path > other.path:
                return 1
            if self.checksum < other.checksum:
                return -1
            elif self.checksum > other.checksum:
                return 1
            if self.size < other.size:
                return -1
            elif self.size > other.size:
                return 1
            if self.executable < other.executable:
                return -1
            elif self.executable > other.executable:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IcePatch2._t_FileInfo)

        __repr__ = __str__

    _M_IcePatch2._t_FileInfo = IcePy.defineStruct('::IcePatch2::FileInfo', FileInfo, (), (
        ('path', (), IcePy._t_string),
        ('checksum', (), _M_Ice._t_ByteSeq),
        ('size', (), IcePy._t_int),
        ('executable', (), IcePy._t_bool)
    ))

    _M_IcePatch2.FileInfo = FileInfo
    del FileInfo

if not _M_IcePatch2.__dict__.has_key('_t_FileInfoSeq'):
    _M_IcePatch2._t_FileInfoSeq = IcePy.defineSequence('::IcePatch2::FileInfoSeq', (), _M_IcePatch2._t_FileInfo)

# End of module IcePatch2

Ice.sliceChecksums["::IcePatch2::FileInfo"] = "4c71622889c19c7d3b5ef8210245"
Ice.sliceChecksums["::IcePatch2::FileInfoSeq"] = "892945a7a7bfb532f6148c4be9889bd"
