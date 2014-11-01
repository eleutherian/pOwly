from django.shortcuts import render
from tutorial.models import Tutorial
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    max_obj = 25
    page = 1

    #KIND OF PAGINATION: NEEDS WORK!

    #if (request.GET.get('max'))
    #    max_obj = request.GET.get('max')
    #if (request.GET.get('page'))
    #    page = request.GET.get('page')

    tutorials = Paginator(Tutorial.objects.all(), max_obj)
    return render(request, 'frontpage/index.html', {'tutorials':tutorials.page(page),})
