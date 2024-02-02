class paciente:
    cod_pac: str
    nome: str
    endereco: str
    fone: str
class medico:
    cod_med: str
    nome: str
    endereco: str
    fone: str
class consulta:
    num_consulta: int
    dia: str
    hora: str
    cod_med: str
    nome_med: str
    cod_pac: str
    nome_pac: str

def titulo(mensagem: str) -> None:
  tamanho = len(mensagem)
  print('*' * (tamanho + 4))
  print('* ' + mensagem + ' *')
  print('*' * (tamanho + 4))

def listar_dias_da_semana():
    for item in range(len(dias_da_semana)):
        print(f'{item + 1}. {dias_da_semana[item]}')
def cadastrar_paciente():
    if len(Paciente) == 5:
        titulo('Não é possível cadastrar novos pacientes. Limite atingido!')
    else:
        pacientes = paciente()
        pacientes.cod_pac = str(len(Paciente) + 1)
        pacientes.nome = input('Informe o nome do paciente: ')
        pacientes.endereco = input('Informe o endereço: ')
        pacientes.fone = input('Informe o telefone: ')
        Paciente.append(pacientes)
        print('Paciente cadastrado com sucesso!')
def cadastrar_medico():
    if len(Medico) == 3:
        titulo('Não é possível cadastrar novos médicos. Limite atingido!')
    else:
        medicos = medico()
        medicos.cod_med = str(len(Medico) + 1)
        medicos.nome = input('Informe o nome do médico: ')
        medicos.endereco = input('Informe o endereço: ')
        medicos.fone = input('Informe o telefone: ')
        Medico.append(medicos)
        print('Médico cadastrado com sucesso!')
