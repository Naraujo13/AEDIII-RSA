#Nicolas de Araujo - 22/03/17
#Estrutura contendo ascii criptografado, sera usada para descriptografar
dictionary = {}

#Chave Publica
E = 17
N = 3424467341


#Cria dicionario ascii criptografado com chave publica fornecida
for i in range (0, 128):
    C =(i**E) % N
    dictionary[C] = i

#Abre arquivo de entrada e de saida
encoded_file = open("entrada.txt")
decoded_file = open("saida.txt", "w")

#Le entrada e escreve no arquivo de saida usando o dicionario para descriptografar
for word in encoded_file.read().split():
   word_int = int(word)
   decoded_file.write((str(chr(dictionary[word_int]))))

#Fecha arquivos
encoded_file.close()
decoded_file.close()