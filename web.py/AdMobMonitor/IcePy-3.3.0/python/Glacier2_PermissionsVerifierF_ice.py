# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `PermissionsVerifierF.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')
__name__ = 'Glacier2'

if not _M_Glacier2.__dict__.has_key('PermissionsVerifier'):
    _M_Glacier2._t_PermissionsVerifier = IcePy.declareClass('::Glacier2::PermissionsVerifier')
    _M_Glacier2._t_PermissionsVerifierPrx = IcePy.declareProxy('::Glacier2::PermissionsVerifier')

if not _M_Glacier2.__dict__.has_key('SSLPermissionsVerifier'):
    _M_Glacier2._t_SSLPermissionsVerifier = IcePy.declareClass('::Glacier2::SSLPermissionsVerifier')
    _M_Glacier2._t_SSLPermissionsVerifierPrx = IcePy.declareProxy('::Glacier2::SSLPermissionsVerifier')

# End of module Glacier2
