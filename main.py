def pegar_bytes(x):
    # Transforma a chave em bytes
    cha = bytes(x, 'utf-8')
    return cha

def geradorconlinear(num_aleatorios, x_0, modulo, multiplicador, incremento):
    num_aleatorios[0] = x_0
    for i in range(1, len(num_aleatorios)):
        num_aleatorios[i] = (num_aleatorios[i - 1] *
                             multiplicador + incremento) % modulo

# Define as constantes do gerador
quan = 5000
num_aleatorios = [0] * quan
x_0 = 4
modulo = 256
multiplicador = 133
incremento = 23

geradorconlinear(num_aleatorios, x_0, modulo, multiplicador, incremento)

def criptografar(msg, chave):
    # Garante que a chave tenha o mesmo comprimento da mensagem ou mais
    while len(chave) < len(msg):
        chave += chave
    
    chave = pegar_bytes(chave)
    msg_byte = pegar_bytes(msg)
    
    chave_bytes = [byte for byte in chave]
    keystream_bits = [byte for byte in num_aleatorios]
    
    mensagem_cifrada = bytes(bit_msg ^ bit_chave ^ bit_keystream for (bit_msg, bit_chave, bit_keystream) in zip(msg_byte, chave_bytes, keystream_bits))
    
    return mensagem_cifrada


def descriptografar(mensagem_cifrada, chave):
    while len(chave) < len(mensagem_cifrada):
        chave += chave
    
    chave = pegar_bytes(chave)
    
    chave_bytes = [byte for byte in chave]
    keystream_bits = [byte for byte in num_aleatorios]
    
    dados_descriptografados = bytes(bit_dado ^ bit_chave ^ bit_keystream for (bit_dado, bit_chave, bit_keystream) in zip(mensagem_cifrada, chave_bytes, keystream_bits))
    
    return dados_descriptografados.decode('utf-8')

mensagem_original = input("Qual a mensagem? ")
chave = input("Qual a chave? ")

mensagem_cifrada = criptografar(mensagem_original, chave)
print("Mensagem criptografada:", mensagem_cifrada)

dados_descriptografados = descriptografar(mensagem_cifrada, chave)
print("Mensagem descriptografada:", dados_descriptografados)
