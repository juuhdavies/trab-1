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

@app.route('/reservas_conferencia', methods=['GET', 'POST'])
def reservas_conferencia():
    return render_template('reservas_conferencia.html')

@app.route('/login')
def login():
    return render_template('login.html')

# área de administração
@app.route('/login_colaborador')
def login_colaborador():
    return render_template('login_colaborador.html')

@app.route('/colaborador/inicio')
def colaborador_inicio():
    # Dados simulados para os cards de resumo do painel
    resumo_hoje = {
        "checkins_pendentes": 5,
        "checkouts_hoje": 3,
        "quartos_livres": 12,
        "mensagens": 2
    }
    return render_template('colaborador_inicio.html', resumo=resumo_hoje)

@app.route('/colaborador/mapa', methods=['GET', 'POST'])
def colaborador_mapa():
    # Data padrão simulando o dia de hoje
    data_selecionada = request.form.get('data_filtro', '2026-06-15')
    
    # Dados simulados com a nova previsão de check-out adicionada
    mapa_quartos = [
        {"numero": "101", "tipo": "Standard", "status": "Ocupado", "hospede": "Tav", "checkout": "16/06/2026"},
        {"numero": "102", "tipo": "Standard", "status": "Livre", "hospede": "-", "checkout": "-"},
        {"numero": "103", "tipo": "Standard", "status": "Reservado", "hospede": "Gale", "checkout": "18/06/2026"},
        {"numero": "201", "tipo": "Executive Family", "status": "Ocupado", "hospede": "Shadowheart", "checkout": "15/06/2026"},
        {"numero": "202", "tipo": "Executive Family", "status": "Livre", "hospede": "-", "checkout": "-"},
        {"numero": "301", "tipo": "Master Suite Elfsong", "status": "Reservado", "hospede": "Astarion", "checkout": "20/06/2026"}
    ]
    return render_template('colaborador_mapa.html', mapa=mapa_quartos, data=data_selecionada)

@app.route('/gerente/cadastro', methods=['GET', 'POST'])
def gerente_cadastro():
    return render_template('gerente_cadastro.html')

@app.route('/colaborador/fluxo', methods=['GET', 'POST'])
def colaborador_fluxo():
    return render_template('colaborador_fluxo.html')

@app.route('/colaborador/reserva', methods=['GET', 'POST'])
def colaborador_reserva():
    return render_template('colaborador_reserva.html')

@app.route('/gerente/faturamento', methods=['GET', 'POST'])
def gerente_faturamento():
    data_inicio = request.form.get('data_inicio', '2026-06-01')
    data_fim = request.form.get('data_fim', '2026-06-15')
    
    # Valores consolidados simulados para o relatório
    faturamento = {
        "total_hospedagem": 14250.00,
        "total_salas": 5800.00,
        "total_geral": 20050.00
    }
    return render_template('gerente_faturamento.html', faturamento=faturamento, inicio=data_inicio, fim=data_fim)

if __name__ == '__main__':
    app.run(debug=True)