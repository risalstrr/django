from django.shortcuts import render

def artikelIndexView(request):
    context = {
        'page_title' :'Artikel',
    }
    return render(request, 'artikel/index.html', context)
