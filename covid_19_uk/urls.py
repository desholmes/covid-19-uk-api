from rest_framework import routers
from covid_19_uk.api.views import UkTotalViewSet

router = routers.DefaultRouter()
router.register(r'uk/totals',
    UkTotalViewSet,
    basename='uk/totals')
urlpatterns = router.urls
