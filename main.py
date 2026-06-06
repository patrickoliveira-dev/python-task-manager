from models.tarefa import Tarefa

from tarefas import (
    salvar_tarefa,
    mostrar_tarefas,
    concluir_tarefa,
    excluir_tarefa
)

while True:

    print("\n=== TASK MANAGER ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        titulo = input("\nDigite um título para a tarefa: ")
        descricao = input("\nDigite a descrição da tarefa: ")

        tarefa = Tarefa(
            titulo,
            descricao
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

        print("\nEncerrando programa...")
        break

    else:

        print("\nOpção inválida.")