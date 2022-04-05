import os
import csv
from csv import reader
from csv import DictReader

with open('UserAd.csv', 'r') as obj:
   csv_reader = DictReader(obj)
   for row in csv_reader:
      #print(row['Login'], row['NomeCompleto'])
      Login = row['Login']
      NomeCompleto = row['NomeCompleto']
      Senha = row['Senha']
      OU = row['OU']
      Nome = row['Nome']
      Sobrenome = row['Sobrenome']
      Email = row['Email']

      comando = "samba-tool user create " + Login + " " + Senha + " --userou=" + OU +  " --given-name=" + '"'+ 
      NomeCompleto + '"' + " --surname=" + Sobrenome + " --mail-address=" + Email + " --must-change-at-next-login"

      #print(comando)
      os.system(comando)

