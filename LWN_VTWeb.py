import json
import os
from virus_total_apis import PublicApi


def analizar(url):
    """Esta función recibe 1 parámetro para analizar una dirección web y ver si es segura o no:
        [url] = Dirección web a analizar"""
    cwd = os.getcwd()
    try:
        api_key = ("8bde52cf2c7050f4944b055fe91ac7249b0f47e2ceab9a7530548356" +
        "ca6c0e3c")
        api = PublicApi(api_key)
        response = api.get_url_report(url)

        x = url.split(".")

        with open(x[1] + ".txt", "w") as f:
            json.dump(response, f, indent=4)

        print("Se ha guardado la información del análisis en: " + cwd + "\\" +
              x[1] + ".txt")
    except:
        print("No fue posible concluir el análisis.")
