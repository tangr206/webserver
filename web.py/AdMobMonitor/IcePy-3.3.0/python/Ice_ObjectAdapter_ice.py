# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `ObjectAdapter.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_CommunicatorF_ice
import Ice_ServantLocatorF_ice
import Ice_LocatorF_ice
import Ice_Identity_ice
import Ice_FacetMap_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('ObjectAdapter'):
    _M_Ice.ObjectAdapter = Ice.createTempClass()
    class ObjectAdapter(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.ObjectAdapter:
                raise RuntimeError('Ice.ObjectAdapter is an abstract class')

        #
        # Operation signatures.
        #
        # def getName(self):
        # def getCommunicator(self):
        # def activate(self):
        # def hold(self):
        # def waitForHold(self):
        # def deactivate(self):
        # def waitForDeactivate(self):
        # def isDeactivated(self):
        # def destroy(self):
        # def add(self, servant, id):
        # def addFacet(self, servant, id, facet):
        # def addWithUUID(self, servant):
        # def addFacetWithUUID(self, servant, facet):
        # def remove(self, id):
        # def removeFacet(self, id, facet):
        # def removeAllFacets(self, id):
        # def find(self, id):
        # def findFacet(self, id, facet):
        # def findAllFacets(self, id):
        # def findByProxy(self, proxy):
        # def addServantLocator(self, locator, category):
        # def findServantLocator(self, category):
        # def createProxy(self, id):
        # def createDirectProxy(self, id):
        # def createIndirectProxy(self, id):
        # def setLocator(self, loc):
        # def refreshPublishedEndpoints(self):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_ObjectAdapter)

        __repr__ = __str__

    _M_Ice._t_ObjectAdapter = IcePy.defineClass('::Ice::ObjectAdapter', ObjectAdapter, (), True, None, (), ())
    ObjectAdapter.ice_type = _M_Ice._t_ObjectAdapter

    _M_Ice.ObjectAdapter = ObjectAdapter
    del ObjectAdapter

# End of module Ice
