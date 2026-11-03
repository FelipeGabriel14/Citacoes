from pathlib import Path
import loads
import Random

idioma = loads.ler_idioma()
caminho = Path(f"citacoes/{idioma}")

files = list(caminho.glob("*.json"))
winner = Random.sortear(files)
caminho_do_arquivo = winner
arquivo = loads.ler_arquivo(caminho_do_arquivo)

print(f"""
{arquivo["texto"]}

- {arquivo["autor"]}
""")