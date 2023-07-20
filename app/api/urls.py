from rest_framework.routers import SimpleRouter

from api import views

router = SimpleRouter()
router.register(r"sample", views.SampleViewSet, basename="sample")
router.register(r"type", views.TypeViewSet, basename="type")
router.register(r"container", views.ContainerViewSet, basename="container")
router.register(r"location", views.LocationViewSet, basename="location")

urlpatterns = router.urls
