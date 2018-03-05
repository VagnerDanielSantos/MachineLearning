# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas

base = pandas.read_csv('E:\\Udemy - Cursos\\MachineLearning\\Arquivos\\census.csv')

previsores = base.iloc[:, 0:14].values

classe = base.iloc[:, 14].values

from sklearn.preprocessing import LabelEncoder # Classe responsável por fazer transformação de string para numerico

labelencoder_previsores = LabelEncoder()

labels = labelencoder_previsores.fit_transform(previsores[: , 1]) # Método para transformar a coluna string em numérico 

# INÍCIO - Transformando categorico para numerico 
previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[: , 1]) 
previsores[:, 3] = labelencoder_previsores.fit_transform(previsores[: , 3]) 
previsores[:, 5] = labelencoder_previsores.fit_transform(previsores[: , 5]) 
previsores[:, 6] = labelencoder_previsores.fit_transform(previsores[: , 6]) 
previsores[:, 7] = labelencoder_previsores.fit_transform(previsores[: , 7]) 
previsores[:, 8] = labelencoder_previsores.fit_transform(previsores[: , 8]) 
previsores[:, 9] = labelencoder_previsores.fit_transform(previsores[: , 9]) 
previsores[:, 13] = labelencoder_previsores.fit_transform(previsores[: , 13]) 
# FIM - Transformando categorico para numerico

from sklearn.preprocessing import LabelEncoder, OneHotEncoder # Classe responsável por classificar ( numericamente ) a coluna race 

onehotencoder = OneHotEncoder(categorical_features = [8])
previsores = onehotencoder.fit_transform(previsores).toarray()

previsores = base.iloc[:, 8:9].values # Necessário a transformação específica devido o campo será gerado float
previsores[:, 0] = labelencoder_previsores.fit_transform(previsores[: , 0])

onehotencoder = OneHotEncoder(categorical_features = [0])
previsores = onehotencoder.fit_transform(previsores).toarray()
previsores = base.iloc[:, 0:14].values

# INÍCIO - Transformando categorico para numerico 
previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[: , 1]) 
previsores[:, 3] = labelencoder_previsores.fit_transform(previsores[: , 3]) 
previsores[:, 5] = labelencoder_previsores.fit_transform(previsores[: , 5]) 
previsores[:, 6] = labelencoder_previsores.fit_transform(previsores[: , 6]) 
previsores[:, 7] = labelencoder_previsores.fit_transform(previsores[: , 7]) 
previsores[:, 8] = labelencoder_previsores.fit_transform(previsores[: , 8]) 
previsores[:, 9] = labelencoder_previsores.fit_transform(previsores[: , 9]) 
previsores[:, 13] = labelencoder_previsores.fit_transform(previsores[: , 13]) 
# FIM - Transformando categorico para numerico

onehotencoder = OneHotEncoder(categorical_features = [1, 3, 5, 6, 7, 8, 9, 13]) # Aplicando transformação 'DUMMY' para todas as colunas 

previsores = onehotencoder.fit_transform(previsores).toarray() # Efetivando a transformação

####################################################

labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)

# ESCALONAMENTO

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)


























