from director import Director
from pelicula import Pelicula

def main():
    
    id_director_max = 0
    id_pelicula_max = 0
    opcion_archivo = input("""En que directorio desea trabajar:
    directores (D)
    peliculas (P)\n""")

    print(opcion_archivo)

    if(opcion_archivo.lower() == 'd'):     
        print("director")
        operacion = escoger_operacion()
        print(operacion)
        if(operacion.lower() == 'c'):
            print("Crear")            

            id_director = id_director_max+1
            nombre_apellido_director = input("Ingrese el nombre y apellido\n")
            anio_nacimiento_director = input("Ingrese anio nacimiento\n")
            anio_debut_director = input("Ingrese anio debut\n")
            casado_director_str = input("director actualmente casado S/N\n")
            casado_bool = False
            if(casado_director_str.lower()=='s'):
                casado_bool = True
            elif(casado_director_str.lower()=='n'):
                casado_bool = False
            else:
                print("ingrese S para si o N para no\n")
            calificacion_pelicula_alta_IMDB_director = input("Ingrese pelicula mejor rankeada (IMDB)\n")
            #agregar pelicula del director
            pelicula_nueva = input("Ingresar nueva película(N) o tomar de la lista(L)\n")
            if(pelicula_nueva.lower()=='n'):
                print("nueva pelicula")
                #creacion director
                director = crear_director(id_director, nombre_apellido_director, anio_nacimiento_director,
                 anio_debut_director, casado_bool, calificacion_pelicula_alta_IMDB_director)
                #datos pelicula
                id_pelicula = id_director_max+1
                #id_director
                nombre_pelicula = input("Ingrese nombre de la pelicula\n")
                fecha_estreno = input("Ingrese año de estreno\n")
                genero = input("Ingrese el genero de la pelicula\n")
                secuela_str = input("La pelicula tiene una secuela S/N\n")
                secuela_bool = False
                if(secuela_str.lower() == 's'):
                    secuela_bool = True
                elif(secuela_str.lower() == 'n'):
                    secuela_bool = False
                else:
                    print("Ingrese S o N\n")
                calificacion_IMDB = input("Ingrese la calificacion de la pelicula(IMDB)\n")
                #creacion pelicula
                director.set_pelicula(id_pelicula, id_director, nombre_pelicula, fecha_estreno,
                genero, secuela_bool, calificacion_IMDB)
                #fin creacion director con creacion pelicula

            elif(pelicula_nueva.lower()=='l'):
                print("Lista")
                id_pelicula = input("escriba el numero de la pelicula")
                #creacion director
                director = crear_director(id_director, nombre_apellido_director, anio_nacimiento_director,
                 anio_debut_director, casado_bool, calificacion_pelicula_alta_IMDB_director)
                #creacion pelicula
                id_pelicula = id_pelicula_max+1
                #id_director
                nombre_pelicula = None    
                fecha_estreno = None
                genero = None
                secuela = None
                calificacion_IMDB = None
                director.set_pelicula(id_pelicula, id_director, nombre_pelicula, fecha_estreno,
                genero, secuela, calificacion_IMDB)
        
                print("director creado")
            # fin creacion de director con pelicula de lista
            else:
                print("Escoja N o L")

        elif(operacion.lower() == 'r'):
            print("read")
        
        elif(operacion.lower() == 'u'):
            print("update")
        
        elif(operacion.lower() == 'd'):
            print("Delete")
        else:
            print("Escoja una opcion C,R,U,D")

    elif(opcion_archivo.lower() == 'p'):
        print("pelicula")
        operacion = escoger_operacion()
        print(operacion)
        if(operacion.lower() == 'c'):
            print("Crear")
        elif(operacion.lower() == 'r'):
            print("read")
        elif(operacion.lower() == 'u'):
            print("update")
        elif(operacion.lower() == 'd'):
            print("Delete")
        else:
            print("Escoja una opcion C,R,U,D")
    else:
        print("escoja 'D' o 'P'")



def escoger_operacion():
        opcion_operacion = input(""""Operacion a realizar
    Crear(C)
    Leer(R)
    Actualizar(U)
    Borrar(D)\n""")
        return opcion_operacion
  
def crear_director(id_director, nombre_apellido, anio_nacimiento,
 anio_debut, casado, calificacion_pelicula_alta_IMDB_director):
    
    director = Director()
    
    director.set_id_director = director
    director.set_nombre_apellido = nombre_apellido
    director.set_anio_nacimiento = anio_nacimiento
    director.set_anio_debut = anio_debut
    director.set_casado = casado
    director.set_calificacion_pelicula_alta_IMDB = calificacion_pelicula_alta_IMDB_director
    
    return director

def crear_pelicula(id_pelicula, id_director, nombre_pelicula, fecha_estreno,
genero, secuela, calificacion_IMDB):
    pelicula = Pelicula()
    pelicula.set_id_pelicula = id_pelicula
    pelicula.set_id_director = id_director
    pelicula.set_nombre_pelicula = nombre_pelicula
    pelicula.set_fecha_estreno = fecha_estreno
    pelicula.set_genero = genero
    pelicula.set_secuela = secuela
    pelicula.set_calificacion_IMDB = calificacion_IMDB

    return pelicula


if __name__ == "__main__":
    main()
