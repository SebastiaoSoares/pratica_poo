from livros import Livro
from usuarios import Usuario

class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.usuario = usuario
        self._livro = livro

    @classmethod
    def criar_emprestimo(cls, usuario: Usuario, livro: Livro):
        if not livro.disponivel:
            raise ValueError(f"O livro '{livro.titulo}' não está disponível para empréstimo.")
        livro.disponivel = False
        return cls(usuario, livro)

    def devolver_livro(self):
        self._livro.disponivel = True

    def __str__(self):
        return f"Empréstimo de '{self._livro.titulo}' para {self.usuario.nome}"
