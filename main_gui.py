import tkinter as tk
from tkinter import messagebox, filedialog
import csv

class PresupuestoApp:
    def __init__(self, master):
        self.master = master
        master.title("Presupuesto de Obra")
        self.rubros = []

        # Campos de entrada
        self.descripcion_label = tk.Label(master, text="Descripción:")
        self.descripcion_label.grid(row=0, column=0)
        self.descripcion_entry = tk.Entry(master)
        self.descripcion_entry.grid(row=0, column=1)

        self.unidad_label = tk.Label(master, text="Unidad:")
        self.unidad_label.grid(row=1, column=0)
        self.unidad_entry = tk.Entry(master)
        self.unidad_entry.grid(row=1, column=1)

        self.cantidad_label = tk.Label(master, text="Cantidad:")
        self.cantidad_label.grid(row=2, column=0)
        self.cantidad_entry = tk.Entry(master)
        self.cantidad_entry.grid(row=2, column=1)

        self.precio_label = tk.Label(master, text="Precio Unitario:")
        self.precio_label.grid(row=3, column=0)
        self.precio_entry = tk.Entry(master)
        self.precio_entry.grid(row=3, column=1)

        # Botones
        self.agregar_button = tk.Button(master, text="Agregar Rubro", command=self.agregar_rubro)
        self.agregar_button.grid(row=4, column=0, columnspan=2)

        self.guardar_button = tk.Button(master, text="Guardar Presupuesto", command=self.guardar_presupuesto)
        self.guardar_button.grid(row=5, column=0, columnspan=2)

        self.total_label = tk.Label(master, text="Total: $0.00")
        self.total_label.grid(row=6, column=0, columnspan=2)

    def agregar_rubro(self):
        descripcion = self.descripcion_entry.get()
        unidad = self.unidad_entry.get()
        try:
            cantidad = float(self.cantidad_entry.get())
            precio = float(self.precio_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Cantidad y precio deben ser números")
            return

        subtotal = cantidad * precio
        self.rubros.append([descripcion, unidad, cantidad, precio, subtotal])
        self.actualizar_total()

        self.descripcion_entry.delete(0, tk.END)
        self.unidad_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)

    def actualizar_total(self):
        total = sum(rubro[4] for rubro in self.rubros)
        self.total_label.config(text=f"Total: ${total:.2f}")

    def guardar_presupuesto(self):
        if not self.rubros:
            messagebox.showwarning("Advertencia", "No hay rubros para guardar")
            return

        archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivo CSV", "*.csv")])
        if not archivo:
            return

        with open(archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Descripción", "Unidad", "Cantidad", "Precio Unitario", "Subtotal"])
            writer.writerows(self.rubros)

        messagebox.showinfo("Éxito", f"Presupuesto guardado en {archivo}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PresupuestoApp(root)
    root.mainloop()
