from rest_framework.response import Response
from rest_framework import viewsets

from .serializers.case_serializer import CaseSerializer
from .utils import get_cases_by_date
from .utils import get_df_from_url
from .utils import get_cases_from_df

url = 'https://raw.githubusercontent.com/tomwhite/covid-19-uk-data/\
master/data/covid-19-cases-uk.csv'
# url = './data/covid-19-cases-uk.csv'

df = get_df_from_url(url)
cases = get_cases_from_df(df)


class UkCasesViewSet(viewsets.ViewSet):

    def list(self, request):
        date = self.request.query_params.get('date')
        returnCases = cases
        if date:
            returnCases = get_cases_by_date(date, df)
        serializer = CaseSerializer(
            instance=returnCases.values(), many=True)
        return Response(serializer.data)
