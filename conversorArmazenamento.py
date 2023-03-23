# VARIÁVEIS/CONSTANTES

valorPadrão = 1024

# String para Float

def stringParaFloat(value):
    print('TRANSFORMANDO STRING EM FLOAT... CONCLUÍDO!')
    return float(value)

# Byte para Bit / Bit para Byte

def bitParaByte(valorInicial):
    print('Conversão executada (BIT PARA BYTE)')
    valorFinalByte = valorInicial / 8
    return print(valorFinalByte)

def byteParaBit(valorInicial):
    print('Conversão executada (BYTE PARA BIT)')
    valorFinalBit = valorInicial * 8
    return print(valorFinalBit)

# Byte para KByte / KByte para Byte

def ByteParaKByte(valorInicial):
    print('Conversão executada (BYTE PARA KBYTE)')
    valorFinalKByte = valorInicial / valorPadrão
    return print(valorFinalKByte)

def KByteParaByte(valorInicial):
    print('Conversão executada (KBYTE PARA BYTE)')
    valorFinalByte = valorInicial * valorPadrão
    return print(valorFinalByte)

# KB para MB / MB para KB

def KByteParaMB(valorInicial):
    print('Conversão executada (KB PARA MB)')
    valorFinalMB = valorInicial / valorPadrão
    return print(valorFinalMB)

def MBParaKByte(valorInicial):
    print('Conversão executada (MB PARA KB)')
    valorFinalKByte = valorInicial * valorPadrão
    return print(valorFinalKByte)

# MB para GB / GB para MB

def MBParaGB(valorInicial):
    print('Conversão executada (MB PARA GB)')
    valorFinalGB = valorInicial / valorPadrão
    return print(valorFinalGB)

def GBParaMB(valorInicial):
    print('Conversão executada (GB PARA MB)')
    valorFinalMB = valorInicial * valorPadrão
    return print(valorFinalMB)

# GB para TB / TB para GB

def GBParaTB(valorInicial):
    print('Conversão executada (GB PARA TB)')
    valorFinalTB = valorInicial / valorPadrão
    return print(valorFinalTB)

def TBParaGB(valorInicial):
    print('Conversão executada (TB PARA GB)')
    valorFinalGB = valorInicial * valorPadrão
    return print(valorFinalGB)

# TB para PB / PB para TB

def TBParaPB(valorInicial):
    print('Conversão executada (TB PARA PB)')
    valorFinalPB = valorInicial / valorPadrão
    return print(valorFinalPB)

def PBParaTB(valorInicial):
    print('Conversão executada (PB PARA TB)')
    valorFinalTB = valorInicial * valorPadrão
    return print(valorFinalTB)