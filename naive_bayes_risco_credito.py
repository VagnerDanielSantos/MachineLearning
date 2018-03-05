# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:32:18 2018

@author: Administrator
"""

import pandas

base = pandas.read_csv('E:\\Udemy - Cursos\\MachineLearning\\Arquivos\\RiscoCredito.csv')

previsores = base.iloc[:, 0:4].values

classe = base.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
previsores[:, 1] = labelencoder.fit_transform(previsores[:, 1])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])

from sklearn.naive_bayes import GaussianNB

classificador = GaussianNB()
classificador.fit(previsores, classe)

# Histórico boa, divida alta, garantia nenhuma, renda > 35
# Histórico ruim, dívida alta, garantia adequada, renda < 15

resultado = classificador.predict([ [0, 0, 1, 2], [3, 0, 0, 0] ])
print(classificador.classes_)
print(classificador.class_count_)
print(classificador.class_prior_)




















