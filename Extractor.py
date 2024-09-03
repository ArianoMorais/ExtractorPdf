import os
import re
from PyPDF2 import PdfReader

def extrair_info_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        
        page = pdf_reader.pages[0]
        texto = page.extract_text()

        cota_match = re.search(r'COTA n\. 0*(\d+)/(\d+)', texto)
        tipo = 'Cota' if cota_match else 'TipoDesconhecido'
        
        numero_cota = cota_match.group(1).lstrip('0') if cota_match else 'NumeroDesconhecido'
        
        materias = {'ADM': 'Procedimentos Administrativos',
                    'CNT': 'COORDENAÇÃO DE CONTENCIOSO JUDICIAL',
                    'CTA': 'Contencioso Administrativo',
                    'FIS': 'Procedimentos Fiscais',
                    'REG': 'Procedimentos Regulatórios'}

        assunto = "ASSUNTO"
    
        for sigla, expressao in materias.items():
            if re.search(rf'\b{re.escape(expressao)}\b', texto):
                materia = sigla
                descricao_materia = materias[sigla]
                break
        else:
            materia = 'MateriaDesconhecida'
            descricao_materia = 'DescricaoDesconhecida'

        interessados = ['AC', 'AF', 'AFCA', 'AFCA1', 'AFCA2', 'AFCA3', 'AFCA4', 'AFCA5', 'AFCA6',
                        'AFFO', 'AFFO1', 'AFFO2', 'AFFO3', 'AFFO4', 'AFFO5', 'AFFO6',
                        'AFIS', 'AFIS1', 'AFIS2', 'AFIS3', 'AFIS4', 'AFIS5', 'AFPE', 'AFPE-BORA',
                        'AFPE-TR', 'AFPE1', 'AFPE2', 'AFPE3', 'AFPE4', 'AFPE5', 'AFPE6', 'AFPE7',
                        'AIN', 'AIN3', 'APC', 'ARI', 'ARI1', 'ARI2', 'ARU', 'ATC', 'AUD', 'CD',
                        'CODI', 'CODI2', 'CODI3', 'CODI4', 'CODI5', 'CODI6', 'CODI7', 'CODI8',
                        'COGE', 'COGE1', 'COGE2', 'COGE3', 'COGE4', 'COGE5', 'COGE6', 'COGE7',
                        'COQL', 'COQL1', 'COQL2', 'COQL3', 'COQL6', 'COQL7', 'COQL8',
                        'COUN', 'COUN1', 'COUN2', 'COUN3', 'COUN4', 'COUN5', 'COUN6', 'COUN7', 'COUN8',
                        'CPAE', 'CPAE1', 'CPAE2', 'CPAE3', 'CPAE4', 'CPAE5', 'CPAE6',
                        'CPOE', 'CPOE1', 'CPOE2', 'CPOE3',
                        'CPRP', 'CPRP1', 'CPRP2', 'CPRP3',
                        'CRG', 'FIGF', 'FIGF1', 'FIGF2', 'FIGF3', 'FIGF4', 'FIGF5', 'FIGF6',
                        'FISF', 'FISF1', 'FISF2', 'FISF3', 'FISF4', 'FISF5',
                        'GIDS', 'GIDS1', 'GIDS2', 'GIDS3', 'GIDS4', 'GIDS5']

        for interessado in interessados:
            if re.search(rf'\b{re.escape(interessado)}\b', texto):
                sigla_interessado = interessado
                break
        else:
            sigla_interessado = 'InteressadoDesconhecido'

        # Mapeamento de setores conforme a matéria
        setores = {'ADM': 'PFE-PA', 'CNT': 'PFE-CO', 'CTA': 'PFE-CA', 'FIS': 'PFE-PF', 'REG': 'PFE-PR'}
        setor = setores.get(materia, 'SetorDesconhecido')

        # Extração do NUP
        nup_match = re.search(r'NUP: (\d+\.\d+)/(\d+)-(\d+)', texto)

        nup = f"{nup_match.group(1)}_{nup_match.group(2)}_{nup_match.group(3)}" if nup_match else 'NUPDesconhecido'

        nup_sem_pontos = nup.replace(".", "")

        nup_completo = nup_sem_pontos.replace("_", "")

        cota = f"{numero_cota}-{cota_match.group(2)}_{materia}_{assunto}_{sigla_interessado}_{setor}_{nup_completo}" if cota_match else 'CotaDesconhecida'
        
        return tipo, cota

def renomear_arquivos_pdfs(diretorio):
    for filename in os.listdir(diretorio):
        if filename.endswith(".pdf"):
            file_path = os.path.join(diretorio, filename)
            
            tipo, cota = extrair_info_pdf(file_path)
            
            novo_nome = f"{tipo}_{cota}.pdf"
            novo_caminho = os.path.join(diretorio, novo_nome)
            
            os.rename(file_path, novo_caminho)
            print(f"Arquivo renomeado: {filename} -> {novo_nome}")

caminho_da_pasta = r'C:\Users\Proeficiencia\Documents\Arquivo_teste'
renomear_arquivos_pdfs(caminho_da_pasta)