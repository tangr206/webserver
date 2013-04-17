# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `IceStorm.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()
import Ice_SliceChecksumDict_ice
import Ice_Identity_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module IceStorm
_M_IceStorm = Ice.openModule('IceStorm')
__name__ = 'IceStorm'

if not _M_IceStorm.__dict__.has_key('Topic'):
    _M_IceStorm._t_Topic = IcePy.declareClass('::IceStorm::Topic')
    _M_IceStorm._t_TopicPrx = IcePy.declareProxy('::IceStorm::Topic')

if not _M_IceStorm.__dict__.has_key('LinkInfo'):
    _M_IceStorm.LinkInfo = Ice.createTempClass()
    class LinkInfo(object):
        def __init__(self, theTopic=None, name='', cost=0):
            self.theTopic = theTopic
            self.name = name
            self.cost = cost

        def __hash__(self):
            _h = 0
            _h = 5 * _h + __builtin__.hash(self.theTopic)
            _h = 5 * _h + __builtin__.hash(self.name)
            _h = 5 * _h + __builtin__.hash(self.cost)
            return _h % 0x7fffffff

        def __cmp__(self, other):
            if other == None:
                return 1
            if self.theTopic < other.theTopic:
                return -1
            elif self.theTopic > other.theTopic:
                return 1
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            if self.cost < other.cost:
                return -1
            elif self.cost > other.cost:
                return 1
            return 0

        def __str__(self):
            return IcePy.stringify(self, _M_IceStorm._t_LinkInfo)

        __repr__ = __str__

    _M_IceStorm._t_LinkInfo = IcePy.defineStruct('::IceStorm::LinkInfo', LinkInfo, (), (
        ('theTopic', (), _M_IceStorm._t_TopicPrx),
        ('name', (), IcePy._t_string),
        ('cost', (), IcePy._t_int)
    ))

    _M_IceStorm.LinkInfo = LinkInfo
    del LinkInfo

if not _M_IceStorm.__dict__.has_key('_t_LinkInfoSeq'):
    _M_IceStorm._t_LinkInfoSeq = IcePy.defineSequence('::IceStorm::LinkInfoSeq', (), _M_IceStorm._t_LinkInfo)

if not _M_IceStorm.__dict__.has_key('_t_QoS'):
    _M_IceStorm._t_QoS = IcePy.defineDictionary('::IceStorm::QoS', (), IcePy._t_string, IcePy._t_string)

if not _M_IceStorm.__dict__.has_key('LinkExists'):
    _M_IceStorm.LinkExists = Ice.createTempClass()
    class LinkExists(Ice.UserException):
        def __init__(self, name=''):
            self.name = name

        def ice_name(self):
            return 'IceStorm::LinkExists'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceStorm._t_LinkExists = IcePy.defineException('::IceStorm::LinkExists', LinkExists, (), None, (('name', (), IcePy._t_string),))
    LinkExists.ice_type = _M_IceStorm._t_LinkExists

    _M_IceStorm.LinkExists = LinkExists
    del LinkExists

if not _M_IceStorm.__dict__.has_key('NoSuchLink'):
    _M_IceStorm.NoSuchLink = Ice.createTempClass()
    class NoSuchLink(Ice.UserException):
        def __init__(self, name=''):
            self.name = name

        def ice_name(self):
            return 'IceStorm::NoSuchLink'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceStorm._t_NoSuchLink = IcePy.defineException('::IceStorm::NoSuchLink', NoSuchLink, (), None, (('name', (), IcePy._t_string),))
    NoSuchLink.ice_type = _M_IceStorm._t_NoSuchLink

    _M_IceStorm.NoSuchLink = NoSuchLink
    del NoSuchLink

