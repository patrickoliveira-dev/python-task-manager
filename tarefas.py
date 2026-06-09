import json
from models.tarefa import Tarefa
from datetime import datetime

def salvar_tarefa(tarefa):

    nova_tarefa = tarefa.to_dict()

    tarefas = carregar_tarefas()

    tarefas.append(nova_tarefa)

    salvar_tarefas(tarefas)

def mostrar_tarefas():

    tarefas = obter_tarefas()

    if tarefas is None:
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
            
            tarefas = json.load(arquivo)

            for tarefa in tarefas:

                if "prioridade" not in tarefa:

                    tarefa["prioridade"] = "Média"
                
            return tarefas
        
    except FileNotFoundError:

        return []
    
    except json.JSONDecodeError:

        print(
            "\n❌ Histórico de tarefas corrompido."
        )

        return []
    
def concluir_tarefa():

    tarefas = obter_tarefas()

    if tarefas is None:
        return

    indice = escolher_tarefa(tarefas)

    if indice is None:
        return

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

    tarefas = obter_tarefas()

    if tarefas is None:
        return
    
    indice = escolher_tarefa(tarefas)

    if indice is None:
        return

    removida = tarefas.pop(indice)

    salvar_tarefas(tarefas)

    print(
        f"\n🗑️ Tarefa "
        f"'{removida['titulo']}' "
        f"removida com sucesso."
    )

def mostrar_estatísticas():

    tarefas = obter_tarefas()

    if tarefas is None:
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
    
    if tarefas_concluidas:

        ultima_concluida = max(
            tarefas_concluidas,
            key=lambda tarefa: datetime.strptime(
                tarefa["data_conclusao"],
                "%d/%m/%Y %H:%M:%S"
            )
        )

    else:

        ultima_concluida = None

    taxa_conclusao = (concluidas / total) * 100

    primeira_criada = tarefas[0]

    print("\n=== ESTATÍSTICAS ===")

    print(f"\n📊 Total de tarefas: {total}")

    print(f"\n✅ Concluídas: {concluidas}")

    print(f"\n⌛ Pendentes: {pendentes}")

    print(f"\n📈 Taxa de conclusão: {taxa_conclusao:.1f}%")

    print(f"\n🕒 Primeira tarefa criada: \n{primeira_criada["titulo"]}\n{primeira_criada["data_criacao"]}")

    if ultima_concluida:

        print(
            f"\n🏁 Última tarefa concluída:"
            f"\n{ultima_concluida['titulo']}"
            f"\n{ultima_concluida['data_conclusao']}"
        )

    else:

        print(
            "\n🏁 Nenhuma tarefa concluída ainda."
        )
    
def editar_tarefa():

    tarefas = obter_tarefas()

    if tarefas is None:
        return
    
    indice = escolher_tarefa(tarefas)

    if indice is None:
        return

    tarefa = tarefas[indice]

    print(
        f"\nTítulo atual: "
        f"{tarefa['titulo']}"
    )

    novo_titulo = input(
        "\nNovo título: "
    )

    if novo_titulo:

        tarefa["titulo"] = novo_titulo

    print(
        f"\nDescrição atual: "
        f"{tarefa['descricao']}"
    )

    nova_descricao = input(
        "\nNova descrição: "
    )

    if nova_descricao:

        tarefa["descricao"] = nova_descricao
    
    print(
        f"\nPrioridade atual: "
        f"{tarefa['prioridade']}"
    )

    while True:

        nova_prioridade = input(
            "\nNova prioridade: "
            "\n1 - Baixa"
            "\n2 - Média"
            "\n3 - Alta"
            "\n\nEscolha: "
        )

        if nova_prioridade == "1":
            tarefa["prioridade"] = "Baixa"
            break

        elif nova_prioridade == "2":
            tarefa["prioridade"] = "Média"
            break

        elif nova_prioridade == "3":
            tarefa["prioridade"] = "Alta"
            break

        print(
            "\n❌ Prioridade inválida."
        )

    salvar_tarefas(tarefas)

    print(
        "\n✅ Tarefa editada com sucesso."
    )

def filtrar_tarefas():

    tarefas = obter_tarefas()

    if tarefas is None:
        return
    
    print("\n=== FILTROS ===")

    print("\n1 - Todas")
    print("2 - Pendentes")
    print("3 - Concluídas")
    print("4 - Prioridade Alta")
    print("5 - Prioridade Média")
    print("6 - Prioridade Baixa")

    opcao = input(
        "\nEscolha uma opção: "
    )

    if opcao == "1":

        tarefas_filtradas = tarefas

    elif opcao == "2":

        tarefas_filtradas = [
            tarefa
            for tarefa in tarefas
            if not tarefa["concluida"]
        ]
    
    elif opcao == "3":

        tarefas_filtradas = [
            tarefa
            for tarefa in tarefas
            if tarefa["concluida"]
        ]
    
    elif opcao == "4":

        tarefas_filtradas = [
            tarefa
            for tarefa in tarefas
            if tarefa["prioridade"] == "Alta"
        ]

    elif opcao == "5":

        tarefas_filtradas = [
            tarefa
            for tarefa in tarefas
            if tarefa["prioridade"] == "Média"
        ]

    elif opcao == "6":

        tarefas_filtradas = [
            tarefa
            for tarefa in tarefas
            if tarefa["prioridade"] == "Baixa"
        ]

    else:

        print(
            "\nOpção inválida."
        )

        return
    
    if not tarefas_filtradas:

        print(
            "\nNenhuma tarefa encontrada."
        )

        return
    
    for dados in tarefas_filtradas:

        tarefa = Tarefa.from_dict(
            dados
        )

        tarefa.exibir()

def buscar_tarefa():

    tarefas = obter_tarefas()

    if tarefas is None:
        return

    texto = input(
        "\nDigite um termo: "
    ).lower()

    tarefas_encontradas = [
        tarefa
        for tarefa in tarefas
        if texto in tarefa["titulo"].lower()
        or texto in tarefa["descricao"].lower()
    ]
    
    if not tarefas_encontradas:

        print(
            "\nNenhuma tarefa encontrada."
        )

        return
    
    for dados in tarefas_encontradas:

        tarefa = Tarefa.from_dict(
            dados
        )

        tarefa.exibir()

def obter_tarefas():

    tarefas = carregar_tarefas()

    if not tarefas:

        print(
            "\nNenhuma tarefa encontrada."
        )

        return None
    
    return tarefas

def listar_titulos(tarefas):

    print("\n=== TAREFAS ===")

    for indice, tarefa in enumerate(
        tarefas,
        start=1
    ):
        
        print(
            f"{indice} - "
            f"{tarefa['titulo']}"
        )

def escolher_tarefa(tarefas):

    listar_titulos(tarefas)

    numero = int(
        input(
            "\nDigite o número da tarefa: "
        )
    )

    if numero < 1 or numero > len(tarefas):

        print(
            "\n❌ Número inválido."
        )

        return None
    
    return numero - 1