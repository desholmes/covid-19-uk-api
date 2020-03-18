from rest_framework.response import Response
from rest_framework import viewsets, status
import pandas as pd

from . import serializers
from . import UkTotal

# df = pd.read_csv('./data/covid-19-totals-uk.csv')
df = pd.read_csv('https://raw.githubusercontent.com/tomwhite/covid-19-uk-data/master/data/covid-19-totals-uk.csv')

totals = {}

for i in range(len(df)):
    totals[i] = UkTotal(date=df.loc[i, "Date"],
                             tests=df.loc[i, "Tests"],
                             confirmed_cases=df.loc[i, "ConfirmedCases"],
                             deaths=df.loc[i, "Deaths"])
# print (df.head())


instance = df[df['Date'] == '2020-03-10']
# print('>>>>>>>> Instance head: ', instance.head(), len(instance))
# print('>>>>>>>> Instance cell: ', instance[0,'Date'])


def get_instance_by_date(date_str):
    print('>>>>>>>>>>>> date_str: ',date_str)
    instance = df[df['Date'] == date_str]
    if len(instance) == 0:
        print('>>>>>>>>>>>> KeyError',)
        raise KeyError
    print('>>>>>>>> Instance head: ', instance.head())
    print('>>>>>>>> Instance cell: ', instance[0,2])
    print('>>>>>>>> No Key Error')
    uk_instance = UkTotal(date=instance.loc[0, "Date"],
                    tests=instance.loc[0, "Tests"],
                    confirmed_cases=instance.loc[0, "ConfirmedCases"],
                    deaths=instance.loc[0, "Deaths"])
    return uk_instance
    

temp = df[df['Date'] == 'bob']

print (len(temp) == 0)

class UkTotalViewSet(viewsets.ViewSet):

    def list(self, request):
        serializer = serializers.UkTotalSerializer(
            instance=totals.values(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            totalInstance = get_instance_by_date(pk)
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.UkTotalSerializer(instance=totalInstance.value())
        return Response(serializer.data)
