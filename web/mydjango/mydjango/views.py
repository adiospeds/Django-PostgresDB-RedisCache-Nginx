from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request):
    return HttpResponse("Hello, world!")
