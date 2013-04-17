# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `SessionF.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')
__name__ = 'Glacier2'

if not _M_Glacier2.__dict__.has_key('Session'):
    _M_Glacier2._t_Session = IcePy.declareClass('::Glacier2::Session')
    _M_Glacier2._t_SessionPrx = IcePy.declareProxy('::Glacier2::Session')

if not _M_Glacier2.__dict__.has_key('SessionManager'):
    _M_Glacier2._t_SessionManager = IcePy.declareClass('::Glacier2::SessionManager')
    _M_Glacier2._t_SessionManagerPrx = IcePy.declareProxy('::Glacier2::SessionManager')

if not _M_Glacier2.__dict__.has_key('SSLSessionManager'):
    _M_Glacier2._t_SSLSessionManager = IcePy.declareClass('::Glacier2::SSLSessionManager')
    _M_Glacier2._t_SSLSessionManagerPrx = IcePy.declareProxy('::Glacier2::SSLSessionManager')

# End of module Glacier2
