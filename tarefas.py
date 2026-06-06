import json
from models.tarefa import Tarefa
from datetime import datetime

def salvar_tarefa(tarefa):

    nova_tarefa = tarefa.to_dict()

    tarefas = carregar_tarefas()

    tarefas.append(nova_tarefa)

    salvar_tarefas(tarefas)

def mostrar_tarefas():

    tarefas = carregar_tarefas()
    
    if not tarefas:

        print("\nNenhuma tarefa encontrada")
        return
    
    print ("\n=== TAREFAS ===")

    for dados in tarefas:

        tarefa = Tarefa.from_dict(
            dados
        )

        tarefa.exibir()

def carregar_tarefas():

    try:

        with open(
            "tarefas.json",
            "r",
            encoding="utf-8"
        ) as arquivo:
            
            return json.load(arquivo)
        
    except FileNotFoundError:

        return []
    
    except json.JSONDecodeError:

        print(
            "\n❌ Histórico de tarefas corrompido."
        )

        return []
    
def concluir_tarefa():

    tarefas = carregar_tarefas()

    if not tarefas:

        print(
            "\nNenhuma tarefa encontrada."
        )

        return
    
    print("\n=== TAREFAS ===")

    for indice, dados in enumerate(
        tarefas,
        start=1
    ):

        print(
            f"{indice} - "
            f"{dados['titulo']}"
        )
    
    numero = int(
        input(
            "\nDigite o número da tarefa: "
        )
    )

    indice = numero - 1

    dados = tarefas[indice]

    tarefa = Tarefa.from_dict(
        dados
    )

    tarefa.concluir()

    tarefas[indice] = tarefa.to_dict()

    salvar_tarefas(tarefas)

    print(
        "\n✅ Tarefa concluída com sucesso."
    )

def salvar_tarefas(tarefas):
    
    with open(
        "tarefas.json",
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            tarefas,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

def excluir_tarefa():

    tarefas = carregar_tarefas()

    if not tarefas:

        print(
            "\nNenhuma tarefa encontrada."
        )

        return
    
    print("\n=== TAREFAS ===")

    for indice, dados in enumerate(
        tarefas,
        start=1
    ):

        print(
            f"{indice} - "
            f"{dados['titulo']}"
        )
    
    numero = int(
        input(
            "\nDigite o número da tarefa: "
        )
    )

    indice = numero - 1

    removida = tarefas.pop(indice)

    salvar_tarefas(tarefas)

    print(
        f"\n🗑️ Tarefa "
        f"'{removida['titulo']}' "
        f"removida com sucesso."
    )

def mostrar_estatísticas():

    tarefas = carregar_tarefas()

    if not tarefas:

        print("\nNenhuma tarefa encontrada")
        return
    
    total = len(tarefas)

    concluidas, pendentes = 0, 0

    tarefas_concluidas = []

    for tarefa in tarefas:

        if tarefa["concluida"]:

            concluidas += 1
            tarefas_concluidas.append(tarefa)

        else:

            pendentes += 1

    taxa_conclusao = (concluidas / total) * 100

    primeira_criada = tarefas[0]

    ultima_concluida = max(
        tarefas_concluidas,
        key=lambda tarefa: datetime.strptime(
            tarefa["data_conclusao"],
            "%d/%m/%Y %H:%M:%S"
        )
    )

    print("\n=== ESTATÍSTICAS ===")

    print(f"\n📊 Total de tarefas: {total}")

    print(f"\n✅ Concluídas: {concluidas}")

    print(f"\n⌛ Pendentes: {pendentes}")

    print(f"\n📈 Taxa de conclusão: {taxa_conclusao:.1f}%")

    print(f"\n🕒 Primeira tarefa criada: \n{primeira_criada["titulo"]}\n{primeira_criada["data_criacao"]}")

    print(f"\n🏁 Última tarefa concluída: \n{ultima_concluida["titulo"]}\n{ultima_concluida["data_conclusao"]}")