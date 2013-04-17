# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `PropertiesF.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Properties'):
    _M_Ice._t_Properties = IcePy.declareClass('::Ice::Properties')

if not _M_Ice.__dict__.has_key('PropertiesAdmin'):
    _M_Ice._t_PropertiesAdmin = IcePy.declareClass('::Ice::PropertiesAdmin')
    _M_Ice._t_PropertiesAdminPrx = IcePy.declareProxy('::Ice::PropertiesAdmin')

# End of module Ice
