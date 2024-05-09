from flask import Flask, render_template, jsonify
import os
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sumarizar-cfe')
def sumarizar_valores_vcfe():
    caminho_pasta_vcfe = 'vcfe'
    total_vcfe = sumarizar_valores_em_arquivos_CFE(caminho_pasta_vcfe, 'vCFe')
    return jsonify(total=total_vcfe)

@app.route('/sumarizar-nfe')
def sumarizar_valores_vnfe():
    caminho_pasta_vnfe = 'vnfe'
    total_vnfe = sumarizar_valores_em_arquivos_NFE(caminho_pasta_vnfe, '{http://www.portalfiscal.inf.br/nfe}vNF')
    return jsonify(total=total_vnfe)

def sumarizar_valores_em_arquivos_CFE(path, tag_nome):
    total_valor = 0

    # Iterar sobre todos os arquivos na pasta
    for filename in os.listdir(path):
        if filename.endswith(".xml"):
            file_path = os.path.join(path, filename)

            # Parsing do arquivo XML
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()

                # Encontrar a tag especificada e somar ao total
                for tag in root.iter(tag_nome):
                    try:
                        total_valor += float(tag.text)
                    except ValueError:
                        print(f"Valor inválido encontrado em {file_path}: {tag.text}")
            except ET.ParseError:
                print(f"Erro ao fazer parsing do arquivo XML: {file_path}")

    return total_valor

def sumarizar_valores_em_arquivos_NFE(path, tag_nome):
    total_valor = 0

    # Iterar sobre todos os arquivos na pasta
    for filename in os.listdir(path):
        if filename.endswith(".xml"):
            file_path = os.path.join(path, filename)

            # Parsing do arquivo XML
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()

                # Encontrar a tag especificada e somar ao total
                for tag in root.iter(tag_nome):
                    try:
                        total_valor += float(tag.text)
                    except ValueError:
                        print(f"Valor inválido encontrado em {file_path}: {tag.text}")
            except ET.ParseError:
                print(f"Erro ao fazer parsing do arquivo XML: {file_path}")

    return total_valor

if __name__ == '__main__':
    app.run(debug=True)