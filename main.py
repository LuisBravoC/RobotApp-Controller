import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.constants import *
from ttkbootstrap import Style
from tkinter import messagebox
from time import sleep
from pyfirmata import Arduino, util, SERVO

# configuracion de placa Arduino
board = Arduino('COM3')
sleep(5)

# Pines donde se conectaran los servos del brazo robot
pinS1 = 3  # Base
pinS2 = 6  # Antebrazo
pinS3 = 10  # Brazo
pinS4 = 11  # Gripper

board.digital[pinS1].mode = SERVO
board.digital[pinS2].mode = SERVO
board.digital[pinS3].mode = SERVO
board.digital[pinS4].mode = SERVO

board.digital[pinS1].write(1)
board.digital[pinS2].write(45)
board.digital[pinS3].write(60)

# Funciones para mover articulaciones del brazo Robot


def servo1(posiciones1):
    # Escritura de angulo en Servomotor
    board.digital[pinS1].write(int(float(posiciones1)))


def servo2(posiciones2):
    # Escritura de angulo en Servomotor
    board.digital[pinS2].write(posiciones2)


def servo3(posiciones3):
    # Escritura de angulo en Servomotor
    board.digital[pinS3].write(posiciones3)

# Abrir garra


def abrir():
    print("Hola")
    board.digital[pinS4].write(60)

# Cerrar Garra


def cerrar():
    board.digital[pinS4].write(0)

# Clase para control manual del brazo


