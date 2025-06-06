import os
from rich.console import Console
from rich.table import Table

console = Console()

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    MENU_TABUADA = '''
    \r\r[bold green][1][/bold green]: -> Tabuada de 1
    \r\r[bold green][2][/bold green]: -> Tabuada de 2
    \r\r[bold green][3][/bold green]: -> Tabuada de 3
    \r\r[bold green][4][/bold green]: -> Tabuada de 4
    \r\r[bold green][5][/bold green]: -> Tabuada de 5
    \r\r[bold green][6][/bold green]: -> Tabuada de 6
    \r\r[bold green][7][/bold green]: -> Tabuada de 7
    \r\r[bold green][8][/bold green]: -> Tabuada de 8
    \r\r[bold green][9][/bold green]: -> Tabuada de 9
    \r\r[bold green][10][/bold green]: -> Tabuada de 10
    \r\r[bold green][0][/bold green]: -> Sair
    '''
    console.print(MENU_TABUADA)

def get_option():
    """Obtém uma opção válida do usuário."""
    options = [str(i) for i in range(11)]
    while True:
        option = console.input('Informe a opção desejada: ').strip()
        if option in options:
            return option
        else:
            console.print('[bold red]Opção inválida, tente novamente![/bold red]')

def get_operation():
    """Exibe o menu de operações e retorna a operação escolhida."""
    menu_operacao = (
        '\n[bold cyan][1][/bold cyan]: -> Soma (+)\n'
        '[bold cyan][2][/bold cyan]: -> Subtração (-)\n'
        '[bold cyan][3][/bold cyan]: -> Multiplicação (x)\n'
        '[bold cyan][4][/bold cyan]: -> Divisão (/)\n'
    )
    opcoes = {'1': '+', '2': '-', '3': 'x', '4': '/'}
    while True:
        console.print(menu_operacao)
        op = console.input('Escolha a operação desejada: ').strip()
        if op in opcoes:
            return opcoes[op]
        else:
            console.print('[bold red]Opção inválida, tente novamente![/bold red]')

def display_tabuada(number, operacao):
    """Exibe a tabuada do número com a operação escolhida."""
    op_simbolo = {'+': 'Soma', '-': 'Subtração', 'x': 'Multiplicação', '/': 'Divisão'}
    table = Table(
        title=f"Tabuada de {number} - {op_simbolo[operacao]}",
        show_header=True,
        header_style="bold magenta"
    )
    table.add_column("Operação", style="dim")
    table.add_column("Resultado", style="bold green")

    if operacao != '/':
        for i in range(1, 11):
            if operacao == '+':
                result = number + i
                oper = f"{number} + {i}"
                resultado_str = str(result)
            elif operacao == '-':
                minuendo = number + i
                result = minuendo - number
                oper = f"{minuendo} - {number}"
                resultado_str = str(result)
            elif operacao == 'x':
                result = number * i
                oper = f"{number} x {i}"
                resultado_str = str(result)
            table.add_row(oper, resultado_str)
    else:
        # Divisão: dividendo calculado para que o quociente varie de 1 a 10
        for quociente in range(1, 11):
            dividendo = number * quociente
            oper = f"{dividendo} / {number}"
            resultado_str = str(quociente)
            table.add_row(oper, resultado_str)

    console.print(table)

def main():
    clear_screen()
    while True:
        display_menu()
        option = get_option()

        if option == '0':
            console.print('[bold red]Saindo do programa...[/bold red]')
            break
        else:
            number = int(option)
            clear_screen()
            operacao = get_operation()
            clear_screen()
            display_tabuada(number, operacao)
            console.input('\n[bold yellow]Pressione Enter para voltar ao menu...[/bold yellow]')
            clear_screen()

if __name__ == "__main__":
    main()
