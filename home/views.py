from django.shortcuts import render


# Create your views here.

# TODO add search engine which will display recently added material
def index_view(request):
    return render(request, "index.html")
