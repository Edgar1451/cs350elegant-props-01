from django.conf.urls import url

from . import views

app_name = 'messenger'

urlpatterns = [
    url(r'^$', views.MessageListView.as_view(), name='list'),
]
