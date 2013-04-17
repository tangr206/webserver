# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `UserAccountMapper.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')
__name__ = 'IceGrid'

if not _M_IceGrid.__dict__.has_key('UserAccountNotFoundException'):
    _M_IceGrid.UserAccountNotFoundException = Ice.createTempClass()
    class UserAccountNotFoundException(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'IceGrid::UserAccountNotFoundException'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceGrid._t_UserAccountNotFoundException = IcePy.defineException('::IceGrid::UserAccountNotFoundException', UserAccountNotFoundException, (), None, ())
    UserAccountNotFoundException.ice_type = _M_IceGrid._t_UserAccountNotFoundException

    _M_IceGrid.UserAccountNotFoundException = UserAccountNotFoundException
    del UserAccountNotFoundException

if not _M_IceGrid.__dict__.has_key('UserAccountMapper'):
    _M_IceGrid.UserAccountMapper = Ice.createTempClass()
    class UserAccountMapper(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.UserAccountMapper:
                raise RuntimeError('IceGrid.UserAccountMapper is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::UserAccountMapper')

        def ice_id(self, current=None):
            return '::IceGrid::UserAccountMapper'

        def ice_staticId():
            return '::IceGrid::UserAccountMapper'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def getUserAccount(self, user, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_UserAccountMapper)

        __repr__ = __str__

    _M_IceGrid.UserAccountMapperPrx = Ice.createTempClass()
    class UserAccountMapperPrx(Ice.ObjectPrx):

        def getUserAccount(self, user, _ctx=None):
            return _M_IceGrid.UserAccountMapper._op_getUserAccount.invoke(self, ((user, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.UserAccountMapperPrx.ice_checkedCast(proxy, '::IceGrid::UserAccountMapper', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.UserAccountMapperPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_UserAccountMapperPrx = IcePy.defineProxy('::IceGrid::UserAccountMapper', UserAccountMapperPrx)

    _M_IceGrid._t_UserAccountMapper = IcePy.defineClass('::IceGrid::UserAccountMapper', UserAccountMapper, (), True, None, (), ())
    UserAccountMapper.ice_type = _M_IceGrid._t_UserAccountMapper

    UserAccountMapper._op_getUserAccount = IcePy.Operation('getUserAccount', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), IcePy._t_string, (_M_IceGrid._t_UserAccountNotFoundException,))

    _M_IceGrid.UserAccountMapper = UserAccountMapper
    del UserAccountMapper

    _M_IceGrid.UserAccountMapperPrx = UserAccountMapperPrx
    del UserAccountMapperPrx

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::UserAccountMapper"] = "779fd561878e199444e04cdebaf9ffd4"
Ice.sliceChecksums["::IceGrid::UserAccountNotFoundException"] = "fe2dc4d87f21b9b2cf6f1339d1666281"
