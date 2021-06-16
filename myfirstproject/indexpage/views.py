from django.shortcuts import render, HttpResponse

# Create your views here.
def index_page(request):
    return render(request, 'indexpage/index.html')