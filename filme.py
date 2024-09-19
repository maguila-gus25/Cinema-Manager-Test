class Filme:

    filmes_db = []  # Simula um banco de dados de filmes

    def __init__(self, titulo: str, duracao: str, genero: str, classificacao_etaria: int, sinopse: str):
        self.__titulo = titulo
        self.__duracao = duracao
        self.__genero = genero
        self.__classificacao_etaria = classificacao_etaria
        self.__sinopse = sinopse

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: str):
        self.__duracao = duracao

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero

    @property
    def classificacao_etaria(self):
        return self.__classificacao_etaria

    @classificacao_etaria.setter
    def classificacao_etaria(self, classificacao_etaria: int):
        self.__classificacao_etaria = classificacao_etaria

    @property
    def sinopse(self):
        return self.__sinopse

    @sinopse.setter
    def sinopse(self, sinopse: str):
        self.__sinopse = sinopse

    def adicionarFilme(self):
        # Adiciona o filme ao "banco de dados"
        Filme.filmes_db.append(self)
        return f"Filme '{self.__titulo}' adicionado com sucesso."

    def atualizarFilme(self, titulo=None, duracao=None, genero=None, classificacao_etaria=None, sinopse=None):
        # Atualiza os atributos do filme se os novos valores forem fornecidos
        if titulo is not None:
            self.__titulo = titulo
        if duracao is not None:
            self.__duracao = duracao
        if genero is not None:
            self.__genero = genero
        if classificacao_etaria is not None:
            self.__classificacao_etaria = classificacao_etaria
        if sinopse is not None:
            self.__sinopse = sinopse
        return f"Filme atualizado: {self.__titulo}, {self.__duracao}, {self.__genero}, {self.__classificacao_etaria}, {self.__sinopse}"

    def removerFilme(self):
        # Remove o filme do "banco de dados"
        if self in Filme.filmes_db:
            Filme.filmes_db.remove(self)
            return f"Filme '{self.__titulo}' removido com sucesso."
        else:
            return f"Filme '{self.__titulo}' não encontrado."

    def __str__(self):
        return (f"Título: {self.__titulo}\n"
                f"Duração: {self.__duracao}\n"
                f"Gênero: {self.__genero}\n"
                f"Classificação Etária: {self.__classificacao_etaria}\n"
                f"Sinopse: {self.__sinopse}")