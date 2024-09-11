from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Shabrina Aulia Kinanti',
        'npm' : '2306245472',
        'class': 'PBP B',
        'product_name' : 'Liptint',
        'price': '600.000',
        'description': 'NEW Liptint with high formula',
        'rating' : '4.5/5.0'
    }

    return render(request, "main.html", context)
