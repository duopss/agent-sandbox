import argparse


def contar(caminho):
    # ponytail: lê o arquivo inteiro na memória; se precisar, ler em blocos.
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        texto = arquivo.read()
    return texto.count("\n"), len(texto.split()), len(texto)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("caminho")
    caminho = parser.parse_args().caminho
    linhas, palavras, caracteres = contar(caminho)
    print(f"{linhas} {palavras} {caracteres} {caminho}")
