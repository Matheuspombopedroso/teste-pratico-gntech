import json
import os
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError

from django.shortcuts import redirect, render

from .models import Previsao

LAT = -27.5969
LON = -48.5489


def inicio(request):
    erro = None
    if request.method == "POST":
        try:
            _salvar_tempo_atual()
            return redirect("clima:inicio")
        except (HTTPError, URLError, KeyError, TimeoutError) as exc:
            erro = f"Não foi possível consultar o tempo: {exc}"

    return render(
        request,
        "clima/inicio.html",
        {
            "previsoes": Previsao.objects.all(),
            "latitude": LAT,
            "longitude": LON,
            "erro": erro,
        },
    )


def _salvar_tempo_atual():
    params = urllib.parse.urlencode(
        {
            "lat": LAT,
            "lon": LON,
            "appid": os.environ["API_KEY_OPENWEATHER"],
            "units": "metric",
            "lang": "pt_br",
        }
    )
    url = f"https://api.openweathermap.org/data/2.5/weather?{params}"
    with urllib.request.urlopen(url, timeout=15) as response:
        data = json.load(response)

    
    clima = data["weather"][0]
    Previsao.objects.create(
    latitude=LAT,
    longitude=LON,
    temperatura=data["main"]["temp"],
    sensacao=data["main"]["feels_like"],
    umidade=data["main"]["humidity"],
    vento=data["wind"]["speed"],
    descricao=clima["description"],
)