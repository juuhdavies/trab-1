from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quartos')
def quartos():
    # Lista de quartos simulada para exibição dinâmica no template
    opcoes_quartos = [
        {
            "nome": "Quarto Standard",
            "descricao": "Acomodação confortável ideal para estadias rápidas. Configuração flexível para solteiros ou casais.",
            "adultos": "1 a 2",
            "criancas": "0 a 1",
            "preco": 150.00
        },
        {
            "nome": "Quarto Executive Family",
            "descricao": "Espaço amplo projetado para famílias, oferecendo total conforto e privacidade.",
            "adultos": "1 a 3",
            "criancas": "0 a 2",
            "preco": 280.00
        },
        {
            "nome": "Master Suite Elfsong",
            "descricao": "A nossa melhor acomodação. Vista panorâmica, hidromassagem e serviços exclusivos inclusos.",
            "adultos": "1 a 3",
            "criancas": "0 a 2",
            "preco": 450.00
        }
    ]
    return render_template('quartos.html', quartos=opcoes_quartos)

@app.route('/reservas', methods=['GET', 'POST'])
def reservas():
    return render_template('reservas.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)