from django.conf.urls import url
from user_administration import views
from user_administration.forms import CustomUserForm

urlpatterns = [
    url(r'^$', CustomUserForm.custom_user_list, name='custom_user_list'),
    url(r'^add/user$', CustomUserForm.custom_user_create, name='create_user'),
    url(r'^update/user/(?P<pk>[0-9]+)/$', CustomUserForm.custom_user_update,
        name='update_user'),
    url(r'^delete/user/(?P<pk>[0-9]+)/$', CustomUserForm.custom_user_delete,
        name='delete_user'),
    url(r'^account/logout/$', views.Logout),
]