def cadastrar_consulta():
    global consultas_no_dia
    if len(Paciente) == 0:
        print("Nenhum paciente cadastrado! Redirecionando para cadastro de pacientes...")
        cadastrar_paciente()
    if len(Medico) == 0:
        print("Nenhum médico cadastrado! Redirecionando para cadastro de médicos...")
        cadastrar_medico()
    print('Cadastro de consultas...')
    if len(Consulta) == 0:
        while True:
            for i in range(len(Medico)):
                print(f'{Medico[i].cod_med}. Dr. {Medico[i].nome}')
            X = input("Selecione o médico desejado ou digite '0' para sair: ")
            if X == '0':
                return None
            else:
                escolha = False
                for i in range(len(Medico)):
                    if str(i + 1) == X:
                        escolha = True
                if escolha == True:
                    consultas = consulta()
                    consultas.cod_med = Medico[int(X) - 1].cod_med
                    consultas.num_consulta = len(Consulta) + 1
                    while True:
                        listar_dias_da_semana()
                        X = input("Selecione o dia desejado ou digite '0' para sair: ")
                        if X == '0':
                            return None
                        elif X == '1' or X == '2' or X == '3' or X == '4' or X == '5':
                            consultas.dia = dias_da_semana[int(X) - 1]
                            consultas.hora = input("Informe a hora desejada: ")
                            while True:
                                for c in range(len(Paciente)):
                                    print(f'Código: {Paciente[c].cod_pac},Nome: {Paciente[c].nome}')
                                X = input('Informe o código do paciente: ')
                                escolha = False
                                for c in range(len(Paciente)):
                                    if str(c + 1) == X:
                                        escolha = True
                                if escolha == True:
                                    consultas.cod_pac = Paciente[int(X) - 1].cod_pac
                                    Consulta.append(consultas)
                                    print('Agendamento realizado com sucesso!')
                                    return None
                                else:
                                    print('Por favor, selecione uma opção válida.')
                        else:
                            print('Por favor, selecione uma opção válida.')
                else:
                    print('Por favor, selecione uma opção válida.')
    else:
        medicos_disponiveis = []
        for item in range(len(Medico)):
            class indisponiveis:
                nome_do_medico = None
                dias_disponiveis = []
            disponiveis = indisponiveis()
            for dias in range(len(dias_da_semana)):
                consultas_no_dia = 0
                for i in range(len(Consulta)):
                    if Medico[item].cod_med == Consulta[i].cod_med and Consulta[i].dia == dias_da_semana[dias]:
                        consultas_no_dia += 1
                if consultas_no_dia < 2:
                    disponiveis.nome_do_medico = Medico[item].nome
                    disponiveis.dias_disponiveis.append(dias_da_semana[dias])
            if disponiveis.nome_do_medico != None:
                medicos_disponiveis.append(disponiveis)
        if len(medicos_disponiveis) == 0:
            print('Infelizmente não temos médicos disponíveis nos próximos 5 dias úteis.')
        else:
            while True:
                for item in range(len(medicos_disponiveis)):  
                    print(f'{item + 1}. {medicos_disponiveis[item].nome_do_medico}')
                X = input("Selecione o médico desejado ou digite '0' para sair: ")
                if X == '0':
                    return None
                else:
                    for item in range(len(medicos_disponiveis)):
                        if str(item + 1) == X:  
                            consultas = consulta()
                            for i in range(len(Medico)):  
                                if Medico[i].nome == medicos_disponiveis[int(X) - 1].nome_do_medico:  
                                    consultas.nome_med = Medico[i].nome  
                                    consultas.cod_med = Medico[i].cod_med  
                            consultas.num_consulta = len(Consulta) + 1  
                            for j in range(len(medicos_disponiveis[int(X) - 1].dias_disponiveis)):
                                print(f'{j + 1}. {medicos_disponiveis[int(X) - 1].dias_disponiveis[j]}')
                            while True:
                                Y = input("Selecione um dos dias disponíveis ou digite '0' para sair: ")  
                                if Y == '0':
                                    return None
                                for j in range(len(medicos_disponiveis[int(X) - 1].dias_disponiveis)):
                                    if str(j + 1) == Y:
                                        for dias in range(len(dias_da_semana)):
                                            if medicos_disponiveis[int(X) - 1].dias_disponiveis[int(Y) - 1] == dias_da_semana[dias]:
                                                consultas.dia = dias_da_semana[dias]
                                                consultas.hora = input("Informe a hora no formato 'HH:MM': ")
                                                while True:
                                                    for c in range(len(Paciente)):
                                                        print(f'Código: P{Paciente[c].cod_pac},Nome: {Paciente[c].nome}')
                                                    X = input("Informe o código do paciente ou digite '0' para sair: ")
                                                    if X == '0':
                                                        return None
                                                    for c in range(len(Paciente)):
                                                        if str(c + 1) == X:
                                                            consultas.cod_pac = Paciente[int(X) - 1].cod_pac
                                                            Consulta.append(consultas)
                                                            print('Agendamento realizado com sucesso!')
                                                            return None
                                                        else:
                                                            print('Por favor, selecione uma opção válida.')
                                    else:
                                        print('Por favor, selecione uma opção válida.')
                        else:
                            print('Por favor, selecione uma opção válida.')
    
def mostrar_consultas():
    if len(Consulta) == 0:
        titulo('Não há consultadas agendadas! Redirecionando para agendamento de consultas...')
        cadastrar_consulta()
    else:
        print('Consultas da semana:')
        for dia in range(len(dias_da_semana)):
            atual = dias_da_semana[dia]
            x = True
            for item in range(len(Consulta)):
                if atual == Consulta[item].dia:
                    if x == True:
                        print(f'\n{Consulta[item].dia}:')
                        x = False
                    print(f'Código da consulta: C{Consulta[item].num_consulta},Hora: {Consulta[item].hora}')
                    for c in range(len(Medico)):
                        if Consulta[item].cod_med == Medico[c].cod_med:
                            print(f'Médico: {Medico[c].nome}')
                    for c in range(len(Paciente)):
                        if Consulta[item].cod_pac == Paciente[c].cod_pac:
                            print(f'Paciente: {Paciente[c].nome}')
# Programa principal:
Paciente, Medico, Consulta = [], [], []
dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
def menu():
    print('''
     Menu principal:
1. Cadastrar um paciente
2. Cadastrar um médico
3. Agendar uma consulta
4. Listar as consultas agendadas
0. Sair do programa''')
while True:
    menu()
    resposta = input('Selecione uma das seguintes opções para continuar: ')
    if resposta == '0':
        print('Finalizado')

        break
    elif resposta == '1':
        cadastrar_paciente()
    elif resposta == '2':
        cadastrar_medico()
    elif resposta == '3':
        cadastrar_consulta()
    elif resposta == '4':
        mostrar_consultas()
    else:
        print('Por favor, selecione uma opção válida!')
