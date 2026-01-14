from livros import Livro
from usuarios import Usuario
from emprestimos import Emprestimo

def main():

    livro1 = Livro("1984", "George Orwell", "001")
    livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "002", disponivel=False)

    usuario1 = Usuario("Alice", "U001")
    usuario2 = Usuario("Bob", "U002")

    emprestimo1 = Emprestimo(usuario1, livro1)
    emprestimo2 = Emprestimo(usuario2, livro2)

    print(emprestimo1)
    print(emprestimo2)

    emprestimo1.devolver_livro()
    print(f"Após devolução: {livro1}")
    
if __name__ == "__main__":
    main()
