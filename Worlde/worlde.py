import random

class wordle:
    def __init__(self, archivo):
        self.archivo = archivo
        self.palabra_correcta = ''

    def get_archivo(self):
        return self.archivo

    def set_archivo(self, archivo):
        self.archivo = archivo

    def transformar_archivo(self, cant_letras):
        archivo = open(self.archivo, "r", encoding="utf-8")
        nombre_archivo = "EspañolXLetras.txt"
        espaniolxletras = open(nombre_archivo, "w", encoding="utf-8")
        for linea in archivo:
            linea = linea.split()
            linea = linea[1]
            if len(linea) == cant_letras:
                linea = linea.replace("á", "a")
                linea = linea.replace("é", "e")
                linea = linea.replace("í", "i")
                linea = linea.replace("ó", "o")
                linea = linea.replace("ú", "u")
                espaniolxletras.write(linea + '\n')
        espaniolxletras.close()
        archivo.close()
        return nombre_archivo

    def palabra_random(self, archivo):
        archivo = open(archivo, "r", encoding="utf-8")
        lista_palabras = []
        for linea in archivo:
            linea = linea.strip()
            lista_palabras.append(linea)
        numero = random.randint(1, len(lista_palabras)) - 1
        palabracorrecta = lista_palabras[numero]
        self.palabra_correcta = palabracorrecta.upper()
        archivo.close()

    def HacerGrid(self, cant_intentos, cant_letras):
        grid = []
        for x in range(cant_intentos):
            grid.append([])
        for y in range(cant_intentos):
            for z in range(cant_letras):
                grid[y].append('\033[47m   \033[0m ')
        return grid

    def PrintGrid(self, grid):
        print(' ' * 2, '\033[45m W O R D L E \033[0m', '\n')
        for lista in grid:
            linea = ''
            for casilla in lista:
                linea += casilla
            print(linea + '\n')

    def Jugar(self, grid, cant_intentos, cant_letras):
        contador = 0
        PalabraJugador = ''
        PalabraRandom = self.palabra_correcta.upper()
        print('\n' * 37)
        while contador < cant_intentos and PalabraJugador.upper() != PalabraRandom:
            self.PrintGrid(grid)
            PalabraJugador = input(' ' * 7).upper()
            print()
            if len(PalabraJugador) == cant_letras:
                for letra in range(cant_letras):
                    LetraJugador = PalabraJugador[letra]
                    LetraPalabra = PalabraRandom[letra]
                    if LetraJugador not in PalabraRandom:
                        grid[contador][letra] = ('\033[100m {} \033[0m '.format(LetraJugador))
                    elif LetraJugador == LetraPalabra:
                        grid[contador][letra] = ('\033[42m {} \033[0m '.format(LetraJugador))
                    elif LetraJugador in PalabraRandom:
                        grid[contador][letra] = ('\033[43m {} \033[0m '.format(LetraJugador))
                contador += 1
                print('\n' * 37)
            else:
                print('\n' * 37)
                print('\033[41m ¡ P A L A B R A   I N V Á L I D A ! \033[0m')
                print()
        print('\n' * 37)
        self.PrintGrid(grid)
        if PalabraJugador == PalabraRandom:
            print('\033[42m ¡ G A N A S T E ! \033[0m', '\n')
        else:
            print('\033[41m ¡ P E R D I S T E ! \033[0m', '\n')
        print(f'La palabra era: {PalabraRandom}')


wordle = wordle("2000 palabras.txt")
wordle.palabra_random(wordle.transformar_archivo(5))
grid = wordle.HacerGrid(6, 5)
wordle.Jugar(grid, 6, 5)
