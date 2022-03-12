from django.shortcuts import render,redirect
from signups.models import Usersignup
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsersignupSerializer
from django.shortcuts import get_object_or_404
import requests
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        useremail = request.POST['useremails']
        phone = request.POST['phoneno']
        userimage = request.FILES['userimages']
        passwords = request.POST['userpassword']
        userdate = Usersignup(username=username,useremail=useremail,phone=phone,userimage=userimage,passwords=passwords)
        # data = {'username':username,'useremail':useremail,'phone':phone,'userimage':userimage,'password':passwords}
        # headers = {'Content-Type': 'application/json'}
        # read = requests.post('http://127.0.0.1:8080/get_registreation/', json= data,headers = headers)
        userdate.save()
        return redirect('/login/')
    context = {
        'title':'registration',
    }
    return render(request, "signup.html", context)

class SignupView(APIView):
    def get(self, request):
        useremails = request.query_params.get('useremail', None)
        users = Usersignup.objects.all()
        if useremails:
            users = Usersignup.filter(useremail = useremails)
        if users:
            serialized = UsersignupSerializer(users, many = True)
            return Response(serialized.data)
        else:
            return Response({})

    def post(self,request, *args, **kwargs):
        
        serializer = UsersignupSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

