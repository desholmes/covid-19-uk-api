from rest_framework.response import Response
from rest_framework import viewsets, status

from . import serializers
from . import Test

tests = {}
tests[1] = Test(date='2020-02-20', tests=5549, confirmed_cases=9, deaths=0)
tests[2] = Test(date='2020-02-21', tests=5885, confirmed_cases=9, deaths=0)
tests[3] = Test(date='2020-02-22', tests=6152, confirmed_cases=9, deaths=0)


def get_next_task_id():
    return max(tests) + 1


class TestViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = serializers.EnglandTotalSerializer(
            instance=tests.values(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            task = tests[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.EnglandTotalSerializer(instance=task)
        return Response(serializer.data)
