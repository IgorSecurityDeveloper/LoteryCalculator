import pandas as pd
from flask import Flask, jsonify, request

# Configuração do Flask
dataAnalyse = Flask(__name__)

# Função para carregar e processar os dados
def carregar_dados(caminho_arquivo):
    dados = pd.read_excel(caminho_arquivo)
    numeros = dados.iloc[:, 1:]  # Considera colunas com os números sorteados
    return numeros

# Função para calcular frequência e probabilidade
def calcular_probabilidades(numeros):
    frequencia = numeros.stack().value_counts().sort_index()
    total_sorteios = numeros.shape[0]
    probabilidades = (frequencia / total_sorteios).sort_values(ascending=False)
    return probabilidades

# Rota para análise
@dataAnalyse.route('/analisar', methods=['POST'])
def analisar():
    caminho_arquivo = request.json.get('caminho_arquivo')
    numeros = carregar_dados(caminho_arquivo)
    probabilidades = calcular_probabilidades(numeros)
    return jsonify(probabilidades.to_dict())

# Rodar o servidor
if __name__ == '__main__':
    dataAnalyse.run(debug=True)