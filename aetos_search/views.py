from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK
from aetos_search.service import SearchService
from common_utils.utils import process_params


class NameSearch(APIView):

    param_config = {
        'type': 'object',
        'properties': {
            'applicantName': {
                'type': 'string'
            }
        },
        'required': ['applicantName']
    }

    @process_params(param_config=param_config)
    def get(self, request, params):
        applicant_name = params.get('applicantName')
        result_set = SearchService().get_filtered_names(applicant_name)
        return JsonResponse(data={'s': 1, 'm': 'Name Search Result', 'd': result_set}, status=HTTP_200_OK)


class StreetSearch(APIView):
    param_config = {
        'type': 'object',
        'properties': {
            'streetName': {
                'type': 'string'
            }
        },
        'required': ['streetName']
    }

    @process_params(param_config=param_config)
    def get(self, request, params):
        street_name = params.get('streetName')
        result_set = SearchService().get_filtered_streets(street_name)
        return JsonResponse(data={'s': 1, 'm': 'Street Search Result', 'd': result_set}, status=HTTP_200_OK)


class ExpiredPermitsSearch(APIView):

    def get(self, request):
        result_set = SearchService().get_expired_permits()
        return JsonResponse(data={'s': 1, 'm': 'Expired Permit Results', 'd': result_set}, status=HTTP_200_OK)
