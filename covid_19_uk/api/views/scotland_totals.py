from rest_framework.response import Response
from rest_framework import viewsets, status

from .serializers.total_serializer import TotalSerializer
from .utils import get_total_instance_by_date
from .utils import get_df_from_url
from .utils import get_totals_from_df

url = 'https://raw.githubusercontent.com/tomwhite/covid-19-uk-data/\
master/data/covid-19-totals-scotland.csv'
# url = './data/covid-19-totals-scotland.csv'

df = get_df_from_url(url)
totals = get_totals_from_df(df)


class ScotlandTotalViewSet(viewsets.ViewSet):

    def list(self, request):
        serializer = TotalSerializer(
            instance=totals.values(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            totalInstance = get_total_instance_by_date(pk, df)
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = TotalSerializer(instance=totalInstance)
        return Response(serializer.data)
