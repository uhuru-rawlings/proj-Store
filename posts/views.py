from django.shortcuts import render

# Create your views here.
def allpost_view(request):
    context = {
        'title': 'project store | all posts'
    }
    return render(request, "posts.html", context)