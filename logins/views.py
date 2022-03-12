from django.shortcuts import render,redirect
from signups.models import Usersignup

# Create your views here.
def login_view(request):
    error = ''
    if request.method == 'POST':
        useremail = request.POST['useremails']
        userpassword = request.POST['userpassword']
        try:
            get_user = Usersignup.objects.get(useremail = useremail)
            if get_user.passwords == userpassword:
                response = redirect('/allposts/')
                response.set_cookie("logedin", useremail)
                return response
            else:
                error = "Wrong password, please check and try again"
        except:
            error = useremail + " " + "does not exist"
    context = {
        'title':'login',
        "error":error
    }
    return render(request, "login.html", context)