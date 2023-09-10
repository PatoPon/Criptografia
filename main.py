# Criptografia em Python
# Feito por Guilherme Novaes Campos

# A técnica usada é uma cifra de fluxo simplificada
# A ideia original era usar a AES mas ela é muito complexa e ficaria mais dificil tanto de
# escrever como explicar

# A cifra de fluxo se baseia em usar chaves bits originais combinados com uma corrente de 
# bits de cifragem (chamados de fluxo de chave) vindos de um gerador de dígitos pseudo-aleatório (GCL nesse 
# caso). Normalmente esta combinação é feita através de uma operação de disjunção exclusiva ou XOR.

# Foi usado o XOR por utilizar algo que eu me familiarizei nas aulas da Priscila sobre circuitos.

# Código -->

# Únicas bibliotecas que eu resolvi usar. Somente pra mostrar uma interface e o tempo que passou
import tkinter as tk
import time as ti

# Função pra criar um botão "Copiar"
copiar_button_chave = None

def criar_botao_copiar(texto, rotulo):
    copiar_button = tk.Button(
        root, text=rotulo, command=lambda t=texto: copiar_texto(t))
    copiar_button.pack()
    return copiar_button

# Função para criptografar

def criptografar():

    com_tempo = ti.time()

    mensagem = mensagem_entry.get()
    chave = chave_entry.get()

    while len(chave) < len(mensagem):
        chave += chave

    mensagem_cifrada = bytes(
        bit_msg ^ bit_chave ^ bit_keystream for (bit_msg, bit_chave, bit_keystream) in zip(mensagem.encode('utf-8'), chave.encode('utf-8'), keystream_bits)
    )

    tempo_final = ti.time()  # Registra o tempo final
    tempo_total = tempo_final - com_tempo  # Calcula o tempo decorrido
    resultado_criptografia.config(
        text=f"Mensagem criptografada: {mensagem_cifrada.hex()} (Tempo: {(tempo_total*1000):.4f} segundos)")

    global copiar_button_criptografia, copiar_button_chave
    if copiar_button_criptografia:
        copiar_button_criptografia.destroy()
    if copiar_button_chave:
        copiar_button_chave.destroy()
    copiar_button_criptografia = criar_botao_copiar(
        mensagem_cifrada.hex(), "Copiar Mensagem Criptografada")
    copiar_button_chave = None  # Retira da área de transferência

# Função para descriptografar

def descriptografar():

    com_tempo = ti.time()

    mensagem_cifrada = mensagem_cifrada_entry.get()
    chave = chave_descriptografia_entry.get()

    while len(chave) < len(mensagem_cifrada):
        chave += chave

    mensagem_original = bytes(
        bit_dado ^ bit_chave ^ bit_keystream for (bit_dado, bit_chave, bit_keystream) in zip(bytes.fromhex(mensagem_cifrada), chave.encode('utf-8'), keystream_bits)
    ).decode('utf-8')

    tempo_final = ti.time()  # Registra o tempo final
    tempo_total = tempo_final - com_tempo  # Calcula o tempo decorrido
    resultado_descriptografia.config(
        text=f"Mensagem descriptografada: {mensagem_original} (Tempo: {(tempo_total*1000):.4f} segundos)")

    global copiar_button_descriptografia
    if copiar_button_descriptografia:
        copiar_button_descriptografia.destroy()
    copiar_button_descriptografia = criar_botao_copiar(
        mensagem_original, "Copiar Mensagem Descriptografada")

# Função para copiar texto para a área de transferência


def copiar_texto(texto):
    root.clipboard_clear()  # Limpa a área de transferência
    root.clipboard_append(texto)  # Adiciona o texto a área de transferência
    root.update()  # Atualiza a área de transferência


# Inicialização do Tkinter (Pra mostrar a interface)
root = tk.Tk()
root.title("Criptografia e Descriptografia (Cifra de fluxo)")

# Define a largura e a altura da janela (A default é muito pequena)
largura = 500 
altura = 400
root.geometry(f"{largura}x{altura}")

