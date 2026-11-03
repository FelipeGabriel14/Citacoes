from pathlib import Path
import loads
import Random

raiz = Path(__file__).parent.parent
caminho_config = raiz / "config.json"
idioma = loads.ler_idioma(caminho_config)
caminho = Path(raiz) / "citacoes" / f"{idioma}"

files = list(caminho.glob("*.txt"))
winner = Random.sortear(files)
caminho_do_arquivo = winner
arquivo = loads.ler_texto(caminho_do_arquivo)
pasta_autor = Path(raiz) / "citacoes" / "autores" / winner.name
caminho_do_autor = pasta_autor.with_suffix(".json")
autor = loads.ler_autor(caminho_do_autor)
print(arquivo)
print(f"""
- {autor}
""")