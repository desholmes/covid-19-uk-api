from rest_framework import routers
from covid_19_uk.api.views.uk_totals import UkTotalViewSet
from covid_19_uk.api.views.uk_cases import UkCasesViewSet
from covid_19_uk.api.views.scotland_totals import ScotlandTotalViewSet
from covid_19_uk.api.views.wales_totals import WalesTotalViewSet
from covid_19_uk.api.views.\
    northern_ireland_totals import NorthernIrelandTotalViewSet

router = routers.DefaultRouter()
router.register(r'uk/totals',
                UkTotalViewSet,
                basename='uk/totals')
router.register(r'uk/cases',
                UkCasesViewSet,
                basename='uk/cases')
router.register(r'scotland/totals',
                ScotlandTotalViewSet,
                basename='scotland/totals')
router.register(r'wales/totals',
                WalesTotalViewSet,
                basename='wales/totals')
router.register(r'northern-ireland/totals',
                NorthernIrelandTotalViewSet,
                basename='northern-ireland/totals')
urlpatterns = router.urls
