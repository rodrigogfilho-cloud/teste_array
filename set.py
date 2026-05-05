#conjunto aff

animais = {"Tucano", "Ornitorrinco", "Papagaio", "Leão"}


#orimeira diferença - o conjunto(set) não mantém a ordem
print(*animais)
# add item
animais.add("Morcego")
print(*animais)
#tentar inserir outro cucano / Os itens dos conjuntos não podem ser duplicados
animais.add("Tucano")
print(*animais)
#remover Leão
animais.remove("Leão")
print(*animais)