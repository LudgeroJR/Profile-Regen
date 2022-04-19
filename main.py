# Importações
from contextlib import suppress
from winreg import \
    (OpenKey,
     HKEY_LOCAL_MACHINE,
     QueryInfoKey,
     QueryValueEx,
     EnumKey)
from tkinter import *


# Obter Profiles existentes.

PROFILE_REGISTRY = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList"

def get_profile_attribute():
    profile_to_sub_key_map = {}
    listaProfile = []
    with OpenKey(HKEY_LOCAL_MACHINE, PROFILE_REGISTRY) as key:
        # QueryInfoKey retorna informações sobre a chave.
        # A primeira informação (index: 0) é referente a quantidade de subchaves contida na chave
        number_of_sub_keys, _, _ = QueryInfoKey(key)

        for index in range(number_of_sub_keys):
            sub_key_name = EnumKey(key, index)
            # Abra as subchaves uma a uma e busca o atributo.
            with OpenKey(HKEY_LOCAL_MACHINE,
                         f"{PROFILE_REGISTRY}\\{sub_key_name}") as sub_key:
                with suppress(FileNotFoundError):
                    registry_value, _ = QueryValueEx(sub_key, 'ProfileImagePath')
                    profile_to_sub_key_map.update({sub_key_name: registry_value})
                    if "C:\\Users" or "D:\\Usuarios" in registry_value:
                        listaProfile.append(registry_value)

    return listaProfile

print(get_profile_attribute())


 #   return profile_to_sub_key_map



# print(get_profile_attribute())



# Obter as informações do profile escolhido
# Renomear pasta do profile escolhido
# Apagar registro do profile escolhido

#Criar tela

janela = Tk()
janela.title("Regerar Profile")
janela.geometry('400x200')



janela.mainloop()

