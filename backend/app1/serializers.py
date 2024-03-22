from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(read_only=True, format='%d-%m-%Y %H:%M:%S')
    name = serializers.HiddenField(default=serializers.CurrentUserDefault())
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'

    def get_student_name(self, obj):
        return obj.name.username