from datetime import datetime

class Tarefa:

    def __init__(
        self,
        titulo,
        descricao,
        prioridade="Média",
        concluida=False,
        data_criacao=None,
        data_conclusao=None,
    ):

        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

        self.data_criacao = (
            data_criacao
            or datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

        self.data_conclusao = (
            data_conclusao
        )

        self.prioridade = prioridade
    
    def exibir(self):

        print(f"\n📌 Título: {self.titulo}")
        print(f"📝 Descrição: {self.descricao}")
        status = (
            "Sim"
            if self.concluida
            else "Não"
        )
        print(f"✅ Concluída: {status}")
        print(f"🕒 Criada em: {self.data_criacao}")
        if self.data_conclusao:

            print(
                f"🏁 Concluída em: "
                f"{self.data_conclusao}"
            )
        if self.prioridade == "Alta":
            emoji = "🔴"

        elif self.prioridade == "Média":
            emoji = "🟡"

        else:
            emoji = "🟢"
        print(
            f"{emoji} Prioridade: "
            f"{self.prioridade}"
        )
    
    def to_dict(self):

        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "concluida": self.concluida,
            "data_criacao": self.data_criacao,
            "data_conclusao": self.data_conclusao
        }
    
    @classmethod
    def from_dict(cls, dados):

        tarefa = cls(
            dados["titulo"],
            dados["descricao"],
            dados.get(
                "prioridade",
                "Média"
            ),
            dados["concluida"],
            dados["data_criacao"],
            dados["data_conclusao"],
        )

        return tarefa
    
    def concluir(self):

        if self.concluida:
            return

        self.concluida = True
    
        self.data_conclusao = (
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )