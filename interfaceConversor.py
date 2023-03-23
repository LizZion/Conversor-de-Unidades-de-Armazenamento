from conversorArmazenamento import stringParaFloat,bitParaByte,byteParaBit,ByteParaKByte,KByteParaByte,KByteParaMB,MBParaKByte,MBParaGB,GBParaMB,GBParaTB,TBParaGB,TBParaPB,PBParaTB

print('Insira qual conversão deseja realizar:\nBIT PARA BYTE (1)\nBYTE PARA BIT (2)\nBYTE PARA KB (3)\nKB PARA BYTE (4)\nKB PARA MB (5)\nMB PARA KB (6)\nMB PARA GB (7)\nGB PARA MB (8)\nGB PARA TB (9)\nTB PARA GB (10)\nTB PARA PB (11)\nPB PARA TB (12)')
escolha = int(input())
print('Por favor, insira o valor a ser convertido: ')
valorInput  = stringParaFloat(input())

if(escolha == 1):
    bitParaByte(valorInput)
elif(escolha == 2):
    byteParaBit(valorInput)
elif(escolha == 3):
    ByteParaKByte(valorInput)
elif(escolha == 4):
    KByteParaByte(valorInput)
elif(escolha == 5):
    KByteParaMB(valorInput)
elif(escolha == 6):
    MBParaKByte(valorInput)
elif(escolha == 7):
    MBParaGB(valorInput)
elif(escolha == 8):
    GBParaMB(valorInput)
elif(escolha == 9):
    GBParaTB(valorInput)
elif(escolha == 10):
    TBParaGB(valorInput)
elif(escolha == 11):
    TBParaPB(valorInput)
elif(escolha == 12):
    PBParaTB(valorInput)
else:
    print("Escolha um número válido de 1 a 12!")