# -*- coding:latin-1 -*-
import time
import getpass, sys
import pyAesCrypt
from os import stat, remove

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

escolha = input('digite: \n1- Encript \n2- Decript\nR: ')


password = getpass.getpass('\nDigite a Senha:')

if escolha == '1':
 # encrypt
 with open("Nome do Arquivo aqui", "rb") as fIn:
  with open("Nome do arquivo aqui.aes", "wb") as fOut:
   pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

 x = input ('você quer deletar o arquivo txt? y ')

 if x != 'y':
  print ('\nok')
  time.sleep(1)
  sys.exit()
  
 remove("Nome do arquivo aqui.txt")
 print ('Arquivo removido')
 time.sleep(2)
 sys.exit()

if escolha == '2':
 # get encrypted file size
 encFileSize = stat("Nome do arquivo aqui.aes").st_size

 # decrypt
 with open("Nome do arquivo aqui.aes", "rb") as fIn:
  try:
   with open("Nome do arquivo aqui.txt", "wb") as fOut:
    # decrypt file stream
    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
  except ValueError:
   print ('senha incorreta')
   # remove output file on error
   remove("Nome do arquivo aqui.txt")

 time.sleep(3)
 sys.exit()

print ('\n\nEscolha errada')
time.sleep(2)
