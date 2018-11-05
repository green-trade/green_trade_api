from django.http import HttpResponse
# from django.shortcuts import render

from inventory.models import Invetory


def index(request):
    ''''''

    latest = Invetory.objects.orde

    return HttpResponse("fuck you")
