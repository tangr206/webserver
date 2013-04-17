# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Plugin.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_LoggerF_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Plugin'):
    _M_Ice.Plugin = Ice.createTempClass()
    class Plugin(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Plugin:
                raise RuntimeError('Ice.Plugin is an abstract class')

        #
        # Operation signatures.
        #
        # def initialize(self):
        # def destroy(self):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Plugin)

        __repr__ = __str__

    _M_Ice._t_Plugin = IcePy.defineClass('::Ice::Plugin', Plugin, (), True, None, (), ())
    Plugin.ice_type = _M_Ice._t_Plugin

    _M_Ice.Plugin = Plugin
    del Plugin

if not _M_Ice.__dict__.has_key('PluginManager'):
    _M_Ice.PluginManager = Ice.createTempClass()
    class PluginManager(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.PluginManager:
                raise RuntimeError('Ice.PluginManager is an abstract class')

        #
        # Operation signatures.
        #
        # def initializePlugins(self):
        # def getPlugin(self, name):
        # def addPlugin(self, name, pi):
        # def destroy(self):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_PluginManager)

        __repr__ = __str__

    _M_Ice._t_PluginManager = IcePy.defineClass('::Ice::PluginManager', PluginManager, (), True, None, (), ())
    PluginManager.ice_type = _M_Ice._t_PluginManager

    _M_Ice.PluginManager = PluginManager
    del PluginManager

# End of module Ice
