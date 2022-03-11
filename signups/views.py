from django.shortcuts import render

# Create your views here.
def signup_view(request):
    context = {
        'title':'registration',
    }
    return render(request, "signup.html", context)