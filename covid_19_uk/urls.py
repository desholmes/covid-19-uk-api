from rest_framework import routers
from covid_19_uk.api.views.uk_totals import UkTotalViewSet
from covid_19_uk.api.views.scotland_totals import ScotlandTotalViewSet

router = routers.DefaultRouter()
router.register(r'uk/totals',
                UkTotalViewSet,
                basename='uk/totals')
router.register(r'scotland/totals',
                ScotlandTotalViewSet,
                basename='scotland/totals')
urlpatterns = router.urls
