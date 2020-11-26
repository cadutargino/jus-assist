import PyPDF2, docx, re, genderbr, pdfplumber
from PyPDF2 import PdfFileReader
import streamlit as st
import os
import base64



def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()

	return all_page_text


st.title('Assistente de redação de peças jurídicas')
st.subheader('Módulo Denúncia')
st.text('Sistema auxiliar para produção de denúncia a partir do PDF do boletim de ocorrência')
doc_file = st.file_uploader("Insira Boletim de Ocorrência", type=["pdf"])
if st.button("Process"):
    if doc_file is not None:
        file_details = {"Filename":doc_file.name,"FileType":doc_file.type,"FileSize":doc_file.size}
        BOText = read_pdf(doc_file)
        st.write(BOText)
        
        # Extrai local
        LocalRegex = re.compile(r'Local: (.*?)Tipo')
        local_mo = LocalRegex.search(BOText)
        Local = local_mo.group()
        Local = Local[6:-4]
        Local = Local.title().strip()
        
        #Extrai indiciado/autor
        nomeRegex = re.compile(r'(Indiciad(o|a)|Autor): -(.*?)-')
        mo = nomeRegex.search(BOText)
        indiciado = mo.group()
        if 'Autor' in indiciado:
            indiciado = indiciado[9:-2]
        else:
            indiciado = indiciado[13:-2]
        
        #Extrai sexo
        nome = indiciado.split()[0]
        sexo = genderbr.get_gender(nome)
        
        #Extrai data e hora
        DataHoraRegex = re.compile(r'Ocorrência: (.*?)Comu')
        dh_mo = DataHoraRegex.search(BOText)
        DataHora = dh_mo.group()
        DataHora = DataHora[:-4]
        DataHora = DataHora.lower()
        data_hora = DataHora[11:].strip()
        data = DataHora.split()[1]
        hora = DataHora.split()[3]
        lista_hora = [data, hora]
        
        if ":" in hora:
            hora = hora.split(sep = ':')
            hora = 'por volta de '+ hora[0] + 'h' + hora[1] + 'min'
        data = data.split(sep = '/')
        meses = { '01':'janeiro', '02':'fevereiro', '03':'março', '04':'abril', '05':'maio', '06':'junho', '07':'julho', '08':'agosto', '09':'setembro', '10':'outubro', '11':'novembro','12':'dezembro'}
        data_ext = data[0] +' de ' + meses[data[1]] + ' de ' + data[2]

        #Escolhe modelo pelo sexo
        if sexo == "M":
            d = docx.Document('CRDen.docx')
        else:
            d = docx.Document('CRDen_a.docx')
        
        #Extrai numero do processo
        numero = doc_file.name[-29:-4] # numero do processo para incluir no nome do arquivo final   
        
        # Mostrando resultados 
        st.write(file_details)
        st.write(Local)
        st.write(indiciado)
        st.write(sexo)
        st.write(numero)
        st.write(data_ext)
        st.write(hora)
        
    else:
        st.write('Arquivo não PDF')

                

    # Trocar o horario na denuncia        

                        
    for para in range(len(d.paragraphs)):
        if 'Consta' in d.paragraphs[para].text:
            for i in range(len(d.paragraphs[para].runs)):
                    if 'data' in d.paragraphs[para].runs[i].text:
                        d.paragraphs[para].runs[i].text = data_ext
                        d.paragraphs[para].runs[i].underline = False

    # Trocar endereço na denuncia                    
    for para in range(len(d.paragraphs)):
        if 'Consta' in d.paragraphs[para].text:
            for i in range(len(d.paragraphs[para].runs)):
                    if 'endereco' in d.paragraphs[para].runs[i].text:
                        d.paragraphs[para].runs[i].text = Local
                        d.paragraphs[para].runs[i].underline = False
    # Trocar hora na denúncia
    for para in range(len(d.paragraphs)):
        if 'Consta' in d.paragraphs[para].text:
            for i in range(len(d.paragraphs[para].runs)):
                    if 'hora' in d.paragraphs[para].runs[i].text:
                        d.paragraphs[para].runs[i].text = hora
                        d.paragraphs[para].runs[i].underline = False


#  for i in range(len(d.paragraphs[4].runs)):
#   print(str(i) + '   :   ' + d.paragraphs[4].runs[i].text)


    # Trocar o nome na Denúncia

    for para in range(len(d.paragraphs)):
        if 'Consta' in d.paragraphs[para].text:
            for i in range(len(d.paragraphs[para].runs)):
                if d.paragraphs[para].runs[i].bold == True:
                    d.paragraphs[para].runs[i].text = indiciado

    for para in range(len(d.paragraphs)):
        if 'Ante o exposto' in d.paragraphs[para].text:
            for i in range(len(d.paragraphs[para].runs)):
                if d.paragraphs[para].runs[i].bold == True:
                    d.paragraphs[para].runs[i].text = indiciado
    
    for para in range(len(d.paragraphs)):
        if 'Ofereço denúncia em separado' in d.paragraphs[para].text:
            for i in range(len(d.paragraphs[para].runs)):
                if d.paragraphs[para].runs[i].bold == True:
                    d.paragraphs[para].runs[i].text = indiciado        


    # Substituindo o número do processo no arquivo Word:
    for para in range(len(d.paragraphs)):
        for run in range(len(d.paragraphs[para].runs)):
                d.paragraphs[para].runs[run].text = re.sub(r'\d{4,7}-\d{2}.\d{4}.\d.\d{2}.\d{4}', numero, d.paragraphs[para].runs[run].text)
        print(d.paragraphs[para].text) 

    d.save("CRDen_" + numero +".docx")
    
    st.markdown(get_binary_file_downloader_html("CRDen_" + numero +".docx", '  minuta da denúncia'), unsafe_allow_html=True)

  
    #@st.cache
    #def get_data():
    #    url = "http://data.insideairbnb.c" \
    #          "om/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
    #    return pd.read_csv(url)

    #df = get_data()
    #st.title('Streamlit 101: An in depth introduction')
    #st.markdown('Welcome to this in-depth introduction to [...].')

    #st.header('Customary quote')
    #st.markdown('> I just love to go home, no matter where I am [...]')
        
    #st.dataframe(df.head())


    #st.title('Streamlit tutorials')

