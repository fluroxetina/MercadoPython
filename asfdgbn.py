# Dicionário de usuários com informações de email e senha
usuarios = {
    "Eduardin": ["email@gmail.com", "12313"],
    "Rafa": ["lcoco@gmail.com", "56798"]
}

# Função de Cadastro de Usuário
def Cadastro():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios:
        while usuarios[usuario][0] == email:
            print("E-mail já cadastrado. Digite outro email.")
            email = input("Digite seu e-mail: ")

    usuarios[nome] = [email, senha]
    print("Cadastro efetuado com sucesso!")

# Função de Login de Usuário
def LoKin():
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios:
        if usuarios[usuario][0] == email and usuarios[usuario][1] == senha:
            print("Login realizado com sucesso!")
            return

    print("Usuário não cadastrado ou senha incorreta.")
    Cadastro()

# Catálogo de Produtos
produtos = [
    {"nome": "Produto 1", "preco": 10.0, "descricao": "Descrição do Produto 1"},
    {"nome": "Produto 2", "preco": 20.0, "descricao": "Descrição do Produto 2"}
]

# Função para exibir catálogo de produtos
def exibir_catalogo():
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Descrição: {produto['descricao']}")

# Carrinho de compras
carrinho = []

# Função para adicionar produtos ao carrinho
def adicionar_ao_carrinho(produto_nome):
    for produto in produtos:
        if produto["nome"] == produto_nome:
            carrinho.append(produto)
            print(f"{produto_nome} adicionado ao carrinho.")
            return
    print(f"Produto {produto_nome} não encontrado no catálogo.")

# Função para remover produtos do carrinho
def remover_do_carrinho(produto_nome):
    for produto in carrinho:
        if produto["nome"] == produto_nome:
            carrinho.remove(produto)
            print(f"{produto_nome} removido do carrinho.")
            return
    print(f"Produto {produto_nome} não está no carrinho.")

# Função para visualizar o carrinho
def visualizar_carrinho():
    if not carrinho:
        print("O carrinho está vazio.")
        return

    total = 0
    for produto in carrinho:
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}")
        total += produto["preco"]
    print(f"Total: {total}")

# Função para finalizar a compra
historico_compras = []

def finalizar_compra():
    if not carrinho:
        print("O carrinho está vazio.")
        return

    # Aqui você pode adicionar lógica para inserir informações de pagamento
    print("Compra finalizada com sucesso!")
    historico_compras.append(carrinho.copy())
    carrinho.clear()

# Função para exibir histórico de compras
def exibir_historico_compras():
    for i, compra in enumerate(historico_compras):
        print(f"Compra {i+1}:")
        for produto in compra:
            print(f"  Nome: {produto['nome']}, Preço: {produto['preco']}")

# Função para atualizar o estoque de produtos
def atualizar_estoque(nome_produto, quantidade):
    for produto in produtos:
        if produto["nome"] == nome_produto:
            produto["quantidade"] = quantidade
            print(f"Estoque de {nome_produto} atualizado para {quantidade} unidades.")
            return
    print(f"Produto {nome_produto} não encontrado no catálogo.")

# Função para adicionar novo produto ao estoque
def adicionar_produto_estoque(nome, preco, descricao):
    novo_produto = {"nome": nome, "preco": preco, "descricao": descricao, "quantidade": 0}
    produtos.append(novo_produto)
    print(f"Produto {nome} adicionado ao estoque.")

# Exemplo de Uso
while True:
    print("\nOpções:")
    print("1 - Cadastro de Usuário")
    print("2 - Login de Usuário")
    print("3 - Exibir Catálogo de Produtos")
    print("4 - Adicionar Produto ao Carrinho")
    print("5 - Remover Produto do Carrinho")
    print("6 - Visualizar Carrinho")
    print("7 - Finalizar Compra")
    print("8 - Exibir Histórico de Compras")
    print("9 - Atualizar Estoque de Produto")
    print("10 - Adicionar Novo Produto ao Estoque")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        break
    elif opcao == 1:
        Cadastro()
    elif opcao == 2:
        LoKin()
    elif opcao == 3:
        exibir_catalogo()
    elif opcao == 4:
        produto_nome = input("Digite o nome do produto a ser adicionado ao carrinho: ")
        adicionar_ao_carrinho(produto_nome)
    elif opcao == 5:
        produto_nome = input("Digite o nome do produto a ser removido do carrinho: ")
        remover_do_carrinho(produto_nome)
    elif opcao == 6:
        visualizar_carrinho()
    elif opcao == 7:
        finalizar_compra()
    elif opcao == 8:
        exibir_historico_compras()
    elif opcao == 9:
        nome_produto = input("Digite o nome do produto a ser atualizado no estoque: ")
        quantidade = int(input("Digite a nova quantidade do produto: "))
        atualizar_estoque(nome_produto, quantidade)
    elif opcao == 10:
        nome = input("Digite o nome do novo produto: ")
        preco = float(input("Digite o preço do novo produto: "))
        descricao = input("Digite a descrição do novo produto: ")
        adicionar_produto_estoque(nome, preco, descricao)
    else:
        print("Opção inválida. Tente novamente.")


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


usuarios = {
    "Eduardin": ["email@gmail.com", "12313", "administrador"],
    "Rafa": ["lcoco@gmail.com", "56798", "usuario"]
}

produtos = [
    {"nome": "Banana", "preco": 5.00, "descricao": "Banana nanica madura"}
]

def Cadastro():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    funcao = input("Digite sua função (usuario/administrador): ").lower()

    for i in usuarios:  
        while usuarios[i][0] == email:
            print("E-mail já cadastrado. Digite outro email")
            email = input("Digite seu e-mail: ")

    usuarios[nome] = [email, senha, funcao]
    print("Cadastro efetuado")

def LoKin():
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    for i in usuarios:
        if usuarios[i][0] == email and usuarios[i][1] == senha:
            print("Login efetuado")
            return usuarios[i][2]  # Retorna a função do usuário

    print("Usuário não cadastrado ou senha incorreta. Realize o cadastro para poder entrar.")
    Cadastro()
    return None

def ExibirCatalogo():
    for i in produtos:
        print(f"Nome: {i['nome']}, Preço: {i['preco']}, Descrição: {i['descricao']}")

carrinho = []

def AddCarrinho(nome_produtos):
    ExibirCatalogo()
    for j in produtos:
        if j["nome"] == nome_produtos:
            carrinho.append(j)
            print(f"{nome_produtos} foi adicionado ao carrinho")
            return
    print("Produto não encontrado")

def ExcCarrinho(nome_produtos):
    for i in carrinho:
        if i["nome"] == nome_produtos:
            carrinho.remove(i)
            print(f"{nome_produtos} foi removido do carrinho")
            return
    print("Produto não encontrado")

def VizualizarCarrinho():
    if not carrinho:
        print("O carrinho está vazio.")
        return

    total = 0
    for produto in carrinho:
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}")
        total += produto["preco"]
    print(f"Total: {total}")

HistoricoCompras = []

def FinalizarPagamento():
    VizualizarCarrinho()
    info = input("Digite a senha do cartão: ")
    print("Compra finalizada")
    HistoricoCompras.append(carrinho.copy())
    carrinho.clear()

def AddPrd():
    aux = {}
    aux["nome"] = input("Digite o nome do novo produto: ")
    aux["preco"] = float(input("Digite o preço do novo produto: "))
    aux["descricao"] = input("Digite a descrição do novo produto: ")
    produtos.append(aux)
    print("Produto adicionado com sucesso!")

def AtualizarEstoque():
    BuscarPrd = input("Qual o item que procura: ")

    for i in produtos:
        if BuscarPrd == i["nome"]:
            Acao = input("O que deseja fazer (add/remove): ").lower()

            if Acao == "add":
                qtd = int(input("Qual nova quantidade do produto: "))
                if qtd == 0:
                    produtos.remove(i)
                print("Estoque atualizado com sucesso!")

            elif Acao == "remove":
                produtos.remove(i)
                print("Produto removido com sucesso!")
            return
    print("Produto não encontrado")

def menu_usuario():
    while True:
        opcao = int(input("O que deseja fazer:\n1 - Exibir o catálogo\n2 - Adicionar produto ao carrinho\n3 - Remover produto do carrinho\n4 - Visualizar o carrinho e o total a pagar\n5 - Finalizar a compra\n0 - Sair\n"))
        if opcao == 1:
            ExibirCatalogo()
        elif opcao == 2:
            nome_produto = input("Digite o nome do produto que deseja adicionar: ")
            AddCarrinho(nome_produto)
        elif opcao == 3:
            nome_produto = input("Digite o nome do produto que deseja remover: ")
            ExcCarrinho(nome_produto)
        elif opcao == 4:
            VizualizarCarrinho()
        elif opcao == 5:
            FinalizarPagamento()
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")

def menu_administrador():
    while True:
        opcao = int(input("O que deseja fazer:\n1 - Exibir o catálogo\n2 - Adicionar produto ao carrinho\n3 - Remover produto do carrinho\n4 - Visualizar o carrinho e o total a pagar\n5 - Finalizar a compra\n6 - Adicionar novo produto\n7 - Atualizar estoque\n0 - Sair\n"))
        if opcao == 1:
            ExibirCatalogo()
        elif opcao == 2:
            nome_produto = input("Digite o nome do produto que deseja adicionar: ")
            AddCarrinho(nome_produto)
        elif opcao == 3:
            nome_produto = input("Digite o nome do produto que deseja remover: ")
            ExcCarrinho(nome_produto)
        elif opcao == 4:
            VizualizarCarrinho()
        elif opcao == 5:
            FinalizarPagamento()
        elif opcao == 6:
            AddPrd()
        elif opcao == 7:
            AtualizarEstoque()
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")

cad = input("Já possui cadastro (sim/nao): ").lower()

if cad == "nao":
    Cadastro()

role = None
if cad == "sim":
    role = LoKin()

if role == "usuario":
    menu_usuario()
elif role == "administrador":
    menu_administrador()
else:
    print("Erro ao identificar função do usuário.")
