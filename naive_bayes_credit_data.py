
import pandas

base = pandas.read_csv('E:\\Udemy - Cursos\\MachineLearning\\Arquivos\\CreditData.csv')
base.loc[base.age < 0, 'age'] = 40.92
               
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

from sklearn.preprocessing import Imputer # Trata as linhas/colunas com dados faltantes
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

from sklearn.cross_validation import train_test_split # Dividir entre treinamento e teste
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
classificador.fit( previsores_treinamento, classe_treinamento )

previsoes = classificador.predict(previsores_teste)

# importação da biblioteca
# criação do classificador

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes) # Verificando os valores corretos dos não corretos

classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)


