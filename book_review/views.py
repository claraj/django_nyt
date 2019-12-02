from django.shortcuts import render
from django.contrib import messages 
from django.shortcuts import HttpResponseRedirect

from .forms import BookSearchForm
from . import booksearch 

def search_author(request):

    # If POST request, process form data
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            reviews = booksearch.search_reviews_by_author(author)
            if reviews is not None:
                return render(request, 'book_review/reviews.html', {'author': author, 'reviews': reviews})
            else:
                # error connecting to API. Show flash message in template
                messages.add_message(request, messages.ERROR, 'Sorry, could not connect to New York Times API.')
                
    else: 
        form = BookSearchForm()
    
    return render(request, 'book_review/search.html', {'form': form})




