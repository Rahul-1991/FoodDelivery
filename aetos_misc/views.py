from rest_framework.views import APIView
from .service import MiscService
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK


class AssignTruckView(APIView):

    def post(self, request):
        print request.data
        location_list = request.data.get('locations')
        result = MiscService().get_suitable_trucks(location_list)
        return JsonResponse(data={'s': 1, 'm': 'selected trucks for location', 'd': result}, status=HTTP_200_OK)
