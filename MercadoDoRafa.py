usuarios = [
    {"nome": "rafa", "email": "blabla", "senha": "123123", "funcao": "administrador"},
    {"nome": "derek", "email": "lcoco", "senha": "15555", "funcao": "usuario"}
]

produtos = [
    {"nome": "Banana", "preco": 5.00, "descricao": "Banana nanica madura"}
]
carrinho = []
def Cadastro():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    funcao = input("Digite sua função (administrador/usuario): ")

    for usuario in usuarios:
        if usuario["email"] == email:
            print("E-mail já cadastrado. Digite outro e-mail.")
            return

    novo_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "funcao": funcao
    }
    usuarios.append(novo_usuario)
    print("Cadastro efetuado com sucesso.")

def LoKin():
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")


    for  i in usuarios:
        if i["email"] == email and i["senha"] == senha:
            print(f"Bem-vindo, {i['nome']}!")
            return i["funcao"]
        
    print("Usuário não cadastrado ou senha incorreta. Realize o cadastro para poder entrar.")
 

def ExibirCatalogo():
    for i in produtos:
        print(f"Nome: {i['nome']}, Preço: {i['preco']}, Descrição: {i['descricao']}")

        

def AddCarinho(nome_produtos):
    for j in produtos:
        if j["nome"] == nome_produtos:
            carrinho.append(j)
            print(f"{nome_produtos} foi adicionado ao carrinho")
        
        else:
            print("Produto não encontrado")


def ExcCarrinho(nome_produtos):
    for i in carrinho:
        if i["nome"] == nome_produtos:
            carrinho.remove(i)

        else:
            print("Produto não encontrado")

def VizualizarCarrinho():

    for i in carrinho:
        print(f"{i['nome']} {i['preco']}")

    total()


def total():
    valor = 0
    for i in carrinho:
        valor += i["preco"]
        print(f"total é de: {valor}")
    
HistoricoCompras = []
def FinalizarPagamento():
    global carrinho
    total()
    Info = int(input("Digite a senha do cartão "))

    print("compra finalizada")
    
    HistoricoCompras.append(carrinho)
    carrinho = []

def AddPrd():

    aux = {}
    aux["nome"] = input("Digite o nome do novo produto ")
    aux["preco"] = input("Digite o preço do novo produto ")
    aux["descricao"] = input("Digite a descrição do novo produto ")
    produtos.append(aux)


def AtualizarEstoque():

    BuscarPrd = input("Qual o item que procura: ")

    for i in produtos:
        if  BuscarPrd == i["nome"]:
            Acao = input("O que deseja fazer add/remove: ").lower()

            if Acao == "add": 
                qtd = int(input("Qual nova qtd do produto"))
                
                if qtd == 0:
                    produtos.remove(i)


            elif Acao == "remove":
                produtos.remove(i)


def MenuUsuario():
    while True:
        opcao = int(input("O que deseja fazer: \n1 - Para exibir o catalogo \n2 - Para adicionar algum produto ao carrinho \n3 - Para remover um produto do carrinho \n4 - Para vizualizar o carrinho e o total a pagar \n5 - Para finalizar a compra \n0 - Para sair \n"))    

        if opcao == 1:
            ExibirCatalogo()

        elif opcao == 2:
            ExibirCatalogo()
            nome_prd = input("Digite qual produto deseja adicionar o carrinho ")
            AddCarinho(nome_prd)
        
        elif opcao == 3:
            ExibirCatalogo()
            nome_prd = input("Digite qual produto deseja remover do carrinho ")
            ExcCarrinho(nome_prd)

        elif opcao == 4:
            VizualizarCarrinho()

        elif opcao == 5:
            FinalizarPagamento()

        elif opcao == 0:
            break

def MenuAdministrador():
    while True:
        opcao = int(input("Digite o que deseja fazer \n1 - Para adicionar novos produtos ao estoque \n2 - Para atualizar a quantidade de produtos no estoque \n0 - Para sair "))

        if opcao == 1:
            AddPrd()

        elif opcao == 2:
            AtualizarEstoque()
        
        elif opcao == 0:
            break


cad = input("Já possui cadastro (sim/nao): ").lower()

if cad == "nao":
    Cadastro()
    funcao = LoKin()
elif cad == "sim":
    funcao = LoKin()

if funcao == "usuario":
    MenuUsuario()

elif funcao == "administrador":
    MenuAdministrador()
