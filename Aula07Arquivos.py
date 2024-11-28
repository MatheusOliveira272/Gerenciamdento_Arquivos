#Trabalhando com arquivos no VSCode

'''-------------------Escrita-------------------'''

# Abre (ou cria) o arquivo "arquivo.txt" em modo de escrita ('w')
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Conteúdo que você deseja escrever no arquivo")

# Abrir o arquivo no modo de escrita. Se o arquivo não existir, ele será criado. Se o arquivo já existir, ele será sobrescrito.
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Escrevendo novas informações no arquivo.\n")


'''-------------------Leitura-------------------'''

# Abrir o arquivo no modo de leitura. Este modo é usado para ler o conteúdo de um arquivo. Se o arquivo não existir, ocorrerá um erro.
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)  # Exibe o conteúdo do arquivo

#Lendo linhas especificas
with open("arquivo.txt", "r") as arquivo:
    linhas = arquivo.readlines()  # Cada linha é um item na lista
    for linha in linhas: #para ler tudo
        print(linha.strip())  # .strip() remove quebras de linha

#Lendo linhas especificas se tiro o for posso colocar a linha q quero ver
with open("testes.txt", "r") as arquivo:
    linhas = arquivo.readlines()  # Cada linha é um item na lista
    print(linhas[2])

'''------------------Acréscimo------------------'''

# Abrir o arquivo no modo de acréscimo. Esse modo permite adicionar conteúdo ao final do arquivo sem apagar o conteúdo existente.
with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Adicionando novas linhas ao final do arquivo.\n")



'''---------------Leitura/Escrita---------------'''

# Abrir o arquivo no modo de leitura e escrita
with open("arquivo.txt", "r+") as arquivo:
    conteudo = arquivo.read() #lê todo o conteúdo do arquivo.
    print("Conteúdo antes da escrita:", conteudo)
    
    # Escreve no começo do arquivo (sobrescreve o início do conteúdo) se eu mandar o cursor para lá usando : arquivo.seek(0)
    arquivo.write("Novo texto no início do arquivo.\n")

    # Ler o conteúdo novamente para ver as alterações
    arquivo.seek(0)  # Retorna para o início do arquivo
    conteudo_atualizado = arquivo.read()
    print("Conteúdo após a escrita:", conteudo_atualizado)
    
    
'''---------------Fechar o Arquivo---------------'''
    
#Fechar o arquivo. O método `with open()` fecha automaticamente o arquivo após o uso. **Evita erros** de acesso e libera memória, o que é uma boa prática. Exemplo:


with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Texto adicional\n")
    
# Aqui, o arquivo já está fechado automaticamente.

 
'''------------------------------------------------------------------'''
'''Aqui está uma síntese das operações de leitura e escrita em arquivos para uso no VS Code:

### 1. **Criar ou Abrir Arquivo**
Para criar ou abrir um arquivo no VS Code, use a função `open()` com os modos apropriados:

- **Modo `r`**: Somente leitura. Ex.: `open("arquivo.txt", "r")`
- **Modo `w`**: Escrita, apaga o conteúdo anterior. Ex.: `open("arquivo.txt", "w")`
- **Modo `a`**: Acréscimo, adiciona conteúdo ao final sem apagar. Ex.: `open("arquivo.txt", "a")`
- **Modo `r+`**: Leitura e escrita.


'''