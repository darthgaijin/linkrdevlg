from django.shortcuts import render


# Create your views here.
def userProfile(request):
    context = {}
    return render(request, 'core/landing-page.html', context)

