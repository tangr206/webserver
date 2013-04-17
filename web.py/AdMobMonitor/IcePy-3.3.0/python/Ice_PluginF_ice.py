# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `PluginF.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Plugin'):
    _M_Ice._t_Plugin = IcePy.declareClass('::Ice::Plugin')

if not _M_Ice.__dict__.has_key('PluginManager'):
    _M_Ice._t_PluginManager = IcePy.declareClass('::Ice::PluginManager')

# End of module Ice
