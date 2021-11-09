import re
#wiliam santiago sierra guemez
opcion = 0

while opcion!=6:
    print("Lista de opciones")
    print("1.-Buscar Variables validas")
    print("2.-Buscar Enteros y decimales")
    print("3.-Expresiones aritmeticas")
    print("4.-Operaciones condicionales")
    print("5.-Cadenas de caracteres")
    opcion = int(input("Ingresa una opción\n"))

    if opcion ==1:
        #busca variables validas
        filename = 'index.txt'
        textfile = open(filename,"r")
        regex = '[a-zA-Z_][a-zA-Z_0-9]*'
        reg = re.compile(regex)

        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif opcion ==2:
        #busca bumeros enteros o decimales
        filename = 'index.txt'
        textfile = open(filename, "r")
        regex = '\d+\.?\d*'
        reg = re.compile(regex)

        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif opcion ==3:
        #Busca expresiones aritmeticas
        filename = 'index.txt'
        textfile = open(filename, "r")
        regex = '\d+.?\d*[+|\-|=|*|\/|%]\d+?\d*'
        reg = re.compile(regex)

        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif opcion ==4:
        #busca expresiones condicional
        filename = 'index.txt'
        textfile = open(filename, "r")
        regex = '(([A-za-z]\w*|\d\.?\d*)\s?(\>|\<|\>=|\<=|=|!=|\=\=)\s?([A-za-z]\w*|\d\.?\d*))'
        reg = re.compile(regex)

        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()

    elif opcion ==5:
        #busca lista de caracteres
        filename = 'index.txt'
        textfile = open(filename, "r")
        regex = "((\".*?\")|(\'.*?\'))"
        reg = re.compile(regex)

        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    else:
        print("\nNo es una opcion valida")
