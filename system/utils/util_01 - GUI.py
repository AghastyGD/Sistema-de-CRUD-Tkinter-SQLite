from cgitb import text
import os
from tkinter import *
from turtle import width
import numpy as np
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

pastaApp1=os.path.dirname(__file__)




def Calculo_de_Media():
    global n1, n2, n3
    media = ttk.Window(themename="superhero")
    media.geometry("500x300")

    # Definindo o tipo de dados
    n1 = IntVar()
    n2 = IntVar()
    n3 = IntVar()

    #Calcule média de duas notas
    boasvinda = Label (media, text="CALCULE A SUA MÉDIA").pack(side=TOP)
    n1 = Label (media, text='DIGITE A PRIMEIRA NOTA ').pack(pady=2)
    n1 = Entry (media, texvariable=n1, width=10).pack(pady=2)
    n2 = Label (media, text = 'SEGUNDA NOTA').pack(pady=2)
    n2 = Entry (media, textvariable=n2, width=10).pack()
    n3 = Label (media, text= 'TERCEIRA NOTA ').pack(pady=2)
    n3 = Entry (media, textvariable=n3, width=10).pack(pady=4)
    logica = "Casa"
    botao_calc = ttk.Button (media, bootstyle = DANGER, text= "CALCULAR", width=15, command=logica).pack(pady=8)
    
    print (logica)
    media.mainloop()


def Conversor_de_Metical():
    global Conversor_de_Metical
    print('Seja bem vindo ao nosso conversor de moedas')
    metical = float (input ('Quantos meticais você tem na carteira: '))
    dolar = metical / 63
    print ('Com {} MT, você pode comprar {} USD'.format(metical, dolar))


def tabuada():
    global tabuada
    print('Seja bem vindo a Tabuada')
    numero = int (input ('Digite um número para ver a sua tabuada: '))
    for sequencia in range (1,13):
        print ('%2d x %2d = %3d' % (sequencia, numero, sequencia*numero))

def Calcular_Quantidade_de_Tinta():
    global Calcular_Quantidade_de_Tinta
    print("Seja bem vindo ao nosso Calculdaor de Quantidade de Tinta para uma Parede")
    larg = float (input ('Por favor, nos forneça a Largura da parede: '))
    alt = float (input('Altura da parede: '))
    area = larg * alt
    print ('Sua parede tem a dimensão de {}x{} e a sua área é de {}m2'.format(larg, alt, area))
    tinta = area / 2
    print ('Para pintar essa parede, você pricisará de {}l de tinta'.format(tinta))

def Contador_de_Letras():
    global Contador_de_Letras

    print("Olá, seja bem vindo ao nosso contador de caractéres")
    frase = input('Por favor, digite a sua frase ')
    letra = len(frase)
    print("Ótimo!\nAqui está a quantidade de caractéres na sua frase:",letra)
        

