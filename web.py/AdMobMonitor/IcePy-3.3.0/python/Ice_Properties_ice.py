# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Properties.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_BuiltinSequences_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('_t_PropertyDict'):
    _M_Ice._t_PropertyDict = IcePy.defineDictionary('::Ice::PropertyDict', (), IcePy._t_string, IcePy._t_string)

if not _M_Ice.__dict__.has_key('Properties'):
    _M_Ice.Properties = Ice.createTempClass()
    class Properties(object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Properties:
                raise RuntimeError('Ice.Properties is an abstract class')

        #
        # Operation signatures.
        #
        # def getProperty(self, key):
        # def getPropertyWithDefault(self, key, value):
        # def getPropertyAsInt(self, key):
        # def getPropertyAsIntWithDefault(self, key, value):
        # def getPropertyAsList(self, key):
        # def getPropertyAsListWithDefault(self, key, value):
        # def getPropertiesForPrefix(self, prefix):
        # def setProperty(self, key, value):
        # def getCommandLineOptions(self):
        # def parseCommandLineOptions(self, prefix, options):
        # def parseIceCommandLineOptions(self, options):
        # def load(self, file):
        # def clone(self):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Properties)

        __repr__ = __str__

    _M_Ice._t_Properties = IcePy.defineClass('::Ice::Properties', Properties, (), True, None, (), ())
    Properties.ice_type = _M_Ice._t_Properties

    _M_Ice.Properties = Properties
    del Properties

if not _M_Ice.__dict__.has_key('PropertiesAdmin'):
    _M_Ice.PropertiesAdmin = Ice.createTempClass()
    class PropertiesAdmin(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.PropertiesAdmin:
                raise RuntimeError('Ice.PropertiesAdmin is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Ice::PropertiesAdmin')

        def ice_id(self, current=None):
            return '::Ice::PropertiesAdmin'

        def ice_staticId():
            return '::Ice::PropertiesAdmin'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def getProperty(self, key, current=None):
        # def getPropertiesForPrefix(self, prefix, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_PropertiesAdmin)

        __repr__ = __str__

    _M_Ice.PropertiesAdminPrx = Ice.createTempClass()
    class PropertiesAdminPrx(Ice.ObjectPrx):

        def getProperty(self, key, _ctx=None):
            return _M_Ice.PropertiesAdmin._op_getProperty.invoke(self, ((key, ), _ctx))

        def getProperty_async(self, _cb, key, _ctx=None):
            return _M_Ice.PropertiesAdmin._op_getProperty.invokeAsync(self, (_cb, (key, ), _ctx))

        def getPropertiesForPrefix(self, prefix, _ctx=None):
            return _M_Ice.PropertiesAdmin._op_getPropertiesForPrefix.invoke(self, ((prefix, ), _ctx))

        def getPropertiesForPrefix_async(self, _cb, prefix, _ctx=None):
            return _M_Ice.PropertiesAdmin._op_getPropertiesForPrefix.invokeAsync(self, (_cb, (prefix, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Ice.PropertiesAdminPrx.ice_checkedCast(proxy, '::Ice::PropertiesAdmin', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Ice.PropertiesAdminPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Ice._t_PropertiesAdminPrx = IcePy.defineProxy('::Ice::PropertiesAdmin', PropertiesAdminPrx)

    _M_Ice._t_PropertiesAdmin = IcePy.defineClass('::Ice::PropertiesAdmin', PropertiesAdmin, (), True, None, (), ())
    PropertiesAdmin.ice_type = _M_Ice._t_PropertiesAdmin

    PropertiesAdmin._op_getProperty = IcePy.Operation('getProperty', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), IcePy._t_string, ())
    PropertiesAdmin._op_getPropertiesForPrefix = IcePy.Operation('getPropertiesForPrefix', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), _M_Ice._t_PropertyDict, ())

    _M_Ice.PropertiesAdmin = PropertiesAdmin
    del PropertiesAdmin

    _M_Ice.PropertiesAdminPrx = PropertiesAdminPrx
    del PropertiesAdminPrx

# End of module Ice
