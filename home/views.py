from django.shortcuts import render
from django.http import JsonResponse
from home.models import Newslatter

# Create your views here.
def home_view(request):
    # if request.method == 'POST':

    context = {
        'title':'Project-Store | Django'
    }
    return render(request, "index.html", context)

def signupnews_view(request):
    useremail = request.POST['useremail']
    new_email = Newslatter(useremail = useremail)
    new_email.save()
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)