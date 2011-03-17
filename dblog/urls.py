from django.conf.urls.defaults import *

urlpatterns = patterns('dblog.views',
    # Example:
    (r'^$', 'index'),
    (r'^(?P<blog_id>[a-z0-9_-]+)/$', 'readblog'),
    (r'^(?P<blog_id>[a-z0-9_-]+)/comment/$', 'comment'),
    (r'^(?P<blog_id>[a-z0-9_-]+)/comment/add/$', 'addComment'),
    (r'^(?P<blog_id>[a-z0-9_-]+)/postComment/$', 'postComment'),
    (r'^writeBlog/$', 'writeBlog'),
    (r'^postEntry/$', 'postEntry'),
)

