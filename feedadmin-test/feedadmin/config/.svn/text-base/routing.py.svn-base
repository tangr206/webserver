"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')
    # map.connect('/get-stype-list', controller='hello', action='GetStypeList')
    map.connect('/save-stype-config', controller='hello', action='SaveStypeConfig')
    map.connect('/get-stype-config', controller='hello', action='GetStypeConfig')
    map.connect('/set-stype-state', controller='hello', action='SetStypeState')

    # map.connect('/hello', controller='FeedAdmin', action='Hello')

    map.connect('/feed-list', controller='FeedAdmin', action='FeedListView')
    map.connect('/get-stype-list', controller='FeedAdmin', action='GetStypeList')
    map.connect('/get-stype-ids', controller='FeedAdmin', action='GetStypeIds')

    map.connect('/feed-config-create', controller='FeedAdmin', action='StypeConfigCreate')
    map.connect('/feed-config-edit', controller='FeedAdmin', action='StypeConfigEdit')
    map.connect('/get-feed-config', controller='FeedAdmin', action='GetStypeConfig')
    map.connect('/save-feed-config', controller='FeedAdmin', action='SaveStypeConfig')
    map.connect('/remove-stype', controller='FeedAdmin', action='RemoveStype')

    map.connect('/get-stype-versions', controller='FeedAdmin', action='GetStypeVersions')

    map.connect('/update-stype-version-using-id', controller='FeedAdmin', action='UpdateStypeVersionUsingId')
    map.connect('/update-stype-version-test-id', controller='FeedAdmin', action='UpdateStypeVersionTestId')
    map.connect('/update-stype-version-status', controller='FeedAdmin', action='UpdateStypeVersionStatus')
    map.connect('/get-stype-version-info', controller='FeedAdmin', action='GetStypeVersionInfo')

    map.connect('/get-stype-version-seqs', controller='FeedAdmin', action='GetStypeVersionTpls')
    map.connect('/add-stype-version', controller='FeedAdmin', action='AddStypeVersion')
    map.connect('/feed-keys-edit', controller='FeedAdmin', action='FeedKeysEdit')
    map.connect('/add-version-seq', controller='FeedAdmin', action='AddVersionTpl')
    map.connect('/save-version-keys', controller='FeedAdmin', action='SaveVersionKeys')
    map.connect('/remove-data-version', controller='FeedAdmin', action='RemoveDataVersion')

    map.connect('/save-version-key-mappings', controller='FeedAdmin', action='SaveVersionKeyMappings')
    map.connect('/get-feed-keys', controller='FeedAdmin', action='GetFeedKeys')
    map.connect('/get-version-keys', controller='FeedAdmin', action='GetVersionKeys')
    map.connect('/generate-code', controller='FeedAdmin', action='GenerateCode')

    map.connect('/reloadtest', controller='FeedAdmin', action='ReloadTest')
    map.connect('/reloaddist', controller='FeedAdmin', action='ReloadDist')

    map.connect('/feed-tpl-edit', controller='FeedAdmin', action='FeedTplEdit')
    map.connect('/save-tpl', controller='FeedAdmin', action='SaveTemplate')
    map.connect('/remove-tpl', controller='FeedAdmin', action='RemoveTemplate')
    map.connect('/get-tpls', controller='FeedAdmin', action='GetTemplates')
    map.connect('/update-tpl-view-status', controller='FeedAdmin', action='UpdateTplViewStatus')
    map.connect('/validate-tpl', controller='FeedAdmin', action='ValidateTemplate')
    
    map.connect('/user-apply', controller='FeedAdmin', action='UserApply')
    map.connect('/user-apply-submit', controller='FeedAdmin', action='UserApplySubmit')
    map.connect('/user-apply-list', controller='FeedAdmin', action='UserApplyList')
    map.connect('/get-user-apply-list', controller='FeedAdmin', action='GetUserApplyList')
    map.connect('/get-user-apply-item', controller='FeedAdmin', action='GetUserApplyItem')
    map.connect('/set-user-apply-handled', controller='FeedAdmin', action='SetUserApplyHandled')
    map.connect('/remove-user-apply', controller='FeedAdmin', action='RemoveUserApply')

    map.connect('/apply-new-feed', controller='FeedAdmin', action='ApplyNewFeed')
    map.connect('/apply-new-feed-submit', controller='FeedAdmin', action='ApplyNewFeedSubmit')
    map.connect('/apply-new-feed-list', controller='FeedAdmin', action='ApplyNewFeedList')
    map.connect('/get-apply-feed-item', controller='FeedAdmin', action='GetApplyFeedItem')
    map.connect('/get-apply-feed-list', controller='FeedAdmin', action='GetApplyFeedList')

    map.connect('/apply-new-version', controller='FeedAdmin', action='ApplyNewVersion')
    map.connect('/apply-new-version-submit', controller='FeedAdmin', action='ApplyNewVersionSubmit')
    map.connect('/apply-new-version-list', controller='FeedAdmin', action='ApplyNewVersionList')
    map.connect('/get-apply-version-list', controller='FeedAdmin', action='GetApplyVersionList')
    map.connect('/version-apply-handled', controller='FeedAdmin', action='VersionApplyHandled')

    map.connect('/apply-new-seq', controller='FeedAdmin', action='ApplyNewTpl')
    map.connect('/apply-new-seq-submit', controller='FeedAdmin', action='ApplyNewTplSubmit')
    map.connect('/apply-new-seq-list', controller='FeedAdmin', action='ApplyNewTplList')
    map.connect('/get-apply-seq-list', controller='FeedAdmin', action='GetApplyTplList')
    map.connect('/seq-apply-handled', controller='FeedAdmin', action='TplApplyHandled')

    map.connect('/apply-rollback', controller='FeedAdmin', action='ApplyRollback')
    map.connect('/apply-rollback-submit', controller='FeedAdmin', action='ApplyRollbackSubmit')
    map.connect('/get-apply-rollback-list', controller='FeedAdmin', action='GetApplyRollbackList')
    map.connect('/apply-rollback-list', controller='FeedAdmin', action='ApplyRollbackList')

    map.connect('/apply-publish', controller='FeedAdmin', action='ApplyPublish')
    map.connect('/apply-publish-submit', controller='FeedAdmin', action='ApplyPublishSubmit')
    map.connect('/get-apply-publish-list', controller='FeedAdmin', action='GetApplyPublishList')
    map.connect('/apply-publish-list', controller='FeedAdmin', action='ApplyPublishList')

    map.connect('/{action}', controller='hello')
    map.connect('/{action}/{id}', controller='hello')

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    return map
