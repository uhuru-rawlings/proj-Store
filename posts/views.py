from django.shortcuts import render, redirect
from profiles.models import Projects
# Create your views here.
def allpost_view(request):
    try:
        user = request.COOKIES['logedin']
    except:
        return redirect('/login/')
    try:
        projects = Projects.objects.all().order_by('-id')
    except:
        projects = "None"
    context = {
        'title': 'project store | all posts',
        'projects':projects
    }
    return render(request, "posts.html", context)


def search_view(request):
    if request.method == 'POST':
        projname = request.POST['searcjproject']
        try:
            projects = Projects.objects.filter(proj_title=projname).order_by('-id')
        except:
            projects = "None"
        context = {
            'title': 'result for' + projname ,
            'projects':projects
        }
        return render(request, "search.html", context)
