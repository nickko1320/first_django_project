from rest_framework import serializers

from .models import Task

class ListTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

class RetrieveTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['due_date', 'status']

class DestroyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'