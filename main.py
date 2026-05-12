from Veiculos import Carro, Moto

entrada = None
cadastrados = {}

while entrada != 0:
    print('--------------MENU--------------')
    print('Digite 0 para sair')
    print('Digite 1 para cadastrar um carro')
    print('Digite 2 para cadastrar uma moto')
    print('Digite 3 para listar os veículos')
    print('Digite 4 para calcular o imposto')

    if entrada == 1:
        placa          = input("digite a placa")
        marca          = input("digite a placa")
        modelo         = input("digite o modelo")
        ano            = input("digite o ano")
        valor_mercado  = input("digite o valor de mercado")
        numero_portas  = input("digite o número de portas")
        tipo_carroceria= input("digite o tipo de carroceria")
        cadastrados[placa] = Carro(placa, marca, modelo, ano, valor_mercado, numero_portas, tipo_carroceria)