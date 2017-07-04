from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK
from aetos_addOrRemove.service import AddRemoveService


class CreateFoodTruck(APIView):

    def post(self, request):
        document = dict(request.data)
        insert_success = AddRemoveService().insert_new_document(document)
        if insert_success:
            return JsonResponse(data={'message': 'Document inserted successfully'}, status=HTTP_200_OK)
        else:
            return JsonResponse(data={'message': 'Error in inserting documnet'}, status=HTTP_200_OK)


class RemoveFoodTruck(APIView):

    def delete(self, request):
        query = dict(request.data)
        delete_success = AddRemoveService().delete_document(query)
        if delete_success:
            return JsonResponse(data={'message': 'Document deleted successfully'}, status=HTTP_200_OK)
        else:
            return JsonResponse(data={'message': 'Error in deleting documnet'}, status=HTTP_200_OK)


