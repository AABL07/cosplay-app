from dataclasses import dataclass

@dataclass
class Participante:
    nome: str
    notas: list

    @property
    def total_fidelidade(self):
        return sum(self.notas[0:3])

    @property
    def total_complexidade(self):
        return sum(self.notas[3:6])

    @property
    def total_acabamento(self):
        return sum(self.notas[6:9])

    @property
    def media_geral(self):
        return round(
            (self.total_fidelidade + self.total_complexidade + self.total_acabamento) / 3,
            2
        )
