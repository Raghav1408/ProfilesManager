from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^HelloView',views.HelloApiView.as_view()),
]
