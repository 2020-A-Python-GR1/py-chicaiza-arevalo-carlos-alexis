class Pelicula:
    __id_pelicula = None
    __id_director = None

    __nombre_pelicula = None    
    __fecha_estreno = None
    __genero = None
    __secuela = None
    ___calificacion_IMDB = None
    
    def __init__(self):
        print("contructor pelicula")

    def set_nombre_pelicula(self, nombre_pelicula):
        self.__nombre_pelicula = nombre_pelicula

    def set_fecha_estreno(self, fecha_estreno):
        self.__fecha_estreno = fecha_estreno

    def set_genero(self, genero):
        self.__genero = genero

    def set_secuela(self, secuela):
        self.__secuela = secuela

    def set_calificacion_IMDB(self, calificacion_IMDB):
        self.__calificacion_IMDB = calificacion_IMDB

    
