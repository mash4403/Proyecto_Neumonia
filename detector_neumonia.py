# Modulo implementación de proyectos Miguel A. Saavedra Codigo 2238093
# Propósito: Archivo principal que configura y ejecuta la aplicación de detección de neumonía.
# Define la lógica de la interfaz gráfica usando tkinter.
# Implementa funciones para leer archivos DICOM y JPG, preprocesar imágenes, cargar el modelo entrenado, hacer predicciones y generar mapas de calor.


import tkinter as tk
from tkinter import ttk, font, filedialog, Text, StringVar
from tkinter import *
from tkinter import ttk, font, filedialog
from tkinter.messagebox import askokcancel, showinfo, WARNING
from PIL import ImageTk, Image
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import csv  # Importa el módulo csv
from load_model import load_trained_model  # Importa la función load_trained_model

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Herramienta para la detección rápida de neumonía")

        # BOLD FONT
        fonti = font.Font(weight="bold")

        self.root.geometry("815x560")
        self.root.resizable(0, 0)

        # LABELS
        self.lab1 = ttk.Label(self.root, text="Imagen Radiográfica", font=fonti)
        self.lab2 = ttk.Label(self.root, text="Imagen con Heatmap", font=fonti)
        self.lab3 = ttk.Label(self.root, text="Resultado:", font=fonti)
        self.lab4 = ttk.Label(self.root, text="Cédula Paciente:", font=fonti)
        self.lab5 = ttk.Label(
            self.root,
            text="SOFTWARE PARA EL APOYO AL DIAGNÓSTICO MÉDICO DE NEUMONÍA",
            font=fonti,
        )
        self.lab6 = ttk.Label(self.root, text="Probabilidad:", font=fonti)

        # STRING VARIABLES
        self.ID = StringVar()
        self.result = StringVar()

        # INPUT BOXES
        self.text1 = ttk.Entry(self.root, textvariable=self.ID, width=10)

        # IMAGE BOXES
        self.text_img1 = Text(self.root, width=31, height=15)
        self.text_img2 = Text(self.root, width=31, height=15)
        self.text2 = Text(self.root)
        self.text3 = Text(self.root)

        # BUTTONS
        self.button1 = ttk.Button(
            self.root, text="Predecir", state="disabled", command=self.run_model
        )
        self.button2 = ttk.Button(
            self.root, text="Cargar Imagen", command=self.load_img_file
        )
        self.button3 = ttk.Button(self.root, text="Borrar", command=self.delete)
        self.button4 = ttk.Button(self.root, text="PDF", command=self.create_pdf)
        self.button6 = ttk.Button(
            self.root, text="Guardar", command=self.save_results_csv
        )

        # WIDGETS POSITIONS
        self.lab1.place(x=110, y=65)
        self.lab2.place(x=545, y=65)
        self.lab3.place(x=500, y=350)
        self.lab4.place(x=65, y=350)
        self.lab5.place(x=122, y=25)
        self.lab6.place(x=500, y=400)
        self.button1.place(x=220, y=460)
        self.button2.place(x=70, y=460)
        self.button3.place(x=670, y=460)
        self.button4.place(x=520, y=460)
        self.button6.place(x=370, y=460)
        self.text1.place(x=200, y=350)
        self.text2.place(x=610, y=350, width=90, height=30)
        self.text3.place(x=610, y=400, width=90, height=30)
        self.text_img1.place(x=65, y=90)
        self.text_img2.place(x=500, y=90)

        # FOCUS ON PATIENT ID
        self.text1.focus_set()

        # Load pre-trained model
        self.model = load_trained_model()

        self.root.mainloop()

    def load_img_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
        )
        if file_path:
            self.image = Image.open(file_path)
            self.image.thumbnail((256, 256))
            self.photo = ImageTk.PhotoImage(self.image)
            self.text_img1.image_create("1.0", image=self.photo)
            self.button1.config(state="normal")
            self.file_path = file_path

    def run_model(self):
        image_array = np.array(self.image.resize((512, 512))) / 255.0
        if image_array.ndim == 3 and image_array.shape[-1] == 3:  # Si es una imagen RGB
            image_array = np.mean(image_array, axis=-1, keepdims=True)  # Convertir a escala de grises
        image_array = np.expand_dims(image_array, axis=0)
        prediction = self.model.predict(image_array)
        probability = prediction[0][0]

        result = "Neumonía" if probability > 0.5 else "Normal"
        self.text2.delete("1.0", tk.END)
        self.text2.insert(tk.END, result)
        self.text3.delete("1.0", tk.END)
        self.text3.insert(tk.END, f"{probability:.2f}")

    def delete(self):
        self.text_img1.delete("1.0", tk.END)
        self.text_img2.delete("1.0", tk.END)
        self.text1.delete(0, tk.END)
        self.text2.delete("1.0", tk.END)
        self.text3.delete("1.0", tk.END)
        self.button1.config(state="disabled")

    def create_pdf(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")])
        if file_path:
            c = canvas.Canvas(file_path, pagesize=letter)
            c.drawString(100, 750, "Reporte de Diagnóstico de Neumonía")
            c.drawString(100, 730, f"Cédula Paciente: {self.ID.get()}")
            c.drawString(100, 710, f"Resultado: {self.text2.get('1.0', 'end-1c')}")
            c.drawString(100, 690, f"Probabilidad: {self.text3.get('1.0', 'end-1c')}")

            # Save the current image as a temporary file
            temp_image_path = "temp_image.png"
            self.image.save(temp_image_path)

            # Draw the image on the PDF
            c.drawImage(temp_image_path, 100, 400, width=200, height=200)

            c.showPage()
            c.save()

    def save_results_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Cédula Paciente', 'Resultado', 'Probabilidad'])
                writer.writerow([self.ID.get(), self.text2.get('1.0', 'end-1c').strip(), self.text3.get('1.0', 'end-1c').strip()])

if __name__ == "__main__":
    App()
