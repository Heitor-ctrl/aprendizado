import requests
def verificacao():
    try:
        response = requests.get("https://www.google.com")
    except requests.ConnectionError:
        print('Erro de conexão.')
    else:
        print('Site ativo')


verificacao()
#SOLUÇÃO GUANABARA
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.google.com')
except:
    print('Deu erro')
else:
    print('Tudo ok.')