import os  # <--- Esto quita el error en 'os.path'
from PIL import Image # <--- Esto quita el error en 'Image.open'
import customtkinter as ctk
from tkinter import messagebox
from logica import Factura #llamo al codigo detras de todo

class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Facturación - Pharma Big")
        self.geometry("500x550")

         # --- Manejo del Logo ---
        self.nombre_logo = "logo_pharmabig.png" 
        ruta_logo = os.path.join(os.path.dirname(__file__), self.nombre_logo)

        try:
            image = Image.open(ruta_logo)
            self.logo_image = ctk.CTkImage(light_image=image, size=(120, 120))
            self.label_logo = ctk.CTkLabel(self, image=self.logo_image, text="")
            self.label_logo.pack(pady=(20, 0)) # Esto lo pone arriba de todo
        except:
            print("Logo no encontrado, saltando...")

        # Configuración visual
        self.label_titulo = ctk.CTkLabel(self, text="NUEVA FACTURA", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20)

        # Inputs o entradas
        self.ent_cliente = ctk.CTkEntry(self, placeholder_text="Nombre del Cliente", width=300)
        self.ent_cliente.pack(pady=10)

       

        self.ent_nit = ctk.CTkEntry(self, placeholder_text="NIT / Cédula", width=300)
        self.ent_nit.pack(pady=10)

        self.ent_producto = ctk.CTkEntry(self, placeholder_text="Descripción del Servicio", width=300)
        self.ent_producto.pack(pady=10)

        self.ent_precio = ctk.CTkEntry(self, placeholder_text="Precio Unitario", width=300)
        self.ent_precio.pack(pady=10)

        self.ent_cantidad = ctk.CTkEntry(self, placeholder_text="Cantidad", width=300)
        self.ent_cantidad.pack(pady=10)

        # Botón
        self.btn_generar = ctk.CTkButton(self, text="Procesar Factura", command=self.evento_boton)
        self.btn_generar.pack(pady=30)

    def evento_boton(self):
        try:
            # Creamos un objeto de la clase Factura (del otro archivo)
            nueva_factura = Factura(
                self.ent_cliente.get(),
                self.ent_nit.get(),
                self.ent_producto.get(),
                self.ent_precio.get(),
                self.ent_cantidad.get()
            )

            resumen = (
                f"Cliente: {nueva_factura.cliente}\n"
                f"Subtotal: ${nueva_factura.calcular_subtotal():,.0f}\n"
                f"IVA (19%): ${nueva_factura.calcular_iva():,.0f}\n"
                f"TOTAL: ${nueva_factura.calcular_total():,.0f}"
            )
            messagebox.showinfo("Factura Lista", resumen)

        except ValueError:
            messagebox.showerror("Error", "Revisa los números ingresados")
            # --- Manejo del Logo ---
