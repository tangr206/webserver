# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Query.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_Identity_ice
import Ice_BuiltinSequences_ice
import IceGrid_Exception_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')

# Start of module IceGrid
__name__ = 'IceGrid'

if not _M_IceGrid.__dict__.has_key('LoadSample'):
    _M_IceGrid.LoadSample = Ice.createTempClass()
    class LoadSample(object):

        def __init__(self, val):
            assert(val >= 0 and val < 3)
            self.value = val

        def __str__(self):
            if self.value == 0:
                return 'LoadSample1'
            elif self.value == 1:
                return 'LoadSample5'
            elif self.value == 2:
                return 'LoadSample15'
            return None

        __repr__ = __str__

        def __hash__(self):
            return self.value

        def __cmp__(self, other):
            return cmp(self.value, other.value)

    LoadSample.LoadSample1 = LoadSample(0)
    LoadSample.LoadSample5 = LoadSample(1)
    LoadSample.LoadSample15 = LoadSample(2)

    _M_IceGrid._t_LoadSample = IcePy.defineEnum('::IceGrid::LoadSample', LoadSample, (), (LoadSample.LoadSample1, LoadSample.LoadSample5, LoadSample.LoadSample15))

    _M_IceGrid.LoadSample = LoadSample
    del LoadSample

if not _M_IceGrid.__dict__.has_key('Query'):
    _M_IceGrid.Query = Ice.createTempClass()
    class Query(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.Query:
                raise RuntimeError('IceGrid.Query is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::Query')

        def ice_id(self, current=None):
            return '::IceGrid::Query'

        def ice_staticId():
            return '::IceGrid::Query'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def findObjectById(self, id, current=None):
        # def findObjectByType(self, type, current=None):
        # def findObjectByTypeOnLeastLoadedNode(self, type, sample, current=None):
        # def findAllObjectsByType(self, type, current=None):
        # def findAllReplicas(self, proxy, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_Query)

        __repr__ = __str__

    _M_IceGrid.QueryPrx = Ice.createTempClass()
    class QueryPrx(Ice.ObjectPrx):

        def findObjectById(self, id, _ctx=None):
            return _M_IceGrid.Query._op_findObjectById.invoke(self, ((id, ), _ctx))

        def findObjectById_async(self, _cb, id, _ctx=None):
            return _M_IceGrid.Query._op_findObjectById.invokeAsync(self, (_cb, (id, ), _ctx))

        def findObjectByType(self, type, _ctx=None):
            return _M_IceGrid.Query._op_findObjectByType.invoke(self, ((type, ), _ctx))

        def findObjectByType_async(self, _cb, type, _ctx=None):
            return _M_IceGrid.Query._op_findObjectByType.invokeAsync(self, (_cb, (type, ), _ctx))

        def findObjectByTypeOnLeastLoadedNode(self, type, sample, _ctx=None):
            return _M_IceGrid.Query._op_findObjectByTypeOnLeastLoadedNode.invoke(self, ((type, sample), _ctx))

        def findObjectByTypeOnLeastLoadedNode_async(self, _cb, type, sample, _ctx=None):
            return _M_IceGrid.Query._op_findObjectByTypeOnLeastLoadedNode.invokeAsync(self, (_cb, (type, sample), _ctx))

        def findAllObjectsByType(self, type, _ctx=None):
            return _M_IceGrid.Query._op_findAllObjectsByType.invoke(self, ((type, ), _ctx))

        def findAllObjectsByType_async(self, _cb, type, _ctx=None):
            return _M_IceGrid.Query._op_findAllObjectsByType.invokeAsync(self, (_cb, (type, ), _ctx))

        def findAllReplicas(self, proxy, _ctx=None):
            return _M_IceGrid.Query._op_findAllReplicas.invoke(self, ((proxy, ), _ctx))

        def findAllReplicas_async(self, _cb, proxy, _ctx=None):
            return _M_IceGrid.Query._op_findAllReplicas.invokeAsync(self, (_cb, (proxy, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.QueryPrx.ice_checkedCast(proxy, '::IceGrid::Query', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.QueryPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_QueryPrx = IcePy.defineProxy('::IceGrid::Query', QueryPrx)

    _M_IceGrid._t_Query = IcePy.defineClass('::IceGrid::Query', Query, (), True, None, (), ())
    Query.ice_type = _M_IceGrid._t_Query

    Query._op_findObjectById = IcePy.Operation('findObjectById', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), _M_Ice._t_Identity),), (), IcePy._t_ObjectPrx, ())
    Query._op_findObjectByType = IcePy.Operation('findObjectByType', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), IcePy._t_ObjectPrx, ())
    Query._op_findObjectByTypeOnLeastLoadedNode = IcePy.Operation('findObjectByTypeOnLeastLoadedNode', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string), ((), _M_IceGrid._t_LoadSample)), (), IcePy._t_ObjectPrx, ())
    Query._op_findAllObjectsByType = IcePy.Operation('findAllObjectsByType', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), _M_Ice._t_ObjectProxySeq, ())
    Query._op_findAllReplicas = IcePy.Operation('findAllReplicas', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_ObjectPrx),), (), _M_Ice._t_ObjectProxySeq, ())

    _M_IceGrid.Query = Query
    del Query

    _M_IceGrid.QueryPrx = QueryPrx
    del QueryPrx

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::LoadSample"] = "ec48c06fa099138a5fbbce121a9a290"
Ice.sliceChecksums["::IceGrid::Query"] = "39dbe5f62c19aa42c2e0fbaf220b4f1"
