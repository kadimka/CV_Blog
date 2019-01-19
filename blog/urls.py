from django.conf.urls import url
from . import views
from django.contrib.auth import views as dviews


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^resume$', views.resume),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url('drafts/', views.post_draft_list, name='post_draft_list'),
    url('post/(?P<pk>\d+)/publish/', views.post_publish, name='post_publish'),
    url('post/(?P<pk>\d+)/remove/', views.post_remove, name='post_remove'),
    url('accounts/login/', dviews.LoginView.as_view(), name='login'),
    url('accounts/logout/', dviews.LogoutView.as_view(next_page='/'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)