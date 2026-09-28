import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from wordcount import contar


class TestWordcount(unittest.TestCase):
    def test_contar(self):
        casos = (
            (b"", (0, 0, 0)),
            (b"a b", (0, 2, 3)),
            ("olá mundo\nsegunda linha\n".encode("utf-8"), (2, 4, 24)),
            (b"a\r\nb\r\n", (2, 2, 6)),
        )
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = Path(pasta) / "entrada.txt"
            for conteudo, esperado in casos:
                with self.subTest(conteudo=conteudo):
                    arquivo.write_bytes(conteudo)
                    self.assertEqual(contar(arquivo), esperado)

    def test_linha_de_comando(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = Path(pasta) / "entrada.txt"
            arquivo.write_bytes("olá mundo\nsegunda linha\n".encode("utf-8"))
            script = Path(__file__).with_name("wordcount.py")
            resultado = subprocess.run(
                [sys.executable, str(script), str(arquivo)],
                capture_output=True, text=True, check=True,
            )
            self.assertEqual(resultado.stdout, f"2 4 24 {arquivo}\n")


if __name__ == "__main__":
    unittest.main()
