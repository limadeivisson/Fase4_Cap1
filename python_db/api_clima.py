import requests

API_KEY = "ea031b746ad9d396118a11258a0ec0bc"
LATITUDE = "-23.5505"
LONGITUDE = "-46.6333"
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric&lang=pt_br"


def verificar_clima():
    try:
        resposta = requests.get(URL)
        dados = resposta.json()

        print("DEBUG - Resposta completa da API:")
        print(dados)

        descricao = dados["weather"][0]["description"]
        temp = dados["main"]["temp"]
        umidade = dados["main"]["humidity"]

        print(f"Clima atual em São Paulo (por coordenadas): {descricao}")
        print(f"Temperatura: {temp}°C")
        print(f"Umidade: {umidade}%")

        if "chuva" in descricao.lower():
            print("🚫 Previsão de chuva detectada. Bomba de irrigação será desligada.")
            return False
        else:
            print("✅ Clima seco. Irrigação pode ser mantida.")
            return True

    except Exception as e:
        print("Erro ao obter os dados climáticos:", e)
        return None

if __name__ == "__main__":
    verificar_clima()