#lista de animais
animais = ["Tucano", "Ornitorrinco", "Papagaio", "Leão"]



#primeira diferença - a lista mantém a ordem
print (*animais)
#Inserindo um item a lista
animais.append ("Cavalo")
print(*animais)
#inserindo outro tucano
animais.append("Tucano")
print(*animais)
#remover papagaio
animais.remove("Papagaio")
print(*animais)