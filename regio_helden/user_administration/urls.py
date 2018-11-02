from django.conf.urls import url
from user_administration import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^profile/$', views.update_profile),
    url(r'^account/logout/$', views.Logout),
]
