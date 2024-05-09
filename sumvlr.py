import os
import xml.etree.ElementTree as ET

def sumarizar_valores_em_arquivos(path):
    total_valor = 0

    # Iterar sobre todos os arquivos na pasta
    for filename in os.listdir(path):
        if filename.endswith(".xml"):
            file_path = os.path.join(path, filename)

            # Parsing do arquivo XML
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Encontrar a tag <vCFe> e somar ao total
            for vcfe in root.iter('vCFe'):
                total_valor += float(vcfe.text)

            # Encontrar a tag <vNF> e somar ao total
            for vnf in root.iter('vNF'):
                total_valor += float(vnf.text)

    return total_valor

# Substitua 'caminho_da_sua_pasta' pelo caminho real onde estão os arquivos XML
caminho_pasta = 'xml'
total = sumarizar_valores_em_arquivos(caminho_pasta)

print(f"Total dos valores: {total}")