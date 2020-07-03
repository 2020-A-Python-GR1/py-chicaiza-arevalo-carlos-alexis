from pelicula import Pelicula
class Director:
    __id_director = None

    __nombre_apellido = None    
    __anio_nacimiento = None
    __anio_debut = None
    __casado = None
    ___calificacion_pelicula_alta_IMDB = None
    
    peliculas = []
    
    def __init__(self):
        print("contructor director")

    def set_nombre_apellido(self, nombre_apellido):
        self.__nombre_apellido = nombre_apellido

    def set_anio_nacimiento(self, anio_nacimiento):
        self.__anio_nacimiento = anio_nacimiento

    def set_anio_debut(self, anio_debut):
        self.__anio_debut = anio_debut

    def set_casado(self, casado):
        self.__casado = casado

    def set_calificacion_pelicula_alta_IMDB(self, calificacion_alta_IMDB):
        self.__calificacion_alta_IMDB = calificacion_alta_IMDB

    def get_nombre_apellido(self):
        return self.__nombre_apellido

    def get_nombre_apellido(self):
        return self.__nombre_apellido
    
    def get_nombre_apellido(self):
        return self.__nombre_apellido

    def get_nombre_apellido(self):
        return self.__nombre_apellido

    def get_nombre_apellido(self):
        return self.__nombre_apellido

    #def set_pelicula(self, id_pelicula, id_director, nombre_pelicula,
     #                fecha_estreno, genero, secuela, calificacion_IMDB):


    def set_pelicula(self,nombre_pelicula):
        pelicula = Pelicula()
        pelicula.set_nombre_pelicula(nombre_pelicula)
        self.peliculas.append(pelicula)
    
    

def main():
    director = Director()
    director.set_pelicula("Mad max")
    print(director.peliculas[0])
if __name__ == "__main__":
    main()
