from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Liptint',
        'price': '600.000',
        'description': 'NEW Liptint with high formula',
        'rating' : '4.5/5.0'
    }

    return render(request, "main.html", context)
