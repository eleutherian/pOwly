from django.shortcuts import render
from tutorial.models import Tutorial

# Create your views here.
def index(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'frontpage/index.html', {'tutorials':tutorials,})
