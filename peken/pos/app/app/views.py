from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login,authenticate,logout

def profile_login(request):
    if request.method == 'POST':
        username=request.POST.get('username1')
        password=request.POST.get('password1')


        user=authenticate(username=username,password=password)
        if user:
            if user.is_active :
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("<h1> ACCOUNT NOT ACTIVE</h1>")
        else:
            return HttpResponse("INVALID PASSWORD OR USERNAME")
    else:
        return render(request,'user_login.html')


def profile_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def login_page(request):
    return HttpResponse("<h1> YOU ARE NOW LOG IN PAGE</h1>")


