# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Process.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Process'):
    _M_Ice.Process = Ice.createTempClass()
    class Process(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Process:
                raise RuntimeError('Ice.Process is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Ice::Process')

        def ice_id(self, current=None):
            return '::Ice::Process'

        def ice_staticId():
            return '::Ice::Process'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def shutdown(self, current=None):
        # def writeMessage(self, message, fd, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Process)

        __repr__ = __str__

    _M_Ice.ProcessPrx = Ice.createTempClass()
    class ProcessPrx(Ice.ObjectPrx):

        def shutdown(self, _ctx=None):
            return _M_Ice.Process._op_shutdown.invoke(self, ((), _ctx))

        def shutdown_async(self, _cb, _ctx=None):
            return _M_Ice.Process._op_shutdown.invokeAsync(self, (_cb, (), _ctx))

        def writeMessage(self, message, fd, _ctx=None):
            return _M_Ice.Process._op_writeMessage.invoke(self, ((message, fd), _ctx))

        def writeMessage_async(self, _cb, message, fd, _ctx=None):
            return _M_Ice.Process._op_writeMessage.invokeAsync(self, (_cb, (message, fd), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Ice.ProcessPrx.ice_checkedCast(proxy, '::Ice::Process', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Ice.ProcessPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Ice._t_ProcessPrx = IcePy.defineProxy('::Ice::Process', ProcessPrx)

    _M_Ice._t_Process = IcePy.defineClass('::Ice::Process', Process, (), True, None, (), ())
    Process.ice_type = _M_Ice._t_Process

    Process._op_shutdown = IcePy.Operation('shutdown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())
    Process._op_writeMessage = IcePy.Operation('writeMessage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_int)), (), None, ())

    _M_Ice.Process = Process
    del Process

    _M_Ice.ProcessPrx = ProcessPrx
    del ProcessPrx

# End of module Ice
