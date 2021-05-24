import argparse
from argparse import RawTextHelpFormatter
import subprocess
import os
import getpass
import msvcrt
import time
import LWN_nmap
import LWN_VTWeb
import LWN_Cifrado
import LWN_Email


def runPS(cmd):
    """Esta función recibe 1 parámetro para ejecutar comandos de PowerShell desde Python:
        [cmd] = Comando de PowerShell a ejecutar"""
    completed = subprocess.run(["powershell", "-Command", cmd])

    
def hash(path):
    """Esta función recibe 1 parámetro que será la ruta de los archivos a los cuales se les desea generar un hash:
        [path] = Ruta de la carpeta que contiene los archivos"""
    try:
        if path != "":
            dest = path + "\*.*"
            cwd = os.getcwd()
            ps = "& \"" +cwd+ "\LWN-Hash.ps1\" -path " + "\"" + dest + "\""
            runPS(ps)
            print("\nEl archivo se ha guardado en: " + cwd + "\hash\Hash-FileNames.txt")
        else:
            print("Debe especificar una ruta valida.")
    except:
        print("No fue posible realizar el hasheo.")


def menu():
    """Esta función no recibe parámetros y despliega un menú de acciones si es que el script se ejecutó sin ningún parámetro"""
    loop = True
    while loop == True:
        os.system('cls')
        print("Que desea hacer?\n")
        print("1.- Escanear una dirección web")
        print("2.- Escanear una ip")
        print("3.- Obtener valores hash")
        print("4.- Enviar email")
        print("5.- Encriptar un mensaje")
        print("6.- Desencriptar un mensaje")
        print("7.- Hackear un mensaje")
        print("8.- Salir")
        op = getpass.getpass("")
        os.system('cls')
        
        if op == '1':
            url = input("Ingrese la dirección web a analizar (Ej. http://www.google.com): ")
            LWN_VTWeb.analizar(url)
            print("\nOperación finalizada!\n")
            print("Presione una tecla para continuar.")
            time.sleep(1)
            msvcrt.getch()
            
        elif op == '2':
            ip = input("Ingrese la dirección ip a analizar (Ej. 192.168.1.100/24): ")
            LWN_nmap.portScan(ip)
            print("\nOperación finalizada!\n")
            print("Presione una tecla para continuar.")
            time.sleep(1)
            msvcrt.getch()
            
        elif op == '3':
            path = input("Ingrese la ruta de los archivos a hashear: ")
            hash(path)
            print("\nOperación finalizada!\n")
            print("Presione una tecla para continuar.")
            time.sleep(1)
            msvcrt.getch()
            
        elif op == '4':
            dest = input("Ingrese la diercción del destinatario: ")
            sub = input("Ingrese el asunto del mensaje: ")
            msj = input("Ingrese el mensaje a enviar: ")
            LWN_Email.email(dest, sub, msj)
            print("\nOperación finalizada!\n")
            print("Presione una tecla para continuar.")
            time.sleep(1)
            msvcrt.getch()
            
        elif op == '5':
            msj = input("Ingrese el mensaje a encriptar: ")
            key = input("Ingrese la clave de encriptado: ")
            LWN_Cifrado.encriptar(msj, key)
            print("\nOperación finalizada!\n")
            print("Presione una tecla para continuar.")
            time.sleep(1)
            msvcrt.getch()
            
        elif op == '6':
            msj = input("Ingrese el mensaje a desencriptar: ")
            key = input("Ingrese la clave de desencriptado: ")
            LWN_Cifrado.desencriptar(msj, key)
            print("\nOperación finalizada!\n")
            print("Presione una tecla para continuar.")
            time.sleep(1)
            msvcrt.getch()
            
        elif op == '7':
            msj = input("Ingrese el mensaje a hackear: ")
            LWN_Cifrado.hackear(msj)
            print("\nOperación finalizada!\n")
            print("Presione una tecla para continuar.")
            time.sleep(1)
            msvcrt.getch()
            
        elif op == '8':
            loop = False
            os.system('cls')
            
        else:
            os.system('cls')
            print("Opción no valida.\n")
            print("Presione una tecla para continuar.")
            time.sleep(1)
            msvcrt.getch()

parser = argparse.ArgumentParser(description='Aquí podrá ver una breve guía de como ejecutar el script.',  
                                epilog="Si tiene dudas, favor de revisar la documentación.",formatter_class=RawTextHelpFormatter)

parser.add_argument('-mode', type=str, required=False,
                    help="""Argumento que define como se utilizara el script.
H = Obtendrá valores hash de un directorio.
S = Escaneara las ip de una dirección dada para obtener información de las mismas.
V = Escaneara una dirección web para saber si es segura.
E = Encriptara un mensaje dado.
D = Desencriptara un mensaje dado.
hack = Intentara descifrar un mensaje sin llave.
email = Enviara un correo electrónico dado un mensaje, asunto y dirección válidos.""")
parser.add_argument('-path', type=str, required=False,
                    help='Directorio del cual se obtendrá los valores hash de su contenido.')
parser.add_argument('-ip', type=str, required=False,
                    help='Dirección ip a escanear. Ej. 192.168.1.100/24')
parser.add_argument('-web', type=str, required=False,
                    help='Posible dirección web comprometida a escanear.')
parser.add_argument('-key', type=str, required=False,
                    help='Palabra clave para encriptar o desencriptar.')
parser.add_argument('-msj', type=str, required=False,
                    help='Mensaje que puede ser usado para encriptar, desencriptar o enviar correos.')
parser.add_argument('-dest', type=str, required=False,
                    help='Destinatario del correo a enviar')
parser.add_argument('-sub', type=str, required=False,
                    help='Asunto del mensaje')

args = parser.parse_args()

if __name__ == "__main__":
    if args.mode == 'H' or args.mode == 'h':
        hash(args.path)

    elif args.mode == 'S' or args.mode == 's':
        LWN_nmap.portScan(args.ip)
        
    elif args.mode == 'V' or args.mode == 'v':
        LWN_VTWeb.analizar(args.web)
        
    elif args.mode == 'E' or args.mode == 'e':
        LWN_Cifrado.encriptar(args.msj, args.key)
        
    elif args.mode == 'D' or args.mode == 'd':
        LWN_Cifrado.desencriptar(args.msj, args.key)
        
    elif args.mode == 'hack':
        LWN_Cifrado.hackear(args.msj)
        
    elif args.mode == 'email':
        LWN_Email.email(args.dest, args.sub, args.msj)
        
    else:
        os.system('cls')
        print("Como no se especificó un modo valido de ejecución, se desplegará un menú de opciones.")
        print("Presione una tecla para continuar.")
        msvcrt.getch()
        menu()
