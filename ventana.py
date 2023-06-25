import tkinter as tk
import requests
from tkinter import messagebox

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de moneda")
        dolar_label = tk.Label(self, text="dólares", font="Calibri 10")
        dolar_label.grid(row=1, column=3)
        self.resizable(0,0)
        self.dolar_entry = tk.Entry(self)
        self.dolar_entry.grid(row=1, column=2)
        self.dolar_entry.configure(background="#8FBC8F")
        boton_salir = tk.Button(self, text="Salir", command=self.destroy).grid(row=4, column=3)
        self.dolar_entry_var = tk.StringVar()
        self.dolar_entry_var.trace("w", self.convertir)
        self.dolar_entry = tk.Entry(self, textvariable=self.dolar_entry_var)
        self.dolar_entry.grid(row=1, column=2)
        self.resultado_label = tk.Label(self, text="")
        self.resultado_label.config(font="Calibri 10")
        tk.Label(self, text="es equivalente a: ").grid(column=0, row=2)
        tk.Label.config(self) 
        tk.Label(self, text="pesos.").grid(column=3, row=2)

        self.resultado_label.grid(row=2, column=2, columnspan=1)
       
    def convertir(self, *args):
        try:
            precio = float(self.dolar_entry.get())
            response = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
            cotizacion = float(response.json()[0]['casa']['venta'].replace(",", "."))
            resultado = precio * cotizacion
            self.resultado_label.config(text=f"${resultado:.2f}")
        except:
            self.resultado_label.config(text="")
            messagebox.showerror(title="Dato mal colocado", message="Ingrese un dato nuevamente")
            
if __name__ == '__main__':
    aplicacion = Ventana()
    aplicacion.mainloop()