class Control(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.g1 = IntVar()
        self.g2 = IntVar()
        self.g3 = IntVar()

        self.r1 = 0
        self.r2 = 0
        self.r3 = 0

        self.img = PhotoImage(file="C:/Users/luism/Documents/Icono.png")
        self.logo = Label(self, image=self.img)
        self.logo.place(x=280, y=25)

        self.grades_button = ttk.Button(
            self, text="Abrir pinza", command=abrir, width=25)
        self.grades_button.grid(row=8, column=0, pady=(15, 0))

        self.print_button = ttk.Button(
            self, text="Cerrar pinza", command=cerrar, width=25)
        self.print_button.grid(row=9, column=0, pady=(10, 0))

        # Label posicion base
        self.label_grade1 = ttk.Label(self)
        # Barra de posicion base
        self.scale1 = ttk.Scale(
            self, variable=self.g1,
            command=self.servo1,
            length=200,
            from_=1,
            to=180,
            orient=HORIZONTAL)

        # Label Grado 2
        self.label_grade2 = ttk.Label(self)
        # Barra de posicion brazo
        self.scale2 = ttk.Scale(
            self, variable=self.g2,
            command=self.servo2,
            length=200,
            from_=45,
            to=130,
            orient=HORIZONTAL,)

        # Label Grado 3
        self.label_grade3 = ttk.Label(self)
        # Barra de posicion antebrazo
        self.scale3 = ttk.Scale(
            self, variable=self.g3,
            command=self.servo3,
            length=200,
            from_=60,
            to=160,
            orient=HORIZONTAL)

       # Mostrar las escalas y sus labels
        self.label_grade1.grid(pady=(10, 0), row=1, column=0)
        self.label_grade1.config(text="Base = 1°")
        self.scale1.grid(row=2, column=0)

        self.label_grade2.grid(pady=(10, 0), row=3, column=0)
        self.label_grade2.config(text="Antebrazo = 1°")
        self.scale2.grid(row=4, column=0)

        self.label_grade3.grid(pady=(10, 0), row=5, column=0)
        self.label_grade3.config(text="Brazo = 1°")
        self.scale3.grid(row=6, column=0)

        # Mostrar y textboxs
        self.entry_label1 = ttk.Label(self)
        self.entry_label1.grid(padx=(30, 0), pady=(10, 0), row=8, column=1)
        self.entry_label1.config(text="Base")

        #self.grade_entry1 = ttk.Entry(self, width=5, validate ="key", validatecommand= self.entry1)
        self.grade_entry1 = ttk.Entry(self, width=5)
        self.grade_entry1.insert(0, 1)
        self.grade_entry1.grid(padx=(30, 0), pady=(10, 0), row=9, column=1)

        self.entry_label2 = ttk.Label(self)
        self.entry_label2.grid(padx=15, pady=(10, 0), row=8, column=2)
        self.entry_label2.config(text="Antebrazo")

        self.grade_entry2 = ttk.Entry(self, width=5)
        self.grade_entry2.insert(0, 1)
        self.grade_entry2.grid(pady=(10, 0), row=9, column=2)

        self.entry_label3 = ttk.Label(self)
        self.entry_label3.grid(padx=15, pady=(10, 0), row=8, column=3)
        self.entry_label3.config(text="Brazo")

        self.grade_entry3 = ttk.Entry(self, width=5)
        self.grade_entry3.insert(0, 1)
        self.grade_entry3.grid(pady=(10, 0), row=9, column=3)

    # Funciones para mover articulaciones del brazo Robot

    def servo1(self, r1):
        # Escritura de angulo en Servomotor
        self.r1 = self.g1.get()
        board.digital[pinS1].write(self.r1)

        sel1 = "Base = " + str(self.r1) + "°"
        self.label_grade1.config(text=sel1)
        self.grade_entry1.delete(0, tk.END)
        self.grade_entry1.insert(0, self.r1)

    def servo2(self, r2):
        self.r2 = self.g2.get()
        # Escritura de angulo en Servomotor
        board.digital[pinS2].write(self.r2)

        sel2 = "Antebrazo = " + str(self.r2) + "°"
        self.label_grade2.config(text=sel2)
        self.grade_entry2.delete(0, tk.END)
        self.grade_entry2.insert(0, self.r2)

    def servo3(self, r3):
        self.r3 = self.g3.get()
        # Escritura de angulo en Servomotor
        board.digital[pinS3].write(self.r3)

        sel3 = "Brazo = " + str(self.r3) + "°"
        self.label_grade3.config(text=sel3)
        self.grade_entry3.delete(0, tk.END)
        self.grade_entry3.insert(0, self.r3)

    def entry1(self):
        self.r1 = self.g1.get()
        print("Entry r1" + str(self.r1))
        self.scale1.config(to=self.r1)
        return True

    def info(self):
        messagebox.showinfo("Informacion",
                            "Modo de uso: \nDesplazar cada perilla para mover las articulaciones del brazo robot \nPara abrir y cerrar el gripper, precione los respectivos botones")

    # Viejas funciones sin uso actual

    def scale_show(self):
        self.r1 = self.g1.get()
        self.r2 = self.g2.get()
        self.r3 = self.g3.get()

        sel1 = "Base = " + str(self.r1) + "°"
        self.label_grade1.config(text=sel1)
        self.grade_entry1.delete(0, tk.END)
        self.grade_entry1.insert(0, self.r1)

        sel2 = "Antebrazo = " + str(self.r2) + "°"
        self.label_grade2.config(text=sel2)
        self.grade_entry2.delete(0, tk.END)
        self.grade_entry2.insert(0, self.r2)

        sel3 = "Brazo = " + str(self.r3) + "°"
        self.label_grade3.config(text=sel3)
        self.grade_entry3.delete(0, tk.END)
        self.grade_entry3.insert(0, self.r3)

    def print_grades(self):
        print("Base: " + str(self.r1))
        print("Antebrazo: " + str(self.r2))
        print("Brazo: " + str(self.r3))

    def get_grades(self):
        self.label_grade1["text"] = \
            "Grados: {}".format(self.name_entry.get())


class Calculations(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Aqui "
                              "va los calculos")
        self.label.pack()

        self.cin_button = ttk.Button(self, text="Cinematica")
        self.cin_button.pack(pady=10)

        self.din_button = ttk.Button(self, text="Dinamica")
        self.din_button.pack()

class Simulation(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Numero de repeticiones")
        self.label.grid(row=0, column=0)
        self.grade_entry1 = ttk.Entry(self)
        self.grade_entry1.insert(0, 1)
        self.grade_entry1.grid(padx=(0, 0), pady=(10, 0), row=1, column=0)

        self.grades_button = ttk.Button(
            self, text="Comenzar", command=self.numeroSimulaciones, width=20)
        self.grades_button.grid(row=2, column=0, pady=(15, 0))

        self.print_button = ttk.Button(
            self, text="Simular", command=self.defectoSimulaciones, width=20)
        self.print_button.grid(row=3, column=0, pady=(10, 0))

    def simulacion(self, n):
    
        SleepTime = 0.01
        SleepTimeGarra = 1
        
        board.digital[pinS1].write(1)
        board.digital[pinS2].write(45)
        board.digital[pinS3].write(60)
        
        for i in range(n):
            
            t = "Numero de repeticiones restantes: " + str(n-i)
            self.label["text"] = (t)

            for x in range(1, 106):
                sleep(SleepTime)
                board.digital[pinS1].write(x)
                print("Base: " + str(x))
                
            sleep(SleepTimeGarra)
            board.digital[pinS4].write(60)
            
            sleep(SleepTimeGarra)
            
            for x in range(60, 131):
                sleep(SleepTime)
                board.digital[pinS3].write(x)
                print("Brazo: " + str(x))
                
            sleep(SleepTimeGarra)
            
            board.digital[pinS4].write(0)

            sleep(SleepTimeGarra)
            
            for x in range(130, 60, -1):
                sleep(SleepTime)
                board.digital[pinS3].write(x)
                print("Brazo: " + str(x))
                
            for x in range(105, 1, -1):
                sleep(SleepTime)
                board.digital[pinS1].write(x)
                print("Base: " + str(x))
                
            for x in range(60, 131):
                sleep(SleepTime)
                board.digital[pinS3].write(x)
                print("Brazo: " + str(x))
                
            sleep(SleepTimeGarra)

            board.digital[pinS4].write(60)

            sleep(SleepTimeGarra)
            
            board.digital[pinS4].write(0)
            
            sleep(SleepTimeGarra)
            
            for x in range(130, 60, -1):
                sleep(SleepTime)
                board.digital[pinS3].write(x)
                print("Brazo: " + str(x))
                
            print("Secuencia Finalizada")

    def numeroSimulaciones(self):
        n = self.grade_entry1.get()
        print("Repeticiones: " + n)
        self.simulacion(int(n))

    def defectoSimulaciones(self):
        n = 1
        print("Repeticiones: " + str(n))
        self.simulacion(n)


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Controlador de brazo")
        main_window.iconbitmap("\Icono.ico")
        main_window.geometry("480x300")

        self.notebook = ttk.Notebook(self)

        #style = Style(theme='united')
        style = Style(
            theme='pink', themes_file='C:/Users/luism/Documents/robotapp_themes.json')

        # Frame de control
        self.control_frame = Control(self.notebook)
        self.notebook.add(
            self.control_frame, text="Control manuel", padding=10)
        #self.control_frame.columnconfigure(tuple(range(10)), weight=1)
        #self.control_frame.rowconfigure(tuple(range(5)), weight=1)

        # Frame de calculos
        self.calculations_frame = Calculations(self.notebook)
        self.notebook.add(
            self.calculations_frame, text="Calculos", padding=10)

        # Frame de simulacion
        self.simulation_frame = Simulation(self.notebook)
        self.notebook.add(
            self.simulation_frame, text="Simulacion", padding=10)

        self.notebook.pack(expand=1, fill=tk.BOTH, padx=10, pady=10)
        self.pack(expand=1, fill=tk.BOTH)


main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
