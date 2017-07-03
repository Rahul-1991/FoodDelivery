from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK
from aetos_search.service import SearchService


class NameSearch(APIView):

    def get(self, request):
        applicant_name = request.GET.get('applicantName')
        result_set = SearchService().get_filtered_names(applicant_name)
        return JsonResponse(data={'s': 1, 'm': 'Name Search Result', 'd': result_set}, status=HTTP_200_OK)


class StreetSearch(APIView):

    def get(self, request):
        street_name = request.GET.get('streetName')
        result_set = SearchService().get_filtered_streets(street_name)
        return JsonResponse(data={'s': 1, 'm': 'Street Search Result', 'd': result_set}, status=HTTP_200_OK)


class ExpiredPermitsSearch(APIView):

    def get(self, request):
        result_set = SearchService().get_expired_permits()
        return JsonResponse(data={'s': 1, 'm': 'Expired Permit Results', 'd': result_set}, status=HTTP_200_OK)

