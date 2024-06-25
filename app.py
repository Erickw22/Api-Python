from flask import Flask, jsonify, request

app = Flask (__name__)

livros = [
    {
        'id': 1,
        "titulo": 'O senhor dos Anéis- A Sociedade do Anel',
        'autor': 'J.R.R Tolken'
    },
    {
        'id': 2,
        "titulo": 'Vikings: A história definitiva dos povos do norte',
        'autor': 'Neil Price'
    },
    {
        'id': 3,
        "titulo": 'O Pequeno Príncipe',
        'autor': 'Saint-Exupéry'
    }
]

# Consultar (todos) os livros
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Consultar livros utilizando (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify (livro)
        
# Editar livros utilizando (id)
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livros_alterados = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livros_alterados)
            return jsonify(livros[indice])

# Adicionar novos livros utilizando
@app.route('/livros',methods=['POST'])
def adcionar_novos_livros():
    novos_livro = request.get_json()
    livros.append(novos_livro)

    return jsonify(livros)


#Exlcuir livros
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug= True) 