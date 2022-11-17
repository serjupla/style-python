from typing import Dict, List, Union

class EstatisticaResumida:
    def __init__(self,dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> Dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {}
        estatistica[f'{self.agencia}-{self.dia}'] = len(clientes_atendidos)
        return estatistica