def main():
    #try:
    #    configuration = open('config.txt')
    #except FileNotFoundError:
    #    print("No se puedo encontrar el archivo config.txt")
    #except PermissionError: 
    #    print("Se encontró config.txt pero es un directorio y no es posible leerlo")
    try:
        configuration = open('config.txt')
    except OSError as err:
        if err.errno == 2:
            print("No se puedo encontrar el archivo config.txt")
        elif err.errno == 13:
            print("Se encontró config.txt pero es un directorio y no es posible leerlo")



if __name__ == '__main__':
    main()