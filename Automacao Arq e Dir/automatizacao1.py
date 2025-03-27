# Implemente um script em Python que realize as seguintes operações:
# 1. Leia o conteúdo de um arquivo de texto
# 2. Escreva o conteúdo lido em um novo arquivo, adicionando uma linha de cabeçalho.
# 3. Trate possíveis exceções durante as operações, 
# exibindo mensagens informativas ao usuário.

import os

def main(caminhoLer,caminhoEscrever):
    try:
        with open (caminhoLer, "r") as arquivoLer:
            conteudo = arquivoLer.read() ## SALVA O CONTEUDO DO ARQUIVO
    except FileNotFoundError:
        print(f"Arquivo {caminhoLer} não existe!")
    except PermissionError:
        print(f"Erro de permissão no arquivo {caminhoLer}!")
    except Exception as e:
        print(f"Erro inesperado ao ler {caminhoLer}!")

    try:
        with open (caminhoEscrever, "w") as arquivoEscrever:
            arquivoEscrever.write("CABECALHO DE TESTE\n\n")
            arquivoEscrever.write(conteudo)
    except PermissionError:
        print(f"Erro de permissão no arquivo {caminhoEscrever}!")
    except Exception as e:
        print(f"Erro inesperado ao ler {caminhoLer}!")
        
if __name__ == "__main__":
    main("fatura.txt","faturaCopia2.txt")
       
        




        