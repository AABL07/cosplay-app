import sqlite3
from models.participante import Participante

DB_PATH = "cosplay.db"

class ParticipanteRepository:

    def criar_tabela(self):
        conn = sqlite3.connect(DB_PATH)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS participantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                fidelidade_j1 REAL, fidelidade_j2 REAL, fidelidade_j3 REAL,
                complexidade_j1 REAL, complexidade_j2 REAL, complexidade_j3 REAL,
                acabamento_j1 REAL, acabamento_j2 REAL, acabamento_j3 REAL,
                total_fidelidade REAL, total_complexidade REAL,
                total_acabamento REAL, media_geral REAL
            )
        """)
        conn.commit()
        conn.close()

    def inserir(self, p: Participante) -> tuple:
        try:
            conn = sqlite3.connect(DB_PATH)
            conn.execute("""
                INSERT INTO participantes (
                    nome,
                    fidelidade_j1, fidelidade_j2, fidelidade_j3,
                    complexidade_j1, complexidade_j2, complexidade_j3,
                    acabamento_j1, acabamento_j2, acabamento_j3,
                    total_fidelidade, total_complexidade, total_acabamento, media_geral
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (p.nome, *p.notas, p.total_fidelidade, p.total_complexidade, p.total_acabamento, p.media_geral))
            conn.commit()
            return True, "Participante cadastrado com sucesso!"
        except sqlite3.IntegrityError:
            return False, "Participante já cadastrado."
        finally:
            conn.close()

    def excluir(self, nome: str) -> tuple:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.execute("DELETE FROM participantes WHERE nome = ?", (nome,))
        conn.commit()
        conn.close()
        return (True, "Participante excluído.") if cursor.rowcount > 0 else (False, "Participante não encontrado.")

    def excluir_todos(self) -> tuple:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("DELETE FROM participantes")
        conn.commit()
        conn.close()
        return True, "Todos os registros foram apagados."

    def listar_ranking(self) -> list:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.execute(
            "SELECT nome, media_geral FROM participantes ORDER BY media_geral DESC"
        )
        resultado = cursor.fetchall()
        conn.close()
        return resultado
