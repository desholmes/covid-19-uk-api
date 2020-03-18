from rest_framework.response import Response
from rest_framework import viewsets, status

from .serializers.case_serializer import CaseSerializer
from .utils import get_case_instances_by_date
from .utils import get_df_from_url
from .utils import get_cases_from_df

url = 'https://raw.githubusercontent.com/tomwhite/covid-19-uk-data/\
master/data/covid-19-cases-uk.csv'
# url = './data/covid-19-cases-uk.csv'

df = get_df_from_url(url)
cases = get_cases_from_df(df)


class UkCasesViewSet(viewsets.ViewSet):

    def list(self, request):
        serializer = CaseSerializer(
            instance=cases.values(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            totalInstances = get_case_instances_by_date(pk, df)
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = CaseSerializer(instance=totalInstances.values(),
                                    many=True)
        return Response(serializer.data)
