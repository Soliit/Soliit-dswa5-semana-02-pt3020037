# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():

    return """<h1>Avaliação contínua: Aula 030</h1>
              <ul>
                <li><a href='/'>Home</a></li>
                <li><a href='/identificacao'>Identificação</a></li>
                <li><a href='/contexto-da-requisicao'>Contexto da requisição</a></li></ul>
              <ul>"""


@app.route('/identificacao')
def identificacao():

    return  """<h1>Avaliação contínua: Aula 030</h1>
              <h2>Aluno: Daniel Alves Freitas</h2>
              <h2>Prontuário: PT3020037</h2>
              <h2>Instituição: IFSP</h2>
              <p><a href="/">Voltar</a></p>"""


@app.route('/contexto-da-requisicao')
def contexto_da_requisicao():

    user_agent = request.headers.get('User-Agent')
    html = '<h1>Avaliação contínua: Aula 030</h1>'
    html += f'<h2>Seu navegador é: {user_agent}'
    html += f'<h2>O IP do cumputador remoto é: {request.remote_addr}</h2>'
    html += f'<h2>O host da aplicação é: {request.host}</h2>'
    html += '<p><a href="/">Voltar</a></p>'

    return html