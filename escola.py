'''Requisitos do Sistema:

•Cadastrar Turmas:
•O sistema deve permitir que novas turmas sejam adicionadas.
•Cada turma deve ter um nome exclusivo.

•Cadastrar Alunos:
•O sistema deve permitir que alunos sejam adicionados a uma turma específica.
•Ao cadastrar um aluno, devem ser informados seu nome e suas notas.
•As notas devem ser inseridas como uma lista de valores numéricos.

•Atualizar Informações de Alunos:
•O sistema deve permitir a atualização das informações de um aluno existente.
•Deve ser possível alterar o nome do aluno e/ou suas notas.

•Remover Alunos:
•O sistema deve permitir que um aluno seja removido de uma turma específica.

•Visualizar Informações:
•O sistema deve permitir a visualização de todas as turmas cadastradas.
•Para cada turma, deve ser possível visualizar a lista de alunos e suas respectivas 
notas.

Estrutura de Dados:

•Cada turma deve conter as seguintes informações:
•Nome da Turma: Identificador exclusivo da turma.
•Lista   de  Alunos:   Cada   aluno   deve   ter   um   nome   e   uma   lista   de   notas 
associadas.

Implementação:
O   sistema   será   implementado   utilizando   dicionários   em   Python   e   incluirá   um   menu 
interativo para que o usuário (professor) possa escolher a operação desejada. Além disso, 
para o usuário acessar o sistema, ele deve possuir um cadastro de login. Esse cadastro é feito 
pelo adm e deve ter tratamento para erros na hora de efetuar o login, somente user e senhas 
cadastrados devem possuir a permissão, caso contrário, uma mensagem de erro deve ser 
apresentada'''


login_cadastrados = {
    "usuario1":123, "usuario2":1414, "usuario3":111   
}

turmas = {
       "Turma A":{
           "Derek":[10,10,10],"Pororoka":[10,10,10]              
    }
          
}


while True:

    cadastrado = input("Possui cadastro? sim/nao ")

    if cadastrado == "sim":
        login = False
        while not login:
            nome = input("Digite o seu nome: ")
            senha = input("Digite sua senha: ")

            if nome in login_cadastrados and login_cadastrados[nome] == senha:
                print("Login efetuado")
                login = True
            else:
                print("Nome ou senha encorretas")
        
        if login:
            break

        elif cadastrado == "não":
            
            novo_usuario = input("Digite o novo nome de usuário: ")
            nova_senha = input("Digite a nova senha: ")
            login_cadastrados[novo_usuario] = nova_senha
            print("Cadastro realizado com sucesso")


while True:

    acao = int(input("\n1- Para adicionar nova turma \n2- Adicionar um novo aluno \n3- Atualizar dados de aluno \n4- Remover aluno \n5- Para visualizar as uma turma \n0- Sair\n"))

    if acao == 1:
        novaturma = input("Digite o nome da nova turma: ")

        if novaturma in turmas:
            print("Esse nome já existe!")
        
        else:
            turmas[novaturma] = {}
            print("Turma adicionada!")

    elif acao == 2:
        print(turmas.keys(), "\nturmas existentes")
        novoaluno = input("\nDigite nome do novo aluno:")
        turma_aluno = input("\nDigite em qual turma o aluno ficara: ")

        if turma_aluno not in turmas:
            print("Essa turma não existe")

        else:
            aux = []
            for nota in range(3):

                notas = float(input("Digite as notas do aluno: "))
                aux.append(notas)

            turmas[turma_aluno][novoaluno] = aux

    elif acao == 3:

        atualizar_aluno = input("Qual aluno deseja atualizar: ")
        print(turmas , "\nTurmas existentes")
        procurar_aluno = input("Qual turma o aluno esta? ")

        if atualizar_aluno in turmas[procurar_aluno]:
            funcao = int(input("Deseja \n1 - Atualizar o nome do aluno \n2 - Atulizar as notas do aluno\n"))

            if funcao == 1:
               novo_nome = input("Digite o novo nome do aluno: ")

               turmas[procurar_aluno][novo_nome]                

            elif funcao == 2:
                aux = []
                for nota in range(3):
                    nova_nota = float(input("Digite as notas do aluno: "))
                    aux.append(nova_nota)

                turmas[procurar_aluno][atualizar_aluno] = aux

    elif acao == 4:

        procurar_turma = input("Digite qual turma é o aluno que deseja remover: ")
        remover_aluno = input("Digite qual o nome do aluno que deseja remover: ")
        del turmas[procurar_turma][remover_aluno]  


    elif acao == 5:

        turma_escolhida = input("Digite qual turma deseja visualizar: ")

        for nome, nota in turmas[turma_escolhida].items():
            print(f"nome: {nome} // notas: {nota}")





