from pathlib import Path
import loads
import random

raiz = Path(__file__).parent.parent
caminho_config = raiz / "config.json"
idioma = loads.ler_idioma(caminho_config)
caminho = Path(raiz) / "citacoes" / f"{idioma}"

files = list(caminho.glob("*.txt"))
if files:

 winner = random.choice(files)
 arquivo = loads.ler_texto(winner)
 autor = None

 try:
    pasta_autor = Path(raiz) / "citacoes" / "autores" / winner.name
    caminho_do_autor = pasta_autor.with_suffix(".json")
    autor = loads.ler_autor(caminho_do_autor)
 except FileNotFoundError:

   print("Error: The author does not exist or the folder does not exist")
 if not arquivo or autor == None:
   print("Error: The selected quote is incomplete or some files are missing")
   exit()
 print(arquivo)
 print(f"\n- {autor}")
else:
   print("There are no quotes to read.")
