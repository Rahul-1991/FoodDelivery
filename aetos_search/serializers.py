# from rest_framework import serializers
# from aetos_search import models
#
#
# class DeliveryModelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.DeliveryModel
#         exclude = ()
#
#     def restore_object(self, attrs, instance=None):
#         if instance is not None:
#             for k, v in attrs.iteritems():
#                 setattr(instance, k, v)
#             return instance
#         return models.DeliveryModel(**attrs)