if not _M_IceStorm.__dict__.has_key('AlreadySubscribed'):
    _M_IceStorm.AlreadySubscribed = Ice.createTempClass()
    class AlreadySubscribed(Ice.UserException):
        def __init__(self):
            pass

        def ice_name(self):
            return 'IceStorm::AlreadySubscribed'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceStorm._t_AlreadySubscribed = IcePy.defineException('::IceStorm::AlreadySubscribed', AlreadySubscribed, (), None, ())
    AlreadySubscribed.ice_type = _M_IceStorm._t_AlreadySubscribed

    _M_IceStorm.AlreadySubscribed = AlreadySubscribed
    del AlreadySubscribed

if not _M_IceStorm.__dict__.has_key('BadQoS'):
    _M_IceStorm.BadQoS = Ice.createTempClass()
    class BadQoS(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def ice_name(self):
            return 'IceStorm::BadQoS'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceStorm._t_BadQoS = IcePy.defineException('::IceStorm::BadQoS', BadQoS, (), None, (('reason', (), IcePy._t_string),))
    BadQoS.ice_type = _M_IceStorm._t_BadQoS

    _M_IceStorm.BadQoS = BadQoS
    del BadQoS

if not _M_IceStorm.__dict__.has_key('Topic'):
    _M_IceStorm.Topic = Ice.createTempClass()
    class Topic(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceStorm.Topic:
                raise RuntimeError('IceStorm.Topic is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceStorm::Topic')

        def ice_id(self, current=None):
            return '::IceStorm::Topic'

        def ice_staticId():
            return '::IceStorm::Topic'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def getName(self, current=None):
        # def getPublisher(self, current=None):
        # def getNonReplicatedPublisher(self, current=None):
        # def subscribe(self, theQoS, subscriber, current=None):
        # def subscribeAndGetPublisher(self, theQoS, subscriber, current=None):
        # def unsubscribe(self, subscriber, current=None):
        # def link(self, linkTo, cost, current=None):
        # def unlink(self, linkTo, current=None):
        # def getLinkInfoSeq(self, current=None):
        # def destroy(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceStorm._t_Topic)

        __repr__ = __str__

    _M_IceStorm.TopicPrx = Ice.createTempClass()
    class TopicPrx(Ice.ObjectPrx):

        def getName(self, _ctx=None):
            return _M_IceStorm.Topic._op_getName.invoke(self, ((), _ctx))

        def getPublisher(self, _ctx=None):
            return _M_IceStorm.Topic._op_getPublisher.invoke(self, ((), _ctx))

        def getNonReplicatedPublisher(self, _ctx=None):
            return _M_IceStorm.Topic._op_getNonReplicatedPublisher.invoke(self, ((), _ctx))

        def subscribe(self, theQoS, subscriber, _ctx=None):
            return _M_IceStorm.Topic._op_subscribe.invoke(self, ((theQoS, subscriber), _ctx))

        def subscribeAndGetPublisher(self, theQoS, subscriber, _ctx=None):
            return _M_IceStorm.Topic._op_subscribeAndGetPublisher.invoke(self, ((theQoS, subscriber), _ctx))

        def unsubscribe(self, subscriber, _ctx=None):
            return _M_IceStorm.Topic._op_unsubscribe.invoke(self, ((subscriber, ), _ctx))

        def link(self, linkTo, cost, _ctx=None):
            return _M_IceStorm.Topic._op_link.invoke(self, ((linkTo, cost), _ctx))

        def unlink(self, linkTo, _ctx=None):
            return _M_IceStorm.Topic._op_unlink.invoke(self, ((linkTo, ), _ctx))

        def getLinkInfoSeq(self, _ctx=None):
            return _M_IceStorm.Topic._op_getLinkInfoSeq.invoke(self, ((), _ctx))

        def destroy(self, _ctx=None):
            return _M_IceStorm.Topic._op_destroy.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceStorm.TopicPrx.ice_checkedCast(proxy, '::IceStorm::Topic', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceStorm.TopicPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceStorm._t_TopicPrx = IcePy.defineProxy('::IceStorm::Topic', TopicPrx)

    _M_IceStorm._t_Topic = IcePy.defineClass('::IceStorm::Topic', Topic, (), True, None, (), ())
    Topic.ice_type = _M_IceStorm._t_Topic

    Topic._op_getName = IcePy.Operation('getName', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_string, ())
    Topic._op_getPublisher = IcePy.Operation('getPublisher', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_ObjectPrx, ())
    Topic._op_getNonReplicatedPublisher = IcePy.Operation('getNonReplicatedPublisher', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_ObjectPrx, ())
    Topic._op_subscribe = IcePy.Operation('subscribe', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceStorm._t_QoS), ((), IcePy._t_ObjectPrx)), (), None, ())
    Topic._op_subscribe.deprecate("subscribe is deprecated, use subscribeAndGetPublisher instead")
    Topic._op_subscribeAndGetPublisher = IcePy.Operation('subscribeAndGetPublisher', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceStorm._t_QoS), ((), IcePy._t_ObjectPrx)), (), IcePy._t_ObjectPrx, (_M_IceStorm._t_AlreadySubscribed, _M_IceStorm._t_BadQoS))
    Topic._op_unsubscribe = IcePy.Operation('unsubscribe', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_ObjectPrx),), (), None, ())
    Topic._op_link = IcePy.Operation('link', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceStorm._t_TopicPrx), ((), IcePy._t_int)), (), None, (_M_IceStorm._t_LinkExists,))
    Topic._op_unlink = IcePy.Operation('unlink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceStorm._t_TopicPrx),), (), None, (_M_IceStorm._t_NoSuchLink,))
    Topic._op_getLinkInfoSeq = IcePy.Operation('getLinkInfoSeq', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_IceStorm._t_LinkInfoSeq, ())
    Topic._op_destroy = IcePy.Operation('destroy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())

    _M_IceStorm.Topic = Topic
    del Topic

    _M_IceStorm.TopicPrx = TopicPrx
    del TopicPrx

if not _M_IceStorm.__dict__.has_key('_t_TopicDict'):
    _M_IceStorm._t_TopicDict = IcePy.defineDictionary('::IceStorm::TopicDict', (), IcePy._t_string, _M_IceStorm._t_TopicPrx)

if not _M_IceStorm.__dict__.has_key('TopicExists'):
    _M_IceStorm.TopicExists = Ice.createTempClass()
    class TopicExists(Ice.UserException):
        def __init__(self, name=''):
            self.name = name

        def ice_name(self):
            return 'IceStorm::TopicExists'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceStorm._t_TopicExists = IcePy.defineException('::IceStorm::TopicExists', TopicExists, (), None, (('name', (), IcePy._t_string),))
    TopicExists.ice_type = _M_IceStorm._t_TopicExists

    _M_IceStorm.TopicExists = TopicExists
    del TopicExists

if not _M_IceStorm.__dict__.has_key('NoSuchTopic'):
    _M_IceStorm.NoSuchTopic = Ice.createTempClass()
    class NoSuchTopic(Ice.UserException):
        def __init__(self, name=''):
            self.name = name

        def ice_name(self):
            return 'IceStorm::NoSuchTopic'

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

    _M_IceStorm._t_NoSuchTopic = IcePy.defineException('::IceStorm::NoSuchTopic', NoSuchTopic, (), None, (('name', (), IcePy._t_string),))
    NoSuchTopic.ice_type = _M_IceStorm._t_NoSuchTopic

    _M_IceStorm.NoSuchTopic = NoSuchTopic
    del NoSuchTopic

if not _M_IceStorm.__dict__.has_key('TopicManager'):
    _M_IceStorm.TopicManager = Ice.createTempClass()
    class TopicManager(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_IceStorm.TopicManager:
                raise RuntimeError('IceStorm.TopicManager is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceStorm::TopicManager')

        def ice_id(self, current=None):
            return '::IceStorm::TopicManager'

        def ice_staticId():
            return '::IceStorm::TopicManager'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def create(self, name, current=None):
        # def retrieve(self, name, current=None):
        # def retrieveAll(self, current=None):
        # def getSliceChecksums(self, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_IceStorm._t_TopicManager)

        __repr__ = __str__

    _M_IceStorm.TopicManagerPrx = Ice.createTempClass()
    class TopicManagerPrx(Ice.ObjectPrx):

        def create(self, name, _ctx=None):
            return _M_IceStorm.TopicManager._op_create.invoke(self, ((name, ), _ctx))

        def retrieve(self, name, _ctx=None):
            return _M_IceStorm.TopicManager._op_retrieve.invoke(self, ((name, ), _ctx))

        def retrieveAll(self, _ctx=None):
            return _M_IceStorm.TopicManager._op_retrieveAll.invoke(self, ((), _ctx))

        def getSliceChecksums(self, _ctx=None):
            return _M_IceStorm.TopicManager._op_getSliceChecksums.invoke(self, ((), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceStorm.TopicManagerPrx.ice_checkedCast(proxy, '::IceStorm::TopicManager', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceStorm.TopicManagerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceStorm._t_TopicManagerPrx = IcePy.defineProxy('::IceStorm::TopicManager', TopicManagerPrx)

    _M_IceStorm._t_TopicManager = IcePy.defineClass('::IceStorm::TopicManager', TopicManager, (), True, None, (), ())
    TopicManager.ice_type = _M_IceStorm._t_TopicManager

    TopicManager._op_create = IcePy.Operation('create', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), _M_IceStorm._t_TopicPrx, (_M_IceStorm._t_TopicExists,))
    TopicManager._op_retrieve = IcePy.Operation('retrieve', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (((), IcePy._t_string),), (), _M_IceStorm._t_TopicPrx, (_M_IceStorm._t_NoSuchTopic,))
    TopicManager._op_retrieveAll = IcePy.Operation('retrieveAll', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_IceStorm._t_TopicDict, ())
    TopicManager._op_getSliceChecksums = IcePy.Operation('getSliceChecksums', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_SliceChecksumDict, ())

    _M_IceStorm.TopicManager = TopicManager
    del TopicManager

    _M_IceStorm.TopicManagerPrx = TopicManagerPrx
    del TopicManagerPrx

# End of module IceStorm

Ice.sliceChecksums["::IceStorm::AlreadySubscribed"] = "5a82e77b38f02f3118c536f9446a889e"
Ice.sliceChecksums["::IceStorm::BadQoS"] = "44f2de592dd62e3f7f4ffdf043692d"
Ice.sliceChecksums["::IceStorm::LinkExists"] = "e11768febd56a8813729ce69be6c4c2"
Ice.sliceChecksums["::IceStorm::LinkInfo"] = "d0e073e5e0925ec95656f71d572e2e13"
Ice.sliceChecksums["::IceStorm::LinkInfoSeq"] = "a8921e43838692bbe6ca63f3dcf9b6"
Ice.sliceChecksums["::IceStorm::NoSuchLink"] = "fd8f652776796bffca2df1a3baf455a3"
Ice.sliceChecksums["::IceStorm::NoSuchTopic"] = "7a9479a5c39cdd32335d722bbc971176"
Ice.sliceChecksums["::IceStorm::QoS"] = "3e27cb32bc95cca7b013efbf5c254b35"
Ice.sliceChecksums["::IceStorm::Topic"] = "6f5a475ba16151d0414ffb84d3dad3"
Ice.sliceChecksums["::IceStorm::TopicDict"] = "fff078a98be068c52d9e1d7d8f6df2a"
Ice.sliceChecksums["::IceStorm::TopicExists"] = "38e6913833539b8d616d114d4e7b28d"
Ice.sliceChecksums["::IceStorm::TopicManager"] = "ffc1baf19222891f8b432be6551fed5"
