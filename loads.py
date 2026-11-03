import json

def ler_idioma():
    with open("config.json", "r", encoding="utf-8") as file:
        idioma = json.load(file)["idioma"]
    return idioma

def ler_texto(directe):
    with open(directe, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def ler_autor(directe):
    with open(directe, "r", encoding="utf-8") as arquivo:
        autor = json.load(arquivo)["autor"]
    return autor