from django.shortcuts import render, redirect
from profiles.models import Projects,Rated
from signups.models import Usersignup
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

def ratings_views(request):
    if request.method == 'POST':
        try:
            user = request.COOKIES['logedin']
            users = Usersignup.objects.get(useremail=user)
        except:
            return redirect('/login/')
        design = request.POST['designs']
        usability = request.POST['usability']
        content = request.POST['content']
        avarage_rated = (int(usability) + int(design) + int(content)) / 3
        postid = request.POST['retedpost']
        posts = Projects.objects.get(id = int(postid))
        try:
            getrated = Rated.objects.get(post= posts)
            totals = avarage_rated + getrated.rated_count
            getrated.update(rated_count = totals)
        except:
            new_ratings = Rated(post= posts, rated_by = users, rated_count = avarage_rated)
            new_ratings.save()
        return redirect("/allposts/")