def Jogo_Da_Velha():
        from tkinter import messagebox
        from turtle import width
        import numpy as np

        size_of_board = 600
        symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
        symbol_thickness = 50
        symbol_X_color = '#EE4035'
        symbol_O_color = '#0492CF'
        Green_color = '#7BC043'


        class Tic_Tac_Toe():
            # ------------------------------------------------------------------
            # Initialization Functions:
            # ------------------------------------------------------------------
            def __init__(self):
                self.window = Tk()
                self.window.title('Jogo da Velha')
                self.window.configure(background="white")
                self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
                self.canvas.pack()
                # Input from user in form of clicks
                self.window.bind('<Button-1>', self.click)

                self.initialize_board()
                self.player_X_turns = True
                self.board_status = np.zeros(shape=(3, 3))

                self.player_X_starts = True
                self.reset_board = False
                self.gameover = False
                self.tie = False
                self.X_wins = False
                self.O_wins = False

                self.X_score = 0
                self.O_score = 0
                self.tie_score = 0

            def mainloop(self):
                self.window.mainloop()

            def initialize_board(self):
                for i in range(2):
                    self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

                for i in range(2):
                    self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

            def play_again(self):
                self.initialize_board()
                self.player_X_starts = not self.player_X_starts
                self.player_X_turns = self.player_X_starts
                self.board_status = np.zeros(shape=(3, 3))

            # ------------------------------------------------------------------
            # Drawing Functions:
            # The modules required to draw required game based object on canvas
            # ------------------------------------------------------------------

            def draw_O(self, logical_position):
                logical_position = np.array(logical_position)
                # logical_position = grid value on the board
                # grid_position = actual pixel values of the center of the grid
                grid_position = self.convert_logical_to_grid_position(logical_position)
                self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                        grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                        outline=symbol_O_color)

            def draw_X(self, logical_position):
                grid_position = self.convert_logical_to_grid_position(logical_position)
                self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                        grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                        fill=symbol_X_color)
                self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                        grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                        fill=symbol_X_color)

            def display_gameover(self):

                if self.X_wins:
                    self.X_score += 1
                    text = messagebox.showinfo("Vencedor", 'Jodador 1 venceu a rodada!')
                    color = symbol_X_color
                    
                elif self.O_wins:
                    self.O_score += 1
                    text = messagebox.showinfo("Vencedor", 'Jodador 2 venceu a rodada!')
                    color = symbol_O_color
                else:
                    self.tie_score += 1
                    text = messagebox.showinfo('Empate', "Jogo empatado")
                    color = 'gray'

                self.canvas.delete("all")
                self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

                score_text = 'Pontuação \n'
                self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                        text=score_text)

                score_text = 'Jogador 1 (X) : ' + str(self.X_score) + '\n'
                score_text += 'Jogador 2 (O) : ' + str(self.O_score) + '\n'
                score_text += 'Empate     : ' + str(self.tie_score)
                self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                        text=score_text)
                self.reset_board = True

                score_text = 'Clique para jogar novamente \n'
                self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="red",
                                        text=score_text)

            # ------------------------------------------------------------------
            # Logical Functions:
            # The modules required to carry out game logic
            # ------------------------------------------------------------------

            def convert_logical_to_grid_position(self, logical_position):
                logical_position = np.array(logical_position, dtype=int)
                return (size_of_board / 3) * logical_position + size_of_board / 6

            def convert_grid_to_logical_position(self, grid_position):
                grid_position = np.array(grid_position)
                return np.array(grid_position // (size_of_board / 3), dtype=int)

            def is_grid_occupied(self, logical_position):
                if self.board_status[logical_position[0]][logical_position[1]] == 0:
                    return False
                else:
                    return True

            def is_winner(self, player):

                player = -1 if player == 'X' else 1

                # Three in a row
                for i in range(3):
                    if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                        return True
                    if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                        return True

                # Diagonals
                if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
                    return True

                if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
                    return True

                return False

            def is_tie(self):

                r, c = np.where(self.board_status == 0)
                tie = False
                if len(r) == 0:
                    tie = True

                return tie

            def is_gameover(self):
                # Either someone wins or all grid occupied
                self.X_wins = self.is_winner('X')
                if not self.X_wins:
                    self.O_wins = self.is_winner('O')

                if not self.O_wins:
                    self.tie = self.is_tie()

                gameover = self.X_wins or self.O_wins or self.tie

                if self.X_wins:
                    print('X ganhou')
                if self.O_wins:
                    print('O ganhou')
                if self.tie:
                    print('Empate')

                return gameover





            def click(self, event):
                grid_position = [event.x, event.y]
                logical_position = self.convert_grid_to_logical_position(grid_position)

                if not self.reset_board:
                    if self.player_X_turns:
                        if not self.is_grid_occupied(logical_position):
                            self.draw_X(logical_position)
                            self.board_status[logical_position[0]][logical_position[1]] = -1
                            self.player_X_turns = not self.player_X_turns
                    else:
                        if not self.is_grid_occupied(logical_position):
                            self.draw_O(logical_position)
                            self.board_status[logical_position[0]][logical_position[1]] = 1
                            self.player_X_turns = not self.player_X_turns

                    # Check if game is concluded
                    if self.is_gameover():
                        self.display_gameover()
                        # print('Done')
                else:  # Play Again
                    self.canvas.delete("all")
                    self.play_again()
                    self.reset_board = False


        game_instance = Tic_Tac_Toe()
        game_instance.mainloop()

opc = ttk.Window(themename="superhero")
opc.geometry("500x300")
opc.title("GD - Menu Principal")
menuprincipal = Label(opc, text="SEJA BEM VINDO AO MENU\n POR FAVOR, SELECIONE UMA OPÇÃO\n").pack(side=TOP)
Botao1 = ttk.Button(text="CALCULADOR DE MEDIA", width=30, command=Calculo_de_Media).pack(pady=2)
Botao2 = ttk.Button(text="CONVERSOR DE MOEDA", width=30, command=Conversor_de_Metical).pack(pady=2)
Botao3 = ttk.Button(text="CÁLCULO DE DIMENSÕES", width=30, command=Calcular_Quantidade_de_Tinta).pack(pady=2)
Botao4 = ttk.Button(text="CONTADOR DE CARACTÉRES", width=30, command=Contador_de_Letras).pack(pady=2)
Botao5 = ttk.Button(text="TABUADA", width=30, command=tabuada).pack(pady=2)
Botao6 = ttk.Button(text="JOGO DA VELHA", width=30, command=Jogo_Da_Velha).pack(pady=2)
Botao7 = ttk.Button(text="SAIR", bootstyle= DANGER, width=30, command=exit).pack(pady=2)
print('Por favor, selecione uma das opções abaixo:\n1 - Calculador de Média\n2 - Conversor de Metical para USD\n3 - Tabuada\n4 - Calcular Quantidade de Tinta para uma Parede\n5 - Contador de Caractéres\n6 - Jogo da Velha')

opc.mainloop()
















