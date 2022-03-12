from django.shortcuts import render, redirect

# Create your views here.
def allpost_view(request):
    try:
        user = request.COOKIES['logedin']
    except:
        return redirect('/login/')
    context = {
        'title': 'project store | all posts'
    }
    return render(request, "posts.html", context)