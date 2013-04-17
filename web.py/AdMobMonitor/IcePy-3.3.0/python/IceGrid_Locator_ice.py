# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Locator.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_Locator_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')
__name__ = 'IceGrid'

if not _M_IceGrid.__dict__.has_key('Registry'):
    _M_IceGrid._t_Registry = IcePy.declareClass('::IceGrid::Registry')
    _M_IceGrid._t_RegistryPrx = IcePy.declareProxy('::IceGrid::Registry')

if not _M_IceGrid.__dict__.has_key('Query'):
    _M_IceGrid._t_Query = IcePy.declareClass('::IceGrid::Query')
    _M_IceGrid._t_QueryPrx = IcePy.declareProxy('::IceGrid::Query')

if not _M_IceGrid.__dict__.has_key('Locator'):
    _M_IceGrid.Locator = Ice.createTempClass()
    class Locator(_M_Ice.Locator):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.Locator:
                raise RuntimeError('IceGrid.Locator is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Locator', '::Ice::Object', '::IceGrid::Locator')

        def ice_id(self, current=None):
            return '::IceGrid::Locator'

        def ice_staticId():
            return '::IceGrid::Locator'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def getLocalRegistry(self, current=None):
        # def getLocalQuery(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_Locator)

        __repr__ = __str__

    _M_IceGrid.LocatorPrx = Ice.createTempClass()
    class LocatorPrx(_M_Ice.LocatorPrx):

        def getLocalRegistry(self, _ctx=None):
            return _M_IceGrid.Locator._op_getLocalRegistry.invoke(self, ((), _ctx))

        def getLocalQuery(self, _ctx=None):
            return _M_IceGrid.Locator._op_getLocalQuery.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.LocatorPrx.ice_checkedCast(proxy, '::IceGrid::Locator', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.LocatorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_LocatorPrx = IcePy.defineProxy('::IceGrid::Locator', LocatorPrx)

    _M_IceGrid._t_Locator = IcePy.defineClass('::IceGrid::Locator', Locator, (), True, None, (_M_Ice._t_Locator,), ())
    Locator.ice_type = _M_IceGrid._t_Locator

    Locator._op_getLocalRegistry = IcePy.Operation('getLocalRegistry', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), _M_IceGrid._t_RegistryPrx, ())
    Locator._op_getLocalQuery = IcePy.Operation('getLocalQuery', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), _M_IceGrid._t_QueryPrx, ())

    _M_IceGrid.Locator = Locator
    del Locator

    _M_IceGrid.LocatorPrx = LocatorPrx
    del LocatorPrx

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::Locator"] = "816e9d7a3cb39b8c80fe342e7f18ae"
