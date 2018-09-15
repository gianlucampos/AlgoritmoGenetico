from tkinter import *

# Frames e containers
root = Tk()
root.winfo_toplevel().title("Algoritmo genético")
root.geometry("500x300+500+100")
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Campos
label_n_cronossomos = Label(root, text="Nº de cronossomos:")
label_n_cronossomos.pack()
entrada_n_cronossomos = Entry(root)
entrada_n_cronossomos.pack()
label_n_geracoes = Label(root, text="Nº de gerações:")
label_n_geracoes.pack()
entrada_n_geracoes = Entry(root)
entrada_n_geracoes.pack()
label_pc = Label(root, text="Taxa de crossover:")
label_pc.pack()
entrada_pc = Entry(root)
entrada_pc.pack()
label_pm = Label(root, text="Taxa de mutação:")
label_pm.pack()
entrada_pm = Entry(root)
entrada_pm.pack()
label_melhorCronossomo = Label(root, text="Melhor Cronossomo:")
label_melhorCronossomo.pack()
entrada_melhorCronossomo = Entry(root)
entrada_melhorCronossomo.pack()


def valida():
    return valida_generico(entrada_n_cronossomos) \
           & valida_generico(entrada_n_geracoes) \
           & valida_generico(entrada_pm) \
           & valida_generico(entrada_pc)


def valida_generico(n1):
    try:
        int(n1.get())
    except ValueError:
        if len(n1.get()) == 0:
            n1.delete(0, END)
            n1.insert(0, "Preencha este campo")
        else:
            n1.delete(0, END)
            n1.insert(0, "Valor deve ser Inteiro")
        return False
    return True


def calcular_cronossomo():
    if valida():
        entrada_melhorCronossomo.delete(0, END)
        entrada_melhorCronossomo.insert(0, int(entrada_n_geracoes.get()) + int(entrada_n_cronossomos.get()))


def limpar_texto():
    entrada_n_cronossomos.delete(0, END)
    entrada_n_geracoes.delete(0, END)
    entrada_pc.delete(0, END)
    entrada_pm.delete(0, END)
    entrada_melhorCronossomo.delete(0, END)


# Botões
botao_calcular = Button(bottomFrame, text="Calcular", fg="black", command=lambda: calcular_cronossomo())
botao_calcular.pack(side=LEFT)
botao_limpar = Button(bottomFrame, text="Limpar Campos", fg="black", command=lambda: limpar_texto())
botao_limpar.pack(side=LEFT)

root.mainloop()
