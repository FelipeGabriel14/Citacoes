import json

def ler_idioma():
    with open("config.json", "r", encoding="utf-8") as file:
        idioma = json.load(file)["idioma"]
    return idioma

def ler_arquivo(directe):
    with open(directe, "r", encoding="utf-8") as arquivo:
        conteudo = json.load(arquivo)
    return conteudo