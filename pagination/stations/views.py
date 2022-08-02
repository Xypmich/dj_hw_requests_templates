from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    data_list = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as f:
        data = csv.DictReader(f)
        for row in data:
            data_list.append(row)
    paginator = Paginator(data_list, 15)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': paginator.page(page_number),
        'page': page
    }
    return render(request, 'stations/index.html', context)
