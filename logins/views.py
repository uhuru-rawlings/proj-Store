from django.shortcuts import render

# Create your views here.
def login_view(request):
    context = {
        'title':'login',
    }
    return render(request, "login.html", context)