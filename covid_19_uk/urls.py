from rest_framework import routers
from covid_19_uk.api.views import TestViewSet

router = routers.DefaultRouter()
router.register(r'tests', TestViewSet, basename='tests')
urlpatterns = router.urls
