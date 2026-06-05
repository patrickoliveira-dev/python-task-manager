import json
from models.tarefa import Tarefa

def salvar_tarefa(tarefa):

    nova_tarefa = tarefa.to_dict()

    tarefas = carregar_tarefas()

    tarefas.append(nova_tarefa)

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

    print(
        "\n✅ Tarefa concluída com sucesso."
    )