import nmap
import sys
import os


def portScan(target):
    """Esta función recibe 1 parámetro para escanear ip's y detectar puertos abiertos:
        [target] = Dirección ip a escanear
        """
    if target != "":
        try:
            cwd = os.getcwd()
            scanner = nmap.PortScanner()
            scanner.scan(target)
            for host in scanner.all_hosts():
                print('###############################\n')
                print('Host: %s' % (host)+'  Estado: %s' % scanner[host].state())
                for protocol in scanner[host].all_protocols():
                    print('Protocolo: %s' % protocol)
                    ports = sorted(scanner[host][protocol].keys())
                    for port in ports:
                        print('Puerto: %s' % port+'  Estado: %s' %
                              scanner[host][protocol][port]['state'])
                print()
            print('###############################')

            with open('Escaneo.csv', 'w') as output:
                output.write(scanner.csv())
            print ("Se ha guardado la información del análisis en: " + cwd +
                   "\\Escaneo.csv")
        except:
            print("No fue posible escanear la red.")
    else:
        print("Debe especificar una dirección valida.")

