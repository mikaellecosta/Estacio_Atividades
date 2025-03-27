# Implemente um script em Python que realize as seguintes operações:
# Verifique se os diretórios de destino (pdf, txt, img) existem; caso contrário, crie-os.
# Mova os arquivos do diretório de trabalho para os diretórios correspondentes com base 
# em suas extensões.
# Trate possíveis exceções durante as operações, exibindo mensagens informativas 
# ao usuário.

import os
import shutil
import errno

with open ("errno.txt","w") as arquivo:
    listaErro = errno.errorcode

    # for code, erro in listaErro.items():
    #     arquivo.write(str(code))
    #     arquivo.write(":")
    #     arquivo.write(erro)
    #     arquivo.write("\n")

def criarDir(diretorios):
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            try:
                os.makedirs(diretorio)
                print(f"{diretorio} criado")
            except Exception as e:
                print(f"Erro inesperado ao criar {diretorio}!")
                print(e.errno)
                

def movArq(dirOrigem):
    for arquivo in os.listdir(dirOrigem):
        caminho_arquivo = os.path.join(dirOrigem, arquivo)
        print(caminho_arquivo, "1")
        if os.path.isfile(caminho_arquivo):
            extensao = arquivo.split('.')[-1].lower()
            print(extensao)
            if extensao in ['pdf','py','txt']:
                dirDestino = os.path.join(dirOrigem, extensao)
                print(dirDestino)
                shutil.move(caminho_arquivo, dirDestino)

if __name__ == "__main__":
    diretorioTrabalho = "DirTrabalho"
    diretorios = [os.path.join(diretorioTrabalho, 'pdf'),
                     os.path.join(diretorioTrabalho, 'txt'),
                     os.path.join(diretorioTrabalho, 'py')]
    criarDir(diretorios)
    movArq(diretorioTrabalho)