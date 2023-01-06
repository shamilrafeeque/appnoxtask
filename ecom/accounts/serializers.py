from rest_framework import serializers
from .models import Account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=['username','email','mobile','password']
        
    def get_name(self,obj):
        name=obj.username
        return name

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        # Adding the below line made it work for me.
        instance.is_active = True
        if password is not None:
            # Set password does the hash, so you don't need to call make_password 
            instance.set_password(password)
            print("kkkkkkk")
        instance.save()
        return instance
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['is_active']    
        

        