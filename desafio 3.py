caixa = 100.0
estoque = {}

while True:
    print("\n===== MENU =====")
    print("1 - Compra")
    print("2 - Venda")
    print("3 - Estoque")
    print("4 - Financeiro")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # COMPRA
    if opcao == "1":
        nome_produto = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade comprada: "))

        total = preco * quantidade

        if caixa >= total:
            caixa -= total

            if nome_produto in estoque:
                estoque[nome_produto]["quantidade"] += quantidade
            else:
                estoque[nome_produto] = {
                    "preco": preco,
                    "quantidade": quantidade
                }

            print("Compra realizada com sucesso!")
        else:
            print("Dinheiro insuficiente no caixa!")

    # VENDA
    elif opcao == "2":
        nome_produto = input("Nome do produto: ")

        if nome_produto in estoque:
            quantidade = int(input("Quantidade vendida: "))

            if estoque[nome_produto]["quantidade"] >= quantidade:
                preco = estoque[nome_produto]["preco"]
                total = preco * quantidade

                lucro = total * 0.05
                valor_final = total + lucro

                caixa += valor_final
                estoque[nome_produto]["quantidade"] -= quantidade

                print(f"Venda realizada! Lucro de 5% aplicado.")
            else:
                print("Quantidade insuficiente em estoque!")
        else:
            print("Produto não encontrado!")

    # ESTOQUE
    elif opcao == "3":
        print("\n=== ESTOQUE ===")
        if estoque:
            for produto, dados in estoque.items():
                print(f"{produto} - Quantidade: {dados['quantidade']} - Preço: R${dados['preco']}")
        else:
            print("Estoque vazio!")

    # FINANCEIRO
    elif opcao == "4":
        print(f"\nValor em caixa: R${caixa:.2f}")

    # SAIR
    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")