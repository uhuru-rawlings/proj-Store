from django.shortcuts import render
from profiles.models import Projects, Userbio, Rated
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RatedSerializer, PostSerializer, UserbioSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
def profiles_view(request):
    context = {
        'title': 'project store | profile'
    }
    return render(request, "profile.html", context)


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