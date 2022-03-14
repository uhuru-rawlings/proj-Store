from django.shortcuts import render,redirect
from profiles.models import Projects, Userbio, Rated
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RatedSerializer, PostSerializer, UserbioSerializer
from django.shortcuts import get_object_or_404
from signups.models import Usersignup
# Create your views here.
def profiles_view(request):
    try:
        user = request.COOKIES['logedin']
        users = Usersignup.objects.get(useremail=user)
    except:
        return redirect('/login/')
    try:
        projects = Projects.objects.filter(user= users).order_by('-id')
    except:
        projects = "None"
    try:
        bio = Userbio.objects.get(user=users)
    except:
        bio = "nobio"
    context = {
        'title': 'project store | profile',
        'users':users,
        'bio':bio,
        'projects':projects
    }
    return render(request, "profile.html", context)

def save_projectView(request):
    if request.method == 'POST':
        try:
            user = request.COOKIES['logedin']
            users = Usersignup.objects.get(useremail=user)
        except:
            return redirect('/login/')
        projecttitle = request.POST['projecttitle']
        livelinks = request.POST['livelinks']
        projectscreenshort = request.FILES['projectscreenshort']
        descriptions = request.POST['descriptions']

        new_project = Projects(user = users,proj_title = projecttitle,project_link = livelinks, project_image = projectscreenshort,project_description = descriptions)
        new_project.save()
        return redirect('/profile/')

def save_bioView(request):
    if request.method == 'POST':
        bion = request.POST['biotext']
        try:
            user = request.COOKIES['logedin']
            users = Usersignup.objects.get(useremail=user)
        except:
            return redirect('/login/')
        check_bio = Userbio.objects.filter(user=users).exists()
        if check_bio:
            bios = Userbio.objects.filter(user=users)
            bios.update(bio = bion)
            return redirect('/profile/')
        else:
            new_bio = Userbio(user=users, bio=bion)
            new_bio.save()

            return redirect('/profile/')

class ProjectViews(APIView):
    def get(self, request):
        proj_title = request.query_params.get('proj_title', None)
        projects = Projects.objects.all()
        if proj_title:
            projects = Projects.filter(proj_title = proj_title)
        if projects:
            selialized = PostSerializer(projects, many = True)
            return Response(selialized.data)
        else:
            return Response({})

class UserbioView(APIView):
    def get(self, request):
        bios = Userbio.objects.all()
        if bios:
            serialized = UserbioSerializer(bios, many = True)
            return Response(serialized.data)
        else:
            return Response({})

class RatedView(APIView):
    def get(self, request):
        reteds = Rated.objects.all()
        if reteds:
            serialized = RatedSerializer(reteds, many = True)
            return Response(serialized.data)
        else:
            return Response({})