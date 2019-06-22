from django.shortcuts import render
from .models import Query
# Create your views here.
def query(request):
    queries = Query.objects.all()

    return render(request, 'search/query.html', {'queries':queries})