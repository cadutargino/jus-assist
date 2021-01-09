import re

# nomeRegex = re.compile(r'(Indiciad([oa])|Autor): -(.*?)-')
#                 mo = nomeRegex.search(BOText)
#                 indiciado = mo.group()
# arquivo = "numero_1500286-33.2020.8.26.0573_emaisalgumacoisa"
# numRegex = re.compile(r'\d{4,7}-\d{2}.\d{4}.\d.\d{2}.\d{4}')
# mo_num = numRegex.search(arquivo)
# numero = mo_num.group()
# print(numero)
# hora1 = "14:15   "
# horateste = "entre 14:15 e 15:30"
# horateste.strip()
# print(len(horateste.strip()))
# print(len(hora1.strip()))
# horaregex = re.compile(r'\d{1,2}:\d{2}')
# if ":" in hora:
#     hora = hora.split(sep=':')
#     hora = 'por volta de ' + hora[0] + 'h' + hora[1] + 'min'

# import comarcas
# print(comarcas.grandes      )
#
# if "Botucatu" in comarcas.grandes:
#     print("yes")
# else:
#     print("no")
# teste = "Rua Quinze De Novembro"
#
#
# def titled_string_correction(string):
#     list_string = string.split()
#     new_list = []
#     new_string = ""
#     for word in list_string:
#         if len(word) <= 2:
#             new_list.append(word.lower())
#         else:
#             new_list.append(word)
#     new_string = " ".join(new_list)
#     return new_string
#
# print(titled_string_correction(teste))

# from datetime import datetime
# now = datetime.now()
#
#
# meses_2 = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho',
#                          7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro',
#                          12: 'dezembro'}
#
# data_atual = f"{now.day} de {meses_2[now.month]} de {now.year}"
#
# def titled_string_rectifier(string):
#     list_string = string.split()
#     new_list = []
#     new_string = ""
#     for word in list_string:
#         if len(word) > 3 or len(list_string) < 3 or word not in list_string[1: -1]:
#             new_list.append(word)
#         else:
#             new_list.append(word.lower())
#     new_string = " ".join(new_list)
#     return new_string
#
# string1 = "Embu Das Artes"
# string2 = "Carlos De Oliveira Dos Santos Da Silva"
# string3= "Preta Gil"
# string4 = " Gil Diniz Dos Santos"
#

# regex para pegar mais de uma testemunha: temunha: - (.+?) - Presente ao
# temunha: - (.+?) - (Presente ao|Não presente)(.+?)(Policial|policial|POLICIAL)
# - [ ^ -]+ - [ ^ -]+ - (Presente ao | Não presente ao)


# Estratégia regex:
# (Autor|Indiciad[oa]|Investigad[oa]): (.+)Vítima: - (.+?) - (Presente ao|Não presente ao)

# 1) extrai o mais geral para vítima, indiciado, testemunha
# tima: (.+) - (Presente ao|Não presente ao)

# 2) No texto extraído verifica quantas pessoas com o regex sobre o trecho:
# - [ ^ -]+ - (Presente ao | Não presente ao)

# 3) if vulgo in resultados,  faz slice para tirar o vulgo:



