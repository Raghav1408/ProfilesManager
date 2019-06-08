from django.conf.urls import url,include
from . import views
from rest_framework.authtoken import views as VIEW
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('HelloView',views.HelloViewSet,base_name = 'Hello-View')
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name = 'User-Login-Token')
router.register('feed',views.ProfileFeedItemViewset)
urlpatterns = [
url(r'^HelloView',views.HelloApiView.as_view()),
url(r'',include(router.urls)),
]
