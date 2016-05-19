
#coding: utf-8
#This file is part of Ficlatté.
#Copyright (C) 2015 Paul Robertson
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of version 3 of the GNU Affero General Public
#    License as published by the Free Software Foundation
#    
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import django.contrib.auth.views
import castle.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ficlatte.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',      'castle.views.home', name='home'),
    url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'castle/login.html'}, name='signin'),
    url(r'^logout/$', castle.views.signout, name='signout'),
#    url(r'^login/$',      TemplateView.as_view(template_name='castle/login.html'), name='signin'),
#    url(r'^signin/$',     'castle.views.signin',  name='signin'),
    url(r'^logout/$',     'castle.views.signout', name='signout'),
    url(r'^dashboard/$',  'castle.views.dashboard', name='dashboard'),
    url(r'^authors/(?P<pen_name>[^/]+)/$', 'castle.views.author', name='author'),
    url(r'^authors/u/drafts/$', 'castle.views.drafts', name='drafts'),
    url(r'^authors/u/profile/$', 'castle.views.profile_view', name='profile'),
    url(r'^authors/u/submit/$', 'castle.views.submit_profile', name='submit_profile'),
    url(r'^register/$', 'castle.views.profile_view', name='register'),
    url(r'^stories/(?P<story_id>\d+)/$', 'castle.views.story_view', name='story'),
    url(r'^stories/edit/(?P<story_id>\d+)/$', 'castle.views.edit_story', name='edit_story'),
    url(r'^stories/delete/(?P<story_id>\d+)/$', 'castle.views.delete_story', name='delete_story'),
    url(r'^stories/new/$', 'castle.views.new_story', name='new_story'),
    url(r'^stories/submit/$', 'castle.views.submit_story', name='submit_story'),
    url(r'^stories/unsubscribe/(?P<story_id>\d+)/$', 'castle.views.story_unsubscribe', name='story-unsub'),
    url(r'^stories/subscribe/(?P<story_id>\d+)/$', 'castle.views.story_subscribe', name='story-sub'),
    url(r'^stories/$', 'castle.views.browse_stories', name='recent_stories'),
    url(r'^stories/active/$', 'castle.views.active_stories', name='active_stories'),
    url(r'^stories/popular/$', 'castle.views.popular_stories', name='popular_stories'),
    url(r'^prompts/$', 'castle.views.prompts', name='prompts'),
    url(r'^prompts/(?P<prompt_id>\d+)/$', 'castle.views.prompt', name='prompt'),
    url(r'^prompts/edit/(?P<prompt_id>\d+)/$', 'castle.views.edit_prompt', name='edit_prompt'),
    url(r'^prompts/new/$', 'castle.views.new_prompt', name='new_prompt'),
    url(r'^prompts/submit/$', 'castle.views.submit_prompt', name='submit_prompt'),
    url(r'^blog/$', 'castle.views.blogs', name='blogs'),
    url(r'^blog/(?P<blog_id>\d+)/$', 'castle.views.blog_view', name='blog'),
    url(r'^blog/edit/(?P<blog_id>\d+)/$', 'castle.views.edit_blog', name='edit_blog'),
    url(r'^blog/new/$', 'castle.views.new_blog', name='new_blog'),
    url(r'^blog/submit/$', 'castle.views.submit_blog', name='submit_blog'),
    url(r'^blog/unsubscribe/(?P<blog_id>\d+)/$', 'castle.views.blog_unsubscribe', name='blog-unsub'),
    url(r'^comment/submit/$', 'castle.views.submit_comment', name='submit_comment'),
    url(r'^tags/(?P<tag_name>[^/]+)/$', 'castle.views.tags', name='tags'),
    url(r'^tags/$', 'castle.views.tags_null', name='tags_null'),
    url(r'^friendship/add/(?P<user_id>\d+)/$', 'castle.views.add_friend', name='add_friend'),
    url(r'^friendship/del/(?P<user_id>\d+)/$', 'castle.views.del_friend', name='del_friend'),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^confirmation/(?P<yesno>(?:yes|no))/(?P<uid>\d+)/(?P<token>\d+)/$', 'castle.views.confirmation', name='confirmation'),
    url(r'^avatar_upload/', 'castle.views.avatar_upload', name='avatar_upload'),
    # Static-ish pages
    url(r'^(?P<template>rules\.html)$', 'castle.views.static_view', name="rules"),
    url(r'^(?P<template>privacy\.html)$', 'castle.views.static_view', name="privacy"),
    url(r'^(?P<template>help\.html)$', 'castle.views.static_view', name="help"),
)
