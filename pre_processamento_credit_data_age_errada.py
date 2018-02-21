# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:05:45 2018

@author: Administrator
"""

import pandas 

base = pandas.read_csv('E:\\Udemy - Cursos\\MachineLearning\\Arquivos\\CreditData.csv')

base.describe()

base.loc[base['age'] < 0 ]

# Como apagar a coluna ( Não recomendado )

base.drop('age', 1, inplace = True)
base.loc[base['age'] < 0 ]

# Apagar somente os registros com problema ( Ter absoluta certeza de que os registros apagados não são de extrema importância)
base = pandas.read_csv('E:\\Udemy - Cursos\\MachineLearning\\Arquivos\\CreditData.csv')

base.drop(base[base.age < 0].index, inplace = True )
base.loc[base['age'] < 0 ]

# Preencher os valores manualmente ( Quando for possível e viável )
base = pandas.read_csv('E:\\Udemy - Cursos\\MachineLearning\\Arquivos\\CreditData.csv')

# Preencher os valores com a média

base.mean()
base['age'].mean() # Esta média está errada, esta sendo considerado os valores negativos da idade.
base['age'][base.age > 0].mean() # Aqui está descartando as idade negativas
base.loc[base.age < 0, 'age'] = 40.92770044906149
base.loc[base['age'] < 0 ]














