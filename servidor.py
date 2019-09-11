from flask import Flask, render_template, request, session, redirect
from usuario import *
from gasto_renda import *
app = Flask(__name__)
app.config['SECRET_KEY'] = '43r78934yt6y5907'

lista_usuarios = []
lista_gastos = [Gasto('Presente','Fixo', '200'), Gasto('Almoço IF','Variado','50')]
lista_rendas = [Renda('Bolsa Pesquisa','200'), Renda('Auxílio','200')]

valor_renda = 250
valor_gasto = 400

@app.route("/")
def abrir_inicial():
    if session.get('user'):
        return render_template('inicio.html', valor_gasto=valor_gasto, valor_renda=valor_renda, lista_renda=lista_rendas, lista_gasto=lista_gastos)
    return redirect("form_login")

@app.route("/form_login")
def abrir_form_login():
    return render_template('login.html')

@app.route("/form_cadastro")
def abrir_form_cadstro():
    return render_template('cadastro_usuario.html')

@app.route("/login")
def login():
    user = request.args.get('nome_usuario')
    senha = request.args.get('senha')
    if user == 'admin' and senha == 'admin':
        session['user'] = user
        return redirect("/")
    #else:

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')

@app.route("/exibir_historico")
def abrir_historico():
    return render_template('historico.html')

@app.route("/exibir_sobre")
def abrir_sobre():
    return render_template('sobre.html')

@app.route("/form_renda")
def abrir_form_renda():
    return render_template('form_renda.html')

@app.route("/form_gasto")
def abrir_for_gasto():
    return render_template('form_gasto.html')

@app.route("/adicionar_renda", methods=['POST'])
def adicionar_renda():
    global valor_renda
    nome = request.form['nome_renda'] 
    valor = request.form['valor_renda']
    lista_rendas.append(Renda(nome, valor))
    valor_renda += float(valor)
    return redirect('/')

@app.route("/adicionar_gasto", methods=['POST'])
def adicionar_gasto():
    global valor_gasto
    nome = request.form['nome_gasto']
    valor = request.form['valor_gasto']
    tipo = request.form['tipo_gasto']
    lista_gastos.append(Gasto(nome, valor, tipo))
    valor_gasto += float(valor)
    return redirect('/')

@app.route("/cancelar_operacao")
def cancelar():
    return redirect("/")

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastro_usuario():
    nome = request.form['nome_completo']
    email = request.form['email']
    user = request.form['nome_usuario']
    senha = request.form['senha']
    senha_confirm = request.form['senha_confirm']
    lista_usuarios.append(Usuario(nome, email, user, senha))
    return redirect('/')

def update_valores(valor_gasto, valor_renda):
    soma = 0
    for r in lista_rendas:
        soma += int(r.valor)
    valor_renda += soma

    soma = 0
    for g in lista_gastos:
        soma += int(g.valor)
    valor_gasto += soma

    return valor_renda, valor_gasto


app.run(debug=True, host='0.0.0.0')