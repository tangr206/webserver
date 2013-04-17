# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `BuiltinSequences.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('_t_BoolSeq'):
    _M_Ice._t_BoolSeq = IcePy.defineSequence('::Ice::BoolSeq', (), IcePy._t_bool)

if not _M_Ice.__dict__.has_key('_t_ByteSeq'):
    _M_Ice._t_ByteSeq = IcePy.defineSequence('::Ice::ByteSeq', (), IcePy._t_byte)

if not _M_Ice.__dict__.has_key('_t_ShortSeq'):
    _M_Ice._t_ShortSeq = IcePy.defineSequence('::Ice::ShortSeq', (), IcePy._t_short)

if not _M_Ice.__dict__.has_key('_t_IntSeq'):
    _M_Ice._t_IntSeq = IcePy.defineSequence('::Ice::IntSeq', (), IcePy._t_int)

if not _M_Ice.__dict__.has_key('_t_LongSeq'):
    _M_Ice._t_LongSeq = IcePy.defineSequence('::Ice::LongSeq', (), IcePy._t_long)

if not _M_Ice.__dict__.has_key('_t_FloatSeq'):
    _M_Ice._t_FloatSeq = IcePy.defineSequence('::Ice::FloatSeq', (), IcePy._t_float)

if not _M_Ice.__dict__.has_key('_t_DoubleSeq'):
    _M_Ice._t_DoubleSeq = IcePy.defineSequence('::Ice::DoubleSeq', (), IcePy._t_double)

if not _M_Ice.__dict__.has_key('_t_StringSeq'):
    _M_Ice._t_StringSeq = IcePy.defineSequence('::Ice::StringSeq', (), IcePy._t_string)

if not _M_Ice.__dict__.has_key('_t_ObjectSeq'):
    _M_Ice._t_ObjectSeq = IcePy.defineSequence('::Ice::ObjectSeq', (), IcePy._t_Object)

if not _M_Ice.__dict__.has_key('_t_ObjectProxySeq'):
    _M_Ice._t_ObjectProxySeq = IcePy.defineSequence('::Ice::ObjectProxySeq', (), IcePy._t_ObjectPrx)

# End of module Ice
