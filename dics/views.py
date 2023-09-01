from django.shortcuts import render
from .models import Word
from django.http import HttpResponse,HttpResponseRedirect
from .forms import SearchForm
from django.db.models import Q


def searchView(request):
    form = SearchForm(request.GET)
    meanings = []  # Store the meanings of matching words
    context = {'form': form, 'meanings': meanings}  # Updated context key

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        matching_words = Word.objects.filter(Q(word__iexact=search_query) | Q(urdu__iexact=search_query))

        for word in matching_words:
            if word.word.lower() == search_query.lower():
                meanings.append(word.urdu)
            if word.urdu.lower() == search_query.lower():
                meanings.append(word.word)

    context['meanings'] = meanings  # Update the context key for meanings
    return render(request, 'dics/search.html', context)




