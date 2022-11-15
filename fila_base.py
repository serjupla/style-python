import abc
from abc import ABC, abstractmethod


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    @abstractmethod
    def gera_senha_atual(self) -> None:
        ...

    @abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()