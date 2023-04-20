valorPadrão = 1024
listaUnidades = ["bit","byte","kilobyte","megabyte","gigabyte","terabyte","petabyte"]

def conversor(valorInicial,unidade1,unidade2):
    print(f'Conversão executada ({unidade1} PARA {unidade2})')
    valorFinal = valorInicial
    if(unidade1 == "bit"):
        valorFinal = valorFinal / 8
        unidade1 = "byte"
    if(listaUnidades.index(unidade1) < listaUnidades.index(unidade2)):
        for i in range(listaUnidades.index(unidade1), listaUnidades.index(unidade2)):
            valorFinal = valorFinal / valorPadrão
    else:
        for i in range(listaUnidades.index(unidade1), listaUnidades.index(unidade2),-1):
            valorFinal = valorFinal * valorPadrão
        if(unidade2 == "bit"):
            valorFinal = (valorFinal / valorPadrão) * 8
    return print(valorFinal)