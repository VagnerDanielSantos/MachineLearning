
import Orange

base = Orange.data.Table('E:\\Udemy - Cursos\\MachineLearning\\Arquivos\\RiscoCredito.csv')
base.domain

cn2_learner = Orange.classification.rules.CN2Learner()  # Algorítmo para Indução de Regra

classificador = cn2_learner(base)

for regras in classificador.rule_list:
    print(regras)
    
# Histórico boa, divida alta, garantia nenhuma, renda > 35
resultado = classificador( [ ['boa', 'alta', 'nenhuma', 'acima_35'], ['ruim', 'alta', 'adequada', '0_15'] ])

for prev in resultado:
    print(base.domain.class_var.values[prev])
    
