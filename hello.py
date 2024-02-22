# A very simple Flask Hello World app for you to get started with...
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return """<h1>Avaliação contínua: Aula 030</h1>
              <br>
              <ul>
                <li><a href=''>Home</a></li>
                <li><a href=''>Identificação</a></li>
                <li><a href=''>Contexto da requisição</a></li></ul>
              <ul>"""