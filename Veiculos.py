class Veiculo:
    def __init__(self, placa, marca, modelo, ano, valor_mercado):

        if not (1885 < ano <= 2026):  # o delorean não funcionaria aqui...
            raise ValueError("Ano inválido")

        if not (10000 < valor_mercado <= 200000):
            raise ValueError("Valor mercado invalido")

        self.__placa = str(placa)
        self.__marca = str(marca)
        self.__modelo = str(modelo)
        self.__ano = int(ano)
        self.__valor_mercado = float(valor_mercado)

    @property
    def placa(self):
        return self.__placa

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def valor_mercado(self):
        return self.__valor_mercado

    def calcular_imposto(self):  # na função base, retorna 0
        return 0

    def __str__(self):
        return f"Placa: {self.__placa} | Marca: {self.__marca} | Modelo: {self.__modelo} | Ano: {self.__ano} | Valor de Mercado: {self.__valor_mercado}"


class Carro(Veiculo):
    def __init__(
        self, placa, marca, modelo, ano, valor_mercado, numero_portas, tipo_carroceria
    ):
        if numero_portas not in [2, 4]:
            raise ValueError("Numero de portas inválido")
        super().__init__(placa, marca, modelo, ano, valor_mercado)
        self.__numero_portas = int(numero_portas)
        self.__tipo_carroceria = str(tipo_carroceria)

    def calcular_imposto(self):
        return self.valor_mercado * 0.1

    def __str__(self):
        return f"{super().__str__()} | Portas: {self.__numero_portas} | Carroceria: {self.__tipo_carroceria}"


class Moto(Veiculo):
    def __init__(self, placa, marca, modelo, ano, valor_mercado, cilindrada, tipo_moto):
        super().__init__(placa, marca, modelo, ano, valor_mercado)
        if cilindrada < 0:
            raise ValueError("Cilindrada inválida")
        self.__cilindrada = cilindrada
        self.__tipo_moto = tipo_moto

    def calcular_imposto(self):
        return self.valor_mercado * 0.5

    def __str__(self):
        return f"{super().__str__()} | Cilindrada: {self.__cilindrada} | Tipo de Moto: {self.__tipo_moto}"
