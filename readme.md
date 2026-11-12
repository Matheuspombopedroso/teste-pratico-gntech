# Teste para desenvolvedor pleo GnTech
12872373 - Desenvolvedor de Software Pleno

Esse repositório foi feito para demonstração de conhecimentos em Django, Python, Postgres e Docker.

Criei um sistema simples, utilizando docker compose, que cria um banco de dados Postgres e conteineriza o Django. O app faz o get na api openweather através do clique de um botão, e também salva os dados no banco, utilizando a mesma função:

```def inicio(request):
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
)```