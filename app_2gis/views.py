from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from .models import Path


def index(request):
    return render(request, "index.html", context={})


class Coord(APIView):
    def get(self, request):
        coords = Path.objects.all()
        return Response({"coords": coords})
