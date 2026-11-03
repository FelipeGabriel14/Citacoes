from pathlib import Path
import loads
import Random

idioma = loads.ler_idioma()
caminho = Path(f"citacoes/{idioma}")

files = list(caminho.glob("*.txt"))
winner = Random.sortear(files)
caminho_do_arquivo = winner
arquivo = loads.ler_texto(caminho_do_arquivo)
pasta_autor = Path("citacoes/autores") / winner.name
caminho_do_autor = pasta_autor.with_suffix(".json")
autor = loads.ler_autor(caminho_do_autor)
print(arquivo)
print(f"""
- {autor}
""")