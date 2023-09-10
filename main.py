def pegar_bytes(x):
    # Transforma a chave em bytes
    cha = bytes(x, 'utf-8')
    return cha


def geradorconlinear(num_aleatorios, x_0, modulo, multiplicador, incremento):

    num_aleatorios[0] = x_0

    for i in range(1, len(num_aleatorios)):
        num_aleatorios[i] = (num_aleatorios[i - 1] *
                             multiplicador + incremento) % modulo


def soma_bytes(byte1, byte2):
    return byte1+byte2

msg = input("Entre com a mensagem: ")

while True:

    chave = input("Entre com a chave de até 128 caracteres: ")
    
    # Verifica o comprimento da chave
    if len(chave) <= 128:
        break  # A chave tem o comprimento desejado, sai do loop
    else:
        print("A chave excede o limite de 128 caracteres. Tente de novo")

while len(chave) < len(msg):
    chave += chave

# -- Variáveis para o gerador congruente linear (GCL) --

# Quantidade de caracteres
quan = 5000

# Quantidade de números pseudo-aleatórios
num_aleatorios = [0] * quan

# Valor inicial
x_0 = 4

# Módulo (choose a large prime number)
modulo = 256

# Multiplicador (choose a prime number)
multiplicador = 133

# Incremento (choose a prime number)
incremento = 23

# -- Fim variaveis GCL --

geradorconlinear(num_aleatorios, x_0, modulo, multiplicador, incremento)

chave = pegar_bytes(chave)

# Cria um set sem repetições
msg_byte = pegar_bytes(msg)

chave_bytes = []

for byte in chave:
    chave_bytes.append(byte)

keystream_bits = []

for byte in num_aleatorios:
    keystream_bits.append(byte)

print(chave_bytes)
print(keystream_bits)

mensagem_cifrada = bytes(bit_msg ^ bit_chave ^ bit_keystream for (bit_msg, bit_chave, bit_keystream) in zip(msg_byte, chave_bytes, keystream_bits))
dados_descriptografados = bytes(bit_dado ^ bit_chave ^ bit_keystream for (bit_dado, bit_chave, bit_keystream) in zip(mensagem_cifrada, chave_bytes, keystream_bits))

# A variável 'mensagem_original' agora deve conter a mensagem original
print("Mensagem criptografada:", mensagem_cifrada)
print("Mensagem descriptografada:", dados_descriptografados.decode('utf-8'))