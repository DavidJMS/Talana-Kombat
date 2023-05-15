from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from apps.core.serializers import CombatSerializer


# Create your views here.
class FightViewSet(APIView):
    def post(self, request):
        # Seteamos la data
        data: dict = request.data
        serializer = CombatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        energy_1, energy_2, champion, history = serializer.save()
        return Response(
            {
                "message": "Funciona!",
                "data": {
                    "energ_1": energy_1,
                    "energy_2": energy_2,
                    "campeon": champion,
                    "history": history,
                },
            },
            status=HTTP_200_OK,
        )
