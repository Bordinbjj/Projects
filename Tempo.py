import requests

def obter_previsao_tempo(api_key, cidade):
    # URL da API da OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric'

    # Requisição à API
    resposta = requests.get(url)
    dados = resposta.json()

    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        # Extraindo informações relevantes
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']

        # Exibindo a previsão do tempo
        print(f'Temperatura em {cidade}: {temperatura}°C')
        print(f'Condição: {descricao}')
    else:
        print(f'Erro ao obter a previsão do tempo. Código de erro: {resposta.status_code}')

if __name__ == "__main__":
    # Substitua 'SUA_API_KEY' pela chave da API OpenWeatherMap
    api_key = 'SUA_API_KEY'
    cidade = input('Digite o nome da cidade: ')

    obter_previsao_tempo(api_key, cidade)

