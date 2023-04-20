from conversorArmazenamento import conversor, stringParaFloat, listaUnidades
valorInicial = input("Insira o valor a ser convertido: ")
unidade1 = input(f"Insira a unidade inicial {listaUnidades}: ")

while not unidade1 in listaUnidades:
    unidade1 = input(f"Insira a unidade inicial {listaUnidades}: ")

unidade2 = input(f"Insira a unidade final {listaUnidades}: ")

while not unidade2 in listaUnidades:
    unidade2 = input(f"Insira a unidade final {listaUnidades}: ")

valorFinal = conversor(int(valorInicial), unidade1, unidade2)