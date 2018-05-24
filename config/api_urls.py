from rest_framework import routers

from mp_resource.playgrounds.api.viewsets import GroupViewSet

app_name = "apis"
router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet, base_name='group')

urlpatterns = router.urls
