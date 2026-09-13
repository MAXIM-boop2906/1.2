import csv
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # 1. Читаем CSV-файл по пути из настроек
    csv_path = settings.BUS_STATION_CSV
    stations_list = []

    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stations_list.append(row)

    # 2. Создаём пагинатор: по 10 записей на страницу
    paginator = Paginator(stations_list, 10)

    # 3. Получаем номер страницы из GET-параметра
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 4. Формируем контекст и рендерим шаблон
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'stations/index.html', context)