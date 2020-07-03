
def main():

    
    opcion_archivo = input("""En que directorio desea trabajar:
    directores (D)
    peliculas (P)\n""")

    print(opcion_archivo)

    if(opcion_archivo.lower() == "d"):     
        print("director")
        operacion = escoger_operacion()
        print(operacion)

    elif(opcion_archivo.lower() == 'p'):
        print("pelicula")
        operacion = escoger_operacion()
        print(operacion)

    else:
        print("escoja 'D' o 'P'")



def escoger_operacion():
        opcion_operacion = input(""""Operacion a realizar
    Crear(C)
    Leer(R)
    Actualizar(U)
    Borrar(D)\n""")
        return opcion_operacion

if __name__ == "__main__":
    main()
