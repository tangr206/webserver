# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `SSLInfo.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_BuiltinSequences_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')
__name__ = 'Glacier2'

if not _M_Glacier2.__dict__.has_key('SSLInfo'):
    _M_Glacier2.SSLInfo = Ice.createTempClass()
    class SSLInfo(object):
        def __init__(self, remoteHost='', remotePort=0, localHost='', localPort=0, cipher='', certs=None):
            self.remoteHost = remoteHost
            self.remotePort = remotePort
            self.localHost = localHost
            self.localPort = localPort
            self.cipher = cipher
            self.certs = certs

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.remoteHost)
            _h = 5 * _h + __builtin__.hash(self.remotePort)
            _h = 5 * _h + __builtin__.hash(self.localHost)
            _h = 5 * _h + __builtin__.hash(self.localPort)
            _h = 5 * _h + __builtin__.hash(self.cipher)
            if self.certs:
                for _i0 in self.certs:
                    _h = 5 * _h + __builtin__.hash(_i0)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.remoteHost < other.remoteHost:
                return -1
            elif self.remoteHost > other.remoteHost:
                return 1
            if self.remotePort < other.remotePort:
                return -1
            elif self.remotePort > other.remotePort:
                return 1
            if self.localHost < other.localHost:
                return -1
            elif self.localHost > other.localHost:
                return 1
            if self.localPort < other.localPort:
                return -1
            elif self.localPort > other.localPort:
                return 1
            if self.cipher < other.cipher:
                return -1
            elif self.cipher > other.cipher:
                return 1
            if self.certs < other.certs:
                return -1
            elif self.certs > other.certs:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_SSLInfo)

        __repr__ = __str__

    _M_Glacier2._t_SSLInfo = IcePy.defineStruct('::Glacier2::SSLInfo', SSLInfo, (), (
        ('remoteHost', (), IcePy._t_string),
        ('remotePort', (), IcePy._t_int),
        ('localHost', (), IcePy._t_string),
        ('localPort', (), IcePy._t_int),
        ('cipher', (), IcePy._t_string),
        ('certs', (), _M_Ice._t_StringSeq)
    ))

    _M_Glacier2.SSLInfo = SSLInfo
    del SSLInfo

# End of module Glacier2

Ice.sliceChecksums["::Glacier2::SSLInfo"] = "ca63bc6d361a48471c4d16ea29818e5"
