from django.shortcuts import render
from .forms import SubscriberForm
from pycbrf.toolbox import ExchangeRates

def landing(request):
    name = "CodingMedved"
    current_day = "03.01.2017"
    form = SubscriberForm(request.POST or None)
    rates = ExchangeRates('2020-03-24')
    dollar = int(rates['USD'].value) * 5.73

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())
