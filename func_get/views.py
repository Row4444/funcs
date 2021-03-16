from rest_framework.response import Response
from rest_framework.views import APIView
from .services import Functions


class StartAPIView(APIView):
    def get(self, request):
        try:
            f = Functions(**request.GET)
            return Response({"result": [*f.result]})
        except:
            return Response(status=204)
