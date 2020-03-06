from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Alex',
        'title' : 'Blog post',
        'content' : 'our post content',
        'date' : ' 24 Febr',

    },
    {
        'author': 'Max',
        'title': 'Blog post 2',
        'content': 'content 2',
        'date': ' 24 February day number 2',
    }


]


def about(request):
    return render(request, 'alexstore/about.html',{'title': 'What a beautiful day'})




def home(request):
    context = {
        'posts' : posts,
        'title':'Our tite'
    }
    return render(request, 'alexstore/home.html',context)

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#
@login_required
def profile(request):
    return render(request, 'users/profile.html')