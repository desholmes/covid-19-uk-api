from rest_framework.response import Response
from rest_framework import viewsets

from .serializers.case_serializer import CaseSerializer
from .utils import get_cases_by_date, get_df_from_url, get_cases_from_df

url = 'https://raw.githubusercontent.com/tomwhite/covid-19-uk-data/\
master/data/covid-19-cases-uk.csv'


class UkCasesViewSet(viewsets.ViewSet):

    def list(self, request):
        df = get_df_from_url(url)
        cases = get_cases_from_df(df)
        date = self.request.query_params.get('date')
        if date:
            cases = get_cases_by_date(date, df)
        serializer = CaseSerializer(
            instance=cases.values(), many=True)
        return Response(serializer.data)
