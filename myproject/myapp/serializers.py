from rest_framework import serializers
from.models import student_ser

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_ser
        fields = '__all__'



