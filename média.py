import os
from colorama import init, Fore, Style

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

arquivo_atual = None

def menu_principal():
    while True:
        limpar_tela()
        print(Fore.CYAN + "\n=== MENU PRINCIPAL ===")
        print(Fore.GREEN + "1 - Criar um arquivo de turma")
        print(Fore.GREEN + "2 - Excluir um arquivo de turma")
        print(Fore.GREEN + "3 - Visualizar um arquivo existente")
        print(Fore.GREEN + "4 - Parar o código")
        opcao = input(Fore.YELLOW + "Escolha uma opção: ")
        limpar_tela()

        if opcao == '1':
            criar_arquivo()
        elif opcao == '2':
            excluir_arquivo()
        elif opcao == '3':
            visualizar_arquivo()
            input(Fore.BLUE + "\nPressione Enter para voltar ao menu...")
        elif opcao == '4':
            print(Fore.RED + "Encerrando...")
            break
        else:
            print(Fore.RED + "Opção inválida.")
            input("\nPressione Enter para continuar...")

def criar_arquivo():
    global arquivo_atual
    limpar_tela()
    nome_arquivo = input(Fore.YELLOW + "Digite o nome do novo arquivo da turma: ") + ".txt"
    arquivo_atual = nome_arquivo
    with open(arquivo_atual, 'w') as f:
        pass
    print(Fore.GREEN + f"Arquivo '{arquivo_atual}' criado com sucesso.")
    input("Pressione Enter para continuar...")
    menu_criacao()

def menu_criacao():
    global arquivo_atual
    while True:
        limpar_tela()
        print(Fore.MAGENTA + f"\n=== MENU DO ARQUIVO: {arquivo_atual} ===")
        print("1 - Adicionar nome e notas de aluno")
        print("2 - Visualizar o arquivo")
        print("3 - Sair para o menu principal")
        opcao = input(Fore.YELLOW + "Escolha uma opção: ")
        limpar_tela()

        if opcao == '1':
            adicionar_aluno()

        elif opcao == '2':
            visualizar_arquivo(arquivo_atual)
            input(Fore.BLUE + "\nPressione Enter para voltar ao menu...")

        elif opcao == '3':
            print(Fore.RED + "Voltando ao menu principal...")
            input("Pressione Enter para continuar...")
            break
        else:
            print(Fore.RED + "Opção inválida.")
            input("\nPressione Enter para continuar...")

def adicionar_aluno():
    global arquivo_atual
    while True:
        limpar_tela()
        print(Fore.MAGENTA + "=== Adicionar Aluno ===")
        nome_aluno = input("Nome do aluno: ")
        try:
            qtd = int(input("Quantas notas deseja inserir? "))
            notas = []
            for i in range(1, qtd + 1):
                entrada = input(f"Nota {i}: ").replace(',', '.')
                nota = float(entrada)
                notas.append(nota)
            media = sum(notas) / len(notas)
            with open(arquivo_atual, 'a') as f:
                f.write(f"Nome:\n{nome_aluno}\n")
                for i, nota in enumerate(notas, 1):
                    f.write(f"Nota {i}:\n{nota}\n")
                f.write(f"Média:\n{round(media, 2)}\n")
                f.write("---------------\n")
            print(Fore.GREEN + "\nAluno, notas e média adicionados.")
        except ValueError:
            print(Fore.RED + "Erro: digite apenas números válidos.")
            input("Pressione Enter para continuar...")
            continue

        opcao = input(Fore.YELLOW + "\nDeseja adicionar outro aluno? (s para sim, qualquer outra tecla para voltar): ")
        if opcao.lower() != 's':
            break

def excluir_arquivo():
    limpar_tela()
    nome = input(Fore.YELLOW + "Digite o nome do arquivo a ser excluído (sem .txt): ")
    caminho = nome + ".txt"
    if os.path.exists(caminho):
        os.remove(caminho)
        print(Fore.RED + f"Arquivo '{caminho}' excluído.")
    else:
        print(Fore.RED + "Arquivo não encontrado.")
    input(Fore.BLUE + "\nPressione Enter para voltar ao menu...")

def visualizar_arquivo(nome_arquivo=None):
    if not nome_arquivo:
        nome = input(Fore.YELLOW + "Digite o nome do arquivo que deseja visualizar: ")
        nome_arquivo = nome + ".txt"
    try:
        with open(nome_arquivo, 'r') as f:
            conteudo = f.read()
            print(Fore.CYAN + "\n=== CONTEÚDO DO ARQUIVO ===")
            print(conteudo)
    except FileNotFoundError:
        print(Fore.RED + "Arquivo não encontrado.")

if __name__ == "__main__":
    menu_principal()
