from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UsersAPI
from .serializers import UsersAPISerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class UsersAPIView(APIView):
    def get(self,request):
        #print(request.data)
        queryset=UsersAPI.objects.filter(Email=request.data.get('Email'))
        if queryset:
            if queryset.values('Password').first()['Password']==request.data.get('Password'):
                return Response("You are Successfully Logged in")
            else:
                return Response("Password is Incorrect")
        else:
            return Response("User is not Registered")

        
        return Response("Working")



    def post(self,request):
        queryset=request.data
        serializer=UsersAPISerializer(data=queryset,partial=True)
        if serializer.is_valid(raise_exception=True):
            save_data=serializer.save()
        return Response({"Success":"User '{}' created Successfully".format(save_data.Name)})
    
    def put(self, request, pk):
        queryset = get_object_or_404(UsersAPI.objects.all(), pk=pk)  

       
        parsed_data = request.data 
        serializer = UsersAPISerializer(instance=queryset, data=parsed_data, partial=True)

        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()
        return Response ({"Success":"User '{}' updated successfully".format(save_data.Name)})

    def delete(self, request, pk):
        queryset = get_object_or_404(UsersAPI.objects.all(), pk=pk)
        queryset.delete()
        return Response ({"Suucess":"User with id '{}' deleted successfully".format(pk)})
