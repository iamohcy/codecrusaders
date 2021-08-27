from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hw2.views.home', name='home'),
    # url(r'^hw2/', include('hw2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_knights, name='login_knights'),
    url(r'^home/$', views.home, name='home'),

    # url(r'^logout/$', views.logout_knights, name='logout_knights'),
    # url(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
    # url(r'^send_password_reset/$', views.send_password_reset, name='send_password_reset'),
    # url(r'^reset_password_page/$', views.reset_password_page, name='reset_password_page'),
    # url(r'^reset_password/$', views.reset_password, name='reset_password'),
    # url(r'^change_password/$', views.change_password, name='change_password'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^verify/$', views.verify, name='verify'),
    # url(r'^profile/$', views.self_profile, name='self_profile'),
    # url(r'^profile/(?P<username>.+)/$', views.profile, name='profile'),
    # url(r'^post_grumb/$', views.post_grumb, name='post_grumb'),
    # url(r'^dislike_grumb/$', views.dislike, {'source': 'grumb'}, name='dislike_grumb'),
    # url(r'^dislike_comment/$', views.dislike, {'source': 'comment'}, name='dislike_comment'),
    # url(r'^undislike_grumb/$', views.undislike, {'source': 'grumb'}, name='undislike_grumb'),
    # url(r'^undislike_comment/$', views.undislike, {'source': 'comment'}, name='undislike_comment'),
    # url(r'^post_comment/$', views.post_comment, name='post_comment'),
    # url(r'^follow/$', views.follow, name='follow'),
    # url(r'^block/$', views.block, name='block'),
    # url(r'^unfollow/$', views.unfollow, name='unfollow'),
    # url(r'^unblock/$', views.unblock, name='unblock'),
    # url(r'^search/$', views.search_grumb, name='search_grumb'),
    # url(r'^update_profile/(?P<section>.+)/$', views.update_profile, name='update_profile'),
    # url(r'^update_follower_grumbs/$', views.update_follower_grumbs, name='update_follower_grumbs'),

    # url(r'^post_comment/(?P<grumb_id>\d+)/$', views.post_comment, name='post_comment'),
)
