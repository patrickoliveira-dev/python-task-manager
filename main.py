from models.tarefa import Tarefa

from tarefas import (
    salvar_tarefa,
    mostrar_tarefas,
    concluir_tarefa,
    excluir_tarefa,
    editar_tarefa,
    filtrar_tarefas,
    buscar_tarefa,
    mostrar_estatísticas
)

while True:

    print("\n=== TASK MANAGER ===")
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Estatísticas")
    print("6 - Editar tarefa")
    print("7 - Filtrar tarefas")
    print("8 - Buscar tarefa")
    print("9 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        titulo = input("\nDigite um título para a tarefa: ")
        descricao = input("\nDigite a descrição da tarefa: ")
        
        print("\n=== PRIORIDADE ===")

        print("\n1 - Baixa")
        print("2 - Média")
        print("3 - Alta")

        prioridade_opcao = input("\nDefina a prioridade para a tarefa: ")

        if prioridade_opcao == "1":
            prioridade = "Baixa"

        elif prioridade_opcao == "2":
            prioridade = "Média"

        elif prioridade_opcao == "3":
            prioridade = "Alta"
        
        else:

            print(
                "\n❌ Prioridade inválida."
            )

            continue

        tarefa = Tarefa(
            titulo,
            descricao,
            prioridade
        )

        salvar_tarefa(tarefa)

        print(
            "\n✅ Tarefa adicionada com sucesso."
        )
    
    elif opcao == "2":

        mostrar_tarefas()
    
    elif opcao == "3":

        concluir_tarefa()

    elif opcao == "4":

        excluir_tarefa()

    elif opcao == "5":

        mostrar_estatísticas()

    elif opcao == "6":

        editar_tarefa()

    elif opcao == "7":

        filtrar_tarefas()

    elif opcao == "8":

        buscar_tarefa()

    elif opcao == "9":

        print(
            "\nEncerrando programa..."
        )

        break

    else:

        print(
            "\nOpção inválida."
        )