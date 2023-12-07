import tkinter as tk
from tkinter import messagebox

class BancoInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Banco Python")

        self.saldo = 1000  # Saldo inicial

        # Rótulo de saldo
        self.label_saldo = tk.Label(master, text="Saldo: $1000")
        self.label_saldo.pack()

        # Botão de depósito
        self.btn_depositar = tk.Button(master, text="Depositar", command=self.depositar)
        self.btn_depositar.pack()

        # Botão de saque
        self.btn_sacar = tk.Button(master, text="Sacar", command=self.sacar)
        self.btn_sacar.pack()

        # Botão de encerramento
        self.btn_encerrar = tk.Button(master, text="Encerrar", command=self.encerrar)
        self.btn_encerrar.pack()

    def atualizar_saldo(self):
        self.label_saldo.config(text="Saldo: ${}".format(self.saldo))

    def depositar(self):
        valor = float(tk.simpledialog.askstring("Depositar", "Digite o valor a depositar:"))
        self.saldo += valor
        self.atualizar_saldo()
        messagebox.showinfo("Depósito", "Depósito de ${} realizado com sucesso!".format(valor))

    def sacar(self):
        valor = float(tk.simpledialog.askstring("Sacar", "Digite o valor a sacar:"))
        if valor <= self.saldo:
            self.saldo -= valor
            self.atualizar_saldo()
            messagebox.showinfo("Saque", "Saque de ${} realizado com sucesso!".format(valor))
        else:
            messagebox.showerror("Erro", "Saldo insuficiente!")

    def encerrar(self):
        resposta = messagebox.askyesno("Encerrar", "Tem certeza que deseja encerrar?")
        if resposta:
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoInterface(root)
    root.mainloop()
