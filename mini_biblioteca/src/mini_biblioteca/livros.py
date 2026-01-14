class Livro:
    def __init__(self, titulo: str, autor: str, codigo: str, disponivel: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.titulo} por {self.autor} (Código: {self.codigo}) - {status}"
