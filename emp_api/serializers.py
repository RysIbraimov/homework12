from rest_framework import serializers

from .models import Position,Employees,User

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=30, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли дожлны совподать')
        return data

    def create(self, validated_data):
        user = User(username=validated_data['username'],)
        user.set_password(validated_data['password'])
        user.save()
        return user

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        #read_only_fields =