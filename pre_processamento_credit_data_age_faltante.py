# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:58:36 2018

@author: Administrator
"""

import pandas 

base = pandas.read_csv('E:\\Udemy - Cursos\\MachineLearning\\Arquivos\\CreditData.csv')

base.describe()

# Preencher os valores com a média

base.mean()
base['age'].mean() # Esta média está errada, esta sendo considerado os valores negativos da idade.
base['age'][base.age > 0].mean() # Aqui está descartando as idade negativas
base.loc[base.age < 0, 'age'] = 40.92770044906149
base.loc[base['age'] < 0 ]

# VERIFICAR SE HÁ REGISTRO INCONSISTENTE (VALOR INVÁLIDO OU FALTANTE)

pandas.isnull(base['age']) # Mostra em todo o registro

base.loc[pandas.isnull(base['age'])]  # Mostra diretamente as linhas

# Fazendo a divisão entre previsores e classe

previsores = base.iloc[:, 1:4].values # 4 é EXCLUSIVO(não conta)

classse = base.iloc[:, 4].values # (4) Ao especificar somente a coluna

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN', strategy='mean', axis = 0)

imputer = imputer.fit(previsores[:, 0:3])

previsores[:, 0:3] = imputer.transform(previsores[:, 0:3])