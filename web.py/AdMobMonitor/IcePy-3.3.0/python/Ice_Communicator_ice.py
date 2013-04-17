# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Communicator.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_LoggerF_ice
import Ice_StatsF_ice
import Ice_ObjectAdapterF_ice
import Ice_PropertiesF_ice
import Ice_ObjectFactoryF_ice
import Ice_RouterF_ice
import Ice_LocatorF_ice
import Ice_PluginF_ice
import Ice_ImplicitContextF_ice
import Ice_Current_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Communicator'):
    _M_Ice.Communicator = Ice.createTempClass()
    class Communicator(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Communicator:
                raise RuntimeError('Ice.Communicator is an abstract class')

        #
        # Operation signatures.
        #
        # def destroy(self):
        # def shutdown(self):
        # def waitForShutdown(self):
        # def isShutdown(self):
        # def stringToProxy(self, str):
        # def proxyToString(self, obj):
        # def propertyToProxy(self, property):
        # def stringToIdentity(self, str):
        # def identityToString(self, ident):
        # def createObjectAdapter(self, name):
        # def createObjectAdapterWithEndpoints(self, name, endpoints):
        # def createObjectAdapterWithRouter(self, name, rtr):
        # def addObjectFactory(self, factory, id):
        # def findObjectFactory(self, id):
        # def getDefaultContext(self):
        # def setDefaultContext(self, ctx):
        # def getImplicitContext(self):
        # def getProperties(self):
        # def getLogger(self):
        # def getStats(self):
        # def getDefaultRouter(self):
        # def setDefaultRouter(self, rtr):
        # def getDefaultLocator(self):
        # def setDefaultLocator(self, loc):
        # def getPluginManager(self):
        # def flushBatchRequests(self):
        # def getAdmin(self):
        # def addAdminFacet(self, servant, facet):
        # def removeAdminFacet(self, facet):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Communicator)

        __repr__ = __str__

    _M_Ice._t_Communicator = IcePy.defineClass('::Ice::Communicator', Communicator, (), True, None, (), ())
    Communicator.ice_type = _M_Ice._t_Communicator

    _M_Ice.Communicator = Communicator
    del Communicator

# End of module Ice
