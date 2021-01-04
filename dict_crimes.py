crimes = ["Tráfico de drogas", "Furto (art. 155)", "Roubo (art. 157)", "Lei Maria da Penha", "Roubo", "Transito"]

# Trafico:
trafico = ["Tráfico (art. 33)", "Porte de droga para consumo (art. 28)"]
trafico_artigo = ["33", "28"]
trafico_filename = []
for art in trafico_artigo:
    arquivo = f"CRDen_{art}_drogas.docx"
    trafico_filename.append(arquivo)

# Furto:
furto = ["Furto simples (art. 155)", "Furto qualificado por rompimento de obstáculo (art. 155, § 4º, I)",
         "Furto qualificado mediante escalada (art. 155, § 4º, II)"]
furto_artigo = ["155", '155_parIV_I', "155_par4_II"]
furto_filename = []
for art in furto_artigo:
    arquivo = f"CRDen_{art}_furto.docx"
    furto_filename.append(arquivo)



# dict(zip(cidades,juizo))

# Lei Maria da Penha:
lei_maria_penha = ["lesão corporal (art. 129, § 9º)", "Ameaça (art. 147)", "Lesão e Ameaça (arts. 129, § 9º e 147)", "Vias de fato (art. 21, Dec-Lei 3688/41)" ]
lmp_artigo = ["129", "147", "129_147", "21"]
lmp_filename = []
for art in lmp_artigo:
    arquivo = f"CRDen_{art}_lmp.docx"
    lmp_filename.append(arquivo)

# roubo:
roubo = ["roubo simples (art.157)", "roubo majorado (concurso de pessoas - 157, § 2º, II)",
         "roubo majorado (arma de fogo - art. 157, § 2ª-A, I)" ]
roubo_artigo = ["157", "157_par2_II", "157_par2-A_I"]
roubo_filename = []
for art in roubo_artigo:
    arquivo = f"CRDen_{art}_roubo.docx"
    roubo_filename.append(arquivo)

# transito:
transito = ["Leão culposa na direção de veículo (art.303)", "Embriaguez ao volante (art. 306)"]
transito_artigo = ["303", "306"]
transito_filename = []
for art in transito_artigo:
    arquivo = f"CRDen_{art}_CTB.docx"
    transito_filename.append(arquivo)
crimes_especie = trafico + furto + lei_maria_penha + roubo + transito
crimes_filename = trafico_filename + furto_filename + lmp_filename + roubo_filename + transito_filename

crimes_especie2 = crimes_especie
crimes_especie2.append("Outro(s) crime(s)- selecione e insira no próximo campo")


dict_crimes = dict(zip(crimes_especie, crimes_filename))
dict_trafico = dict(zip(trafico, trafico_filename))
dict_furto = dict(zip(furto, furto_filename))
dict_lmp = dict(zip(lei_maria_penha, lmp_filename))

med_prot = ["deferimento", "indeferimento"]
med_prot_filename= ["CRParec_medida_protetiva_deferimento.docx", "CRParec_medida_protetiva_indeferimento.docx"]
dict_med_prot = dict(zip(med_prot, med_prot_filename))

prisao = ["conversão em prisão preventiva", "liberdade provisória", "liberdade provisória com medidas protetivas"]
prisao_filenames = ["CRParec_prisao_preventiva.docx", "CRParec_liberdade_provisoria.docx", "CRParec_liberdade_provisoria_medida_protetiva.docx"]
dict_prisao = dict(zip(prisao, prisao_filenames))

blanck = "blanck.docx"