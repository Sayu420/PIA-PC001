import argparse
import sys
import getpass


def encriptar(msj, key):
    """Esta función recibe 2 parámetros para cifrar mensajes:
        [msj] = Mensaje a cifrar
        [key] = Llave de cifrado"""
    if msj != "":
        if key != "":
            try:
                message = msj
                espacios = 1           
                while espacios > 0:
                    clave = key
                    espacios = clave.count(' ')
                    if clave.isalpha() is False:
                        espacios += 1
                key = len(clave)
                SYMBOLS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 !?ÁáÉéÍíÓóÚúÜü.'

                translated = ''

                for symbol in message:
                    if symbol in SYMBOLS:
                        symbolIndex = SYMBOLS.find(symbol)
                        translatedIndex = symbolIndex + key

                        if translatedIndex >= len(SYMBOLS):
                            translatedIndex = translatedIndex - len(SYMBOLS)
                        elif translatedIndex < 0:
                            translatedIndex = translatedIndex + len(SYMBOLS)

                        translated = translated + SYMBOLS[translatedIndex]
                    else:
                        translated = translated + symbol
                print("\nMensaje encriptado: ")
                print(translated)
            except:
                print("\nDebe especificar una clave y/o mensaje para encriptar.")
        else:
            print("Debe especificar una llave valida!")
    else:
       print("Debe especificar un mensaje valido!")


def desencriptar(msj, key):
    """Esta funcion recibe 2 parametros para descifrar mensajes:
        [msj] = Mensaje a descifrar
        [key] = Llave de cifrado"""
    if msj != "":
        if key != "":
            try:
                message = msj
                espacios = 1
                while espacios > 0:
                    clave = key
                    espacios = clave.count(' ')
                    if clave.isalpha() is False:
                        espacios += 1
                key = len(clave)

                SYMBOLS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 !?ÁáÉéÍíÓóÚúÜü.'

                translated = ''

                for symbol in message:
                    if symbol in SYMBOLS:
                        symbolIndex = SYMBOLS.find(symbol)
                        translatedIndex = symbolIndex - key

                        if translatedIndex >= len(SYMBOLS):
                            translatedIndex = translatedIndex - len(SYMBOLS)
                        elif translatedIndex < 0:
                            translatedIndex = translatedIndex + len(SYMBOLS)

                        translated = translated + SYMBOLS[translatedIndex]
                    else:
                        translated = translated + symbol

                print("\nMensaje desencriptado: ")
                print(translated)

            except:
                print("\nDebe especificar una clave y/o mensaje para desencriptar.")
        else:
            print("Debe especificar una llave valida!")
    else:
       print("Debe especificar un mensaje valido!")


def hackear(msj):
    """Esta función recibe 1 parámetro para intentar hackear el mensaje:
        [msj] = Mensaje a hackear"""
    if msj != "":
        try:
            message = msj
            SYMBOLS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 !?ÁáÉéÍíÓóÚúÜü.'

            for key in range(len(SYMBOLS)):
                translated = ''

                for symbol in message:
                    if symbol in SYMBOLS:
                        symbolIndex = SYMBOLS.find(symbol)
                        translatedIndex = symbolIndex - key

                        if translatedIndex < 0:
                            translatedIndex = translatedIndex + len(SYMBOLS)

                        translated = translated + SYMBOLS[translatedIndex]

                    else:
                        translated = translated + symbol
                print('Key #%s: %s' % (key, translated))
        except:
            print("\nNo se pudo realizar el hackeo.")
    else:
        print("Debe especificar un mensaje a descifrar.")
