    
import Orange

base = Orange.data.Table('E:\\Udemy - Cursos\\MachineLearning\\Arquivos\\CreditData.csv')
base.domain

base_dividida = Orange.evaluation.testing.sample(base, n=0.25)
base_teste = base_dividida[0]
base_treinamento = base_dividida[1]

len(base_teste)
len(base_treinamento)

cn2_learner = Orange.classification.rules.CN2Learner()
classificador = cn2_learner(base_treinamento)  # Neste momento é gerado as regras

for regras in classificador.rule_list:
    print(regras)
    
resultado = Orange.evaluation.TestOnTestData(base_teste, base_treinamento, [classificador])
print(Orange.evaluation.CA(resultado))