# Criação dos elementos da interface

# Meu nome!!!!
seu_nome_label = tk.Label(root, text="Guilherme Novaes Campos - Trabalho do Primeiro Periodo", fg="gray")
seu_nome_label.pack(side="bottom", padx=10, pady=10)

# Rótulo e campo de entrada pra mensagem ser criptografada
mensagem_label = tk.Label(root, text="Mensagem:")
mensagem_entry = tk.Entry(root)

# Rótulo e campo de entrada pra chave
chave_label = tk.Label(root, text="Chave:")
chave_entry = tk.Entry(root)

# Botão pra iniciar a criptografia
criptografar_button = tk.Button(
    root, text="Criptografar", command=criptografar)

# Rótulo e campo de entrada pra a mensagem cifrada (e descriptografar depois)
mensagem_cifrada_label = tk.Label(root, text="Mensagem Cifrada:")
mensagem_cifrada_entry = tk.Entry(root)

# Rótulo e campo de entrada pra a chave de descriptografia (que o professor vai dar)
chave_descriptografia_label = tk.Label(root, text="Chave:")
chave_descriptografia_entry = tk.Entry(root)

# Botão pra iniciar a descriptografia
descriptografar_button = tk.Button(
    root, text="Descriptografar", command=descriptografar)

# Rótulo pra exibir o resultado da criptografia
resultado_criptografia = tk.Label(root, text="")

# Rótulo pra exibir o resultado da descriptografia
resultado_descriptografia = tk.Label(root, text="")

# Variáveis pra os botões "Copiar"
copiar_button_criptografia = None
copiar_button_descriptografia = None

# Posicionamento dos elementos na janela
mensagem_label.pack()
mensagem_entry.pack()

chave_label.pack()
chave_entry.pack()

# Não sei por que eu preciso ficar dando "pack" em tudo. Fica feio

criptografar_button.pack()

mensagem_cifrada_label.pack()
mensagem_cifrada_entry.pack()

chave_descriptografia_label.pack()
chave_descriptografia_entry.pack()

descriptografar_button.pack()

resultado_criptografia.pack()
resultado_descriptografia.pack()

# Variáveis pro gerador congruente linear (Essa parte que eu mais demorei pra entender)
# Basicamente é uma equação que o programa vai usar pra criar números pseudo-aleatorios

quan = 5000
num_aleatorios = [0] * quan
x_0 = 4
modulo = 256
multiplicador = 133
incremento = 23

# Inicialização do gerador congruente linear -- Equação: X{n+1} = (a * X{n} + c) mod m}
num_aleatorios[0] = x_0
for i in range(1, len(num_aleatorios)):
    num_aleatorios[i] = (num_aleatorios[i - 1] *
                         multiplicador + incremento) % modulo

keystream_bits = num_aleatorios

# Inicialização da GUI
root.mainloop()

# 157 linhas de código

# Observações: Esse metódo com certeza não é o mais seguro, porém é rápido e fácil de fazer. Sendo assim ideal pra fins educativos

# Fontes:
# https://demonstrations.wolfram.com/LinearCongruentialGenerators/
# https://pt.wikipedia.org/wiki/Pseudoaleatoriedade
# https://www.kaspersky.com.br/resource-center/definitions/encryption
# http://www.serafim.eti.br/academia/recursos/Roteiro_05-Cifras_de_Fluxo_e_Bloco.pdf
# http://sbseg2016.ic.uff.br/pt/files/anais/wticg/ST4-2.pdf
# http://uab.ifsul.edu.br/tsiad/conteudo/modulo5/src/biblioteca/1_Leitura_Complementar_Algoritmos_de_Criptografia.pdf.pdf
# https://institucional.upis.br/biblioteca/pdf/revistas/revista_informatica/Cavalcante_teoria_numeros_criptografia_2005_UPIS.pdf
#
# Braga, Alexandre, and Ricardo Dahab. "Introdução à criptografia para programadores: Evitando maus usos da criptografia em sistemas de 
# software." Sociedade Brasileira de Computação (2015).