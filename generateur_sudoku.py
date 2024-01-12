import random
import time
import tkinter as tk
from tkinter import messagebox

tableau = [
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]]
]


def ligne_ok(tableau, nombre, ligne):
    for i in range(9):
        if tableau[ligne][i] == nombre:
            return 0
    return 1

def colone_ok(tableau, nombre, colone):
    for i in range(9):
        if tableau[i][colone] == nombre:
            return 0
    return 1

def carre_ok(tableau, nombre, ligne, colone):
    for i in range(9):
        for n in range(9):
            if ((ligne // 3) == (i // 3)) and ((colone // 3) == (n // 3)): #meme carré
                if tableau[i][n] == nombre:
                    return 0
    return 1

def next_case(tableau, ligne, colone):
    if ((colone + 1) < 9) and (ligne < 9):
        return ligne, colone + 1
    elif ((colone + 1) == 9) and ((ligne + 1) < 9):
        return ligne + 1, 0
    else:
        return -1, 0

def remplir(tableau, ligne, colone):
    #cas d'arret
    if ligne == -1:
        return 0 #génération terminé
    #cas général
    else:
        possible=[1,2,3,4,5,6,7,8,9]
        random.shuffle(possible) #rend le sudoku aléatoire
        indice=0
        while indice < 9:
            if (ligne_ok(tableau, possible[indice], ligne) == 1) and (colone_ok(tableau, possible[indice], colone) == 1) and (carre_ok(tableau, possible[indice], ligne, colone) == 1):
                tableau[ligne][colone] = possible[indice]
                i, n = next_case(tableau, ligne, colone)
                if (remplir(tableau, i, n)) == 0:
                    return 0
            else:
                indice+= 1
        if indice == 9:
            tableau[ligne][colone] = ''
            return -1

class SudokuDifficultyGUI:
    def __init__(self, master, tableau):
        self.master = master
        self.master.title("Choisir la Difficulté")

        self.tableau = tableau

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.master, text="Choisissez la difficulté :")
        label.pack(pady=10)

        buttons_frame = tk.Frame(self.master)
        buttons_frame.pack()

        facile_button = tk.Button(buttons_frame, text="Facile", command=lambda: self.enleve_case(0))
        facile_button.grid(row=0, column=0, padx=10)

        moyenne_button = tk.Button(buttons_frame, text="Moyenne", command=lambda: self.enleve_case(1))
        moyenne_button.grid(row=0, column=1, padx=10)

        difficile_button = tk.Button(buttons_frame, text="Difficile", command=lambda: self.enleve_case(2))
        difficile_button.grid(row=0, column=2, padx=10)

    def enleve_case(self, difficulty):
        if difficulty == 0:
            self.facile()
        elif difficulty == 1:
            self.moyenne()
        else:
            self.difficile()

    def facile(self):
        for i in range(9):
            for n in range(9):
                nb = random.randint(1, 9)
                if nb <= 3:
                    self.tableau[i][n] = ' '

        self.master.destroy()  # Ferme la fenêtre après la sélection de la difficulté

    def moyenne(self):
        for i in range(9):
            for n in range(9):
                nb = random.randint(1, 9)
                if nb <= 5:
                    self.tableau[i][n] = ' '

        self.master.destroy()  # Ferme la fenêtre après la sélection de la difficulté

    def difficile(self):
        for i in range(9):
            for n in range(9):
                nb = random.randint(1, 9)
                if nb <= 7:
                    self.tableau[i][n] = ' '

        self.master.destroy()  # Ferme la fenêtre après la sélection de la difficulté

def choisir_diff(tableau):
    root = tk.Tk()
    app = SudokuDifficultyGUI(root, tableau)
    root.mainloop()

class SudokuGUI:
    def __init__(self, master, sudoku_grid):
        self.master = master
        self.master.title("Sudoku Solver")

        self.sudoku_grid = sudoku_grid
        self.create_grid()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                cell_value = self.sudoku_grid[i][j]
                cell_label = tk.Label(self.master, text=str(cell_value), width=4, height=2, relief="solid", font=("Helvetica", 16, "bold"))
                cell_label.grid(row=i, column=j)

if __name__ == '__main__':
    temps_debut = time.time()
    remplir(tableau, 0, 0)
    temps_fin = time.time()
    temps = temps_fin - temps_debut #chronometre le temps de génération
    #print(temps)
    for i in range(9):
        print(tableau[i])
    choisir_diff(tableau)
    root = tk.Tk()
    app = SudokuGUI(root, tableau)
    root.mainloop()
