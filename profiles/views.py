from django.shortcuts import render

# Create your views here.
def profiles_view(request):
    context = {
        'title': 'project store | profile'
    }
    return render(request, "profile.html", context)