# ------------- // --------------
"""
Exercício:
Importar ficheiro 'input.csv' - contém registos de vários clientes com datas de inscrição e aprovação.
Objetivo: Verificar as datas se são válidas (VERIFICAR - DATA) e dividir em 2 ficheiros:
                output.csv ( para as datas, se válidas = True, senão = False ) & resultado.log ( imprimir as mensagens de erro para as datas False ) 
"""
# ------------- // --------------

camposoutput = ["ID", "NOME", "D.INSCRIÇÃO", "D.APROVAÇÃO", "VALIDA.INSCRIÇÃO", "VALIDA.APROVAÇÃO"]
camposlog = ["ID", "MENSAGEM-INSCRIÇÃO", "MENSAGEM-APROVAÇÃO"]

def ler(ficheiro):
    with open(ficheiro, 'r', encoding="utf-8") as file:
        rows = file.readlines()
        tabela = []
        for row in rows[1:]:
            id, nome, data_inscricao, data_aprovacao = row.replace("\n", '').replace('"', '').split(",")  #Para cada campo da linha vai separar por variáveis e remover "\n" e '""' por ","
            tabela.append([id, nome, data_inscricao, data_aprovacao])
        return tabela

def gravar(ficheiro, tabela):
    with open(ficheiro, "w", encoding="utf-8") as file:
        linha = ""
        for i in range(len(camposoutput)):
            if i == len(camposoutput) - 1:
                linha += str(camposoutput[i])
            else:
                linha += str(camposoutput[i]) + ","
        file.write(linha + "\n")

        for linha in tabela:
            id, nome, data_inscricao, data_aprovacao, inscricao_valida, aprovacao_valida = linha
            file.write(
                f'"{id}","{nome}","{data_inscricao}","{data_aprovacao}","{inscricao_valida}","{aprovacao_valida}"\n')
    return

def gravarlog(ficheiro, tabela):
    with open(ficheiro, "w", encoding="utf-8") as file:
        linha = ""
        for i in range(len(camposlog)):                        # Caso seja preciso
            if i == len(camposlog) - 1:                        # Mostrar o cabeçalho dos erros
                linha += str(camposlog[i])                     # (id, mensagem-inscrição, mensagem-aprovação) descomentar
            else:
                linha += str(camposlog[i]) + ","
        file.write(linha + "\n")
        for linha in tabela:
            id, erro_inscricao, erro_aprovacao = linha
            file.write(
                f'"{id}","{erro_inscricao}","{erro_aprovacao}"\n')
    return

def validar(tabela):
    clientes = []
    for cliente in tabela:
        id, nome, data_inscricao, data_aprovacao = cliente
        data_inscricao_valida, erro_inscricao = validar_data(data_inscricao)
        data_aprovacao_valida, erro_aprovacao = validar_data(data_aprovacao)

        clientes.append([id, nome, data_inscricao, data_aprovacao, data_inscricao_valida, data_aprovacao_valida])

    return clientes

def validarlog(tabela):
    clientes = []
    for cliente in tabela:
        id, nome, data_inscricao, data_aprovacao = cliente
        data_inscricao_valida, erro_inscricao = validar_data(data_inscricao)
        data_aprovacao_valida, erro_aprovacao = validar_data(data_aprovacao)

        clientes.append([id, erro_inscricao, erro_aprovacao])

    return clientes

# ------------- // --------------
""" 
VERIFICAR - DATA
"""
# ------------- // --------------

def separar_data(data):
    datelist = data.split('-')

    dia = int(datelist[0])
    mes = int(datelist[1])
    ano = int(datelist[2])

    return dia, mes, ano


def ultimo_dia_do_mes(mes, ano):
    ultimo = 0
    if mes == 2:
        if (ano % 4) == 0:
            ultimo = 29
        else:
            ultimo = 28
    elif mes in (1, 3, 5, 7, 8, 10, 12):
        ultimo = 31
    else:
        ultimo = 30
    # ...
    # ...
    return ultimo


def formato_correto(data):
    correto = False

    datelist = []
    for letra in data:
        datelist.append(letra)

    if datelist[2] and datelist[5] == '-':
        return True

    return correto


def validar_data(data):
    valida = False
    if formato_correto(data):
        dia, mes, ano = separar_data(data)
        msg1 = f'O ano {ano} deverá ser entre 1900 e 2022.'
        msg2 = f'O mês {mes} deverá ser entre 1 e 12.'
        msg3 = f'O dia {dia} deverá ser entre 1 e {ultimo_dia_do_mes(mes, ano)}'
        if 1900 <= ano <= 2022:
            if 1 <= mes <= 12:
                if 1 <= dia <= ultimo_dia_do_mes(mes, ano):
                    return True, ''
                else:
                    return False, msg3
            else:
                return False, msg2
        else:
            return False, msg1
    else:
        print(f'{data} não está no formato DD-MM-YYYY')
    return valida


if __name__ == '__main__':
    tabela = ler('input.csv')

    validartabela = validar(tabela)
    gravar("output.csv", validartabela)

    erros = validarlog(tabela)
    gravarlog("resultado.log", erros)

    print("------------")
    print("Verificar os ficheiros...")
    print("------------")
