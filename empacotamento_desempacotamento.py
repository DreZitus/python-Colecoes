#empacotamento com tuplas

nome_produto = "carne"
preco = 22.9
qtde_comprada = 1

carne = (nome_produto, preco, qtde_comprada)

#desempacotamento com tuplas

compras_efetuadas = ""

for nome, preco, qtde in compras_efetuadas:
    print(f"nome: {nome}\tPreço: {preco}\tQtde: {qtde}")