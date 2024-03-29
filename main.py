from flask import Flask
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('casas.csv')
colunas = ['tamanho' , 'preco']
df = df[colunas]

X = df.drop('preco', axis=1)#axis é o índice da coluna, no caso tamanho
y = df['preco']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

app = Flask(__name__)
#definindo a rota home
@app.route('/')
#qual função acessa na rota:
def home():
    return "Rota ok."

@app.route('/cotacao/<int:tamanho>')
def cotacao(tamanho):
    preco = modelo.predict([[tamanho]])
    return str(preco)

app.run(debug=True) #executa 