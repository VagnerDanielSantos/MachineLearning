
import Orange 

base = Orange.data.Table('E:\\Udemy - Cursos\\MachineLearning\\Arquivos\\CreditData.csv')
base.domain

base_dividida = Orange.evaluation.testing.sample(base, n=0.25)
base_teste = base_dividida[0]
base_treinamento = base_dividida[1]

len(base_teste)
len(base_treinamento)

classificador = Orange.classification.MajorityLearner()
resultado = Orange.evaluation.TestOnTestData(base_teste, base_treinamento, [classificador])
print(Orange.evaluation.CA(resultado))

from collections import Counter
print(Counter(str(d.get_class()) for d in base_teste))



