import json

def ler_idioma(caminho):
    with open(caminho, "r", encoding="utf-8") as file:
        idioma = json.load(file)["idioma"]
    return idioma

def ler_texto(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def ler_autor(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        autor = json.load(arquivo)["autor"]
    return autor