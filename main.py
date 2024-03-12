from flask import Flask

app = Flask('meu app')
#definindo a rota home
@app.route('/')
#qual função acessa na rota:
def home():
    return "Rota ok."

app.run() #executa 