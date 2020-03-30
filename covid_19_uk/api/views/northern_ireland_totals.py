from rest_framework.response import Response
from rest_framework import viewsets

from .serializers.total_serializer import TotalSerializer
from .utils import get_totals_by_date, get_df_from_url, get_totals_from_df

url = 'https://raw.githubusercontent.com/tomwhite/covid-19-uk-data/\
master/data/covid-19-totals-northern-ireland.csv'


class NorthernIrelandTotalViewSet(viewsets.ViewSet):

    def list(self, request):
        df = get_df_from_url(url)
        totals = get_totals_from_df(df)
        date = self.request.query_params.get('date')
        if date:
            totals = get_totals_by_date(date, df)
        serializer = TotalSerializer(
            instance=totals.values(), many=True)
        return Response(serializer.data)
