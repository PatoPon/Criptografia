def pegar_bytes(x):
    # Transforma a chave em bytes
    cha = bytes(x, 'utf-8')
    return cha

def geradorconlinear(num_aleatorios, x_0, modulo, multiplicador, incremento):
    
    num_aleatorios[0] = x_0

    for i in range(1, len(num_aleatorios)):
        num_aleatorios[i] = (num_aleatorios[i - 1] * multiplicador + incremento) % modulo

def soma_bytes (byte1, byte2):
    return byte1+byte2

msg = input("Entre com a mensagem: ")

# Pede uma chave para o usuário
chave = input("Entre com a chave: ")

# -- Variáveis para o gerador congruente linear (GCL) --

# Quantidade de caracteres
quan = len(msg)

# Quantidade de números pseudo-aleatórios
num_aleatorios = [0] * quan

# Valor inicial
x_0 = 433

# Módulo (choose a large prime number)
modulo = 997

# Multiplicador (choose a prime number)
multiplicador = 839

# Incremento (choose a prime number)
incremento = 463

# -- Fim variaveis GCL --

geradorconlinear(num_aleatorios, x_0, modulo, multiplicador, incremento)

chave = pegar_bytes(chave)
print(chave)

# Cria um set sem repetições
char_unicos = set(msg)

mapeamento_bytes = []

# Mapeia os caracteres em um dicionarios para os números aleatorios -- zip é o mapeador
print(mapeamento_bytes)
mapeamento = dict(zip(char_unicos, mapeamento_bytes))
print(mapeamento)

chave_bits = []

for byte in chave:
    chave_bits.append(bin(byte))

print(chave_bits)

keystream_bits = []

for byte in num_aleatorios:
    keystream_bits.append(bin(byte))

mapeamento_bytes = [sum(i) for i in zip(chave, num_aleatorios)]