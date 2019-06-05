from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('HelloView1',views.HelloViewSet,base_name = 'Hello-View')
urlpatterns = [
url(r'^HelloView',views.HelloApiView.as_view()),
url(r'',include(router.urls)),
]
