import requests
import json

req=None

def requisicao(tit):
    try:
        tit2 = tit.replace(" ", "+")
        # print(tit2)
        req = requests.get("http://www.omdbapi.com/?t=" + tit2 + "&apikey=fedc1749")
        dic = json.loads(req.text)
        return dic
    except:
        print("num deu")
        return None
def print_det(filme):
    print(filme["Title"] + "\n" + filme["Year"] + "\n" + filme["Director"] + "\n" + filme[
        "imdbRating"])

sair = False

while not sair:
    filme = input()
    if filme == "SAIR":
        sair = True
    else:
        pesquisa = requisicao(filme)
        if pesquisa["Response"] == "False":
            print("Filme nao encontrado"+"\n")
        else:
            print_det(pesquisa)
            print("")