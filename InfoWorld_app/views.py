import base64
from django.shortcuts import render
from components.infoworld import Infoworld

# Create your views here.

def homepage(request):
    return render(request, './home.html')
def infoworld(request):
    return render(request, './infoworld.html')
def get_text(request):
    if request.method == "POST":
        country = request.POST["search"]
        country_data, country_code = Infoworld().get_country_information(country)
        if country_data['error'] != '':
            data = {
                'error':'There was error in your request, please check spelling.'
            }
        else:
            population = "{:,}".format(country_data['population'])
            data = {
                'name':country_data['name'],
                'capital':country_data['capital'],
                'population':population,
                'currency_name':country_data['currency_name'],
                'currency_symbol':country_data['currency_symbol'],
                'border_length':country_data['border_length'],
                'few_borders':country_data['few_borders'],
                'many_borders':country_data['many_borders'],
                'countrycode':country_code
            }
        return render(request, './home.html', context=data)
