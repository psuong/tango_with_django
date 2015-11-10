from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

#import the HttpResponse

# Tutorial Section 4.4
# Create your views here.
# def index(request):
#     return HttpResponse(" Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")

# Tutorial Section 4.4
# def index(request):
#     context_dict = {'boldmessage': 'Bold conent',
#                     'site_url': '/rango/about/',
#                     'title': 'About'}
#     return render(request, 'rango/index.html', context_dict)

# Tutorial Section 4.4
# def about(request):
#     return HttpResponse("Rango says: Here is the about page! <br/> <a href='/rango'>Index</a>")

# Exercise Section 5
def about(request):
    context_dict = {'boldmessage': 'This is the about page.',
                    'site_url': '/rango/',
                    'title': 'Index'}
    return render(request, 'rango/about.html', context_dict)

# Section 7
# templates/rango/index.html template changed
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = { 'categories': category_list }

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)
