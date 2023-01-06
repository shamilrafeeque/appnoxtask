from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Account
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        print(user)
        print('4444444444444444444444444')
        token = super().get_token(user)
        print('**********************************9999999999999999')
        print(user.email)
        print(token)

        # Add custom claims
       
       
       
        token['is_superuser'] = user.is_superuser
        token['email'] = user.email
        token['is_active'] = user.is_active
        
      

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    print('77777777777777777777777777')
    serializer_class = MyTokenObtainPairSerializer



class Register(APIView):  
     def post(self,request):
        data = request.data
       
        serializer = UserSerializer(data=data)
        
        if serializer.is_valid():
                serializer.save()
                print("@@@@@*************************")
                print(serializer.data)
                phone_number=data['mobile']
                print(phone_number,'oooooooooooooooooooooooooo')
               
                

                response={
                    "messages" : "User Created Successfully",
                    "data" : serializer.data
                }
                
                return Response(data= response, status = status.HTTP_201_CREATED)
            
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
        
        
# @api_view(['GET'])
# def Logout(request,id):
#    ids =Account.objects.get(id=id)
#    if id==ids:
#        print("hii")
#        print(ids)
#        ids.is_active= False
#        ids.save()
#        serializer = LoginSerializer(ids, many=False)
#        return Response(serializer.data)
#    message = {'detail':'somthin whent worng'}
#    return Response(message, status=status.HTTP_400_BAD_REQUEST)
       
       
       