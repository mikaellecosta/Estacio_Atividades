def eh_sufixo(padrao, indice):  ## ABA  --> 1 
    tamanho_padrao = len(padrao) ## 3
    tamanho_sufixo = tamanho_padrao - indice  ## 3 - 1 = 2
    for i in range(tamanho_sufixo): ## 2
        if padrao[i] != padrao[indice + i]: ## padrao[0] != padrao [1+0]
            return False
    return True

def pre_process_tabela_carac_ruim(padrao):
    tabela_caracter_ruim = {}
    tamanho_padrao = len(padrao)

    for i in range(tamanho_padrao - 1):
        tabela_caracter_ruim[padrao[i]] = tamanho_padrao - i - 1

    return tabela_caracter_ruim
                                        
def pre_process_sufixo_bom(padrao):
    tamanho_padrao = len(padrao)
    tabela_bom_sufixo = [tamanho_padrao] * (tamanho_padrao + 1)
    ultimo_prefixo = tamanho_padrao

    for i in range(tamanho_padrao - 1, -1, -1): 
        if eh_sufixo(padrao, i): 
            ultimo_prefixo = i 
        
        tabela_bom_sufixo[i] = tamanho_padrao - ultimo_prefixo + i

    for i in range(tamanho_padrao):
        j = tamanho_padrao - 1

        while j >= 0 and padrao[i - j] == padrao[tamanho_padrao - j - 1]:
            j -= 1

        if j == -1:
            ultimo_prefixo = i

        tabela_bom_sufixo[tamanho_padrao - j - 1] = tamanho_padrao + i - ultimo_prefixo

    return tabela_bom_sufixo

def busca_boyer_moore(texto, padrao):
    tabela_caracter_ruim = pre_process_tabela_carac_ruim(padrao)
    tabela_bom_sufixo = pre_process_sufixo_bom(padrao)

    tamanho_texto = len(texto)
    tamanho_padrao = len(padrao)
    i = 0

    while i <= tamanho_texto - tamanho_padrao:
        j = tamanho_padrao - 1
        while j >= 0 and padrao[j] == texto[i + j]:
            j -= 1
        if j < 0:
            # Ocorrência encontrada
            print(f'O padrão ocorre na posição {i} no texto.')
            i += tabela_bom_sufixo[0]
        else:
            deslocamento_caracter_ruim = tabela_caracter_ruim.get(texto[i + j], -1)
            deslocamento_bom_sufixo = tabela_bom_sufixo[j]
            i += max(deslocamento_caracter_ruim, deslocamento_bom_sufixo)

# Exemplo de uso:
texto = "AABCAAABABAABABAAABABAABACABAABABAAABABAABABAAABABAABACABAABABAAABABAABABAAABABAABACABAABABAAABABAABABA"
padrao = "BA"
busca_boyer_moore(texto, padrao)