# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `LocatorF.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Locator'):
    _M_Ice._t_Locator = IcePy.declareClass('::Ice::Locator')
    _M_Ice._t_LocatorPrx = IcePy.declareProxy('::Ice::Locator')

if not _M_Ice.__dict__.has_key('LocatorRegistry'):
    _M_Ice._t_LocatorRegistry = IcePy.declareClass('::Ice::LocatorRegistry')
    _M_Ice._t_LocatorRegistryPrx = IcePy.declareProxy('::Ice::LocatorRegistry')

# End of module Ice
