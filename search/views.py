from django.shortcuts import render
from django.db.models import Q
from catalog.models import Product
from django.http import JsonResponse



def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups = Q(name__icontains=query)

            results = Product.objects.filter(lookups).distinct()

            context ={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search_results.html', context)

        else:
            return render(request, 'search_results.html')

    else:
        return render(request, 'search_results.html')

