from rest_framework.response import Response
from rest_framework import viewsets

from .serializers.total_serializer import TotalSerializer
from .utils import get_totals_by_date
from .utils import get_df_from_url
from .utils import get_totals_from_df

url = 'https://raw.githubusercontent.com/tomwhite/covid-19-uk-data/\
master/data/covid-19-totals-northern-ireland.csv'


df = get_df_from_url(url)
totals = get_totals_from_df(df)


class NorthernIrelandTotalViewSet(viewsets.ViewSet):

    def list(self, request):
        date = self.request.query_params.get('date')
        returnTotals = totals
        if date:
            returnTotals = get_totals_by_date(date, df)
        serializer = TotalSerializer(
            instance=returnTotals.values(), many=True)
        return Response(serializer.data)
