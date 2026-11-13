import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import csv
from datetime import datetime

def open_win_form(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Reportar un riesgo")
    win.geometry("520x420")
    
    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)
    
    # Encabezado
    ttk.Label(frm, text="Nuevo reporte de riesgo", font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 2))
    ttk.Label(frm, text="Ayuda a otros a moverse seguros. Todos los campos son obligatorios.").grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 15))
    
    # Campos del formulario
    ttk.Label(frm, text="Zona o colonia:").grid(row=2, column=0, sticky="w", pady=5)
    entry_zona = ttk.Entry(frm, width=30)
    entry_zona.insert(0, "Centro")
    entry_zona.grid(row=2, column=1, sticky="ew", pady=5)
    
    ttk.Label(frm, text="Tipo de riesgo:").grid(row=3, column=0, sticky="w", pady=5)
    combo_riesgo = ttk.Combobox(
        frm, 
        width=28, 
        values=["Casi accidente", "Auto que no respeta el paso", "Cruce sin semáforo", "Banqueta dañada"], 
        state="readonly"
    )
    combo_riesgo.set("Cruce sin semáforo")
    combo_riesgo.grid(row=3, column=1, sticky="ew", pady=5)
    
    ttk.Label(frm, text="Fecha:").grid(row=4, column=0, sticky="w", pady=5)
    entry_fecha = ttk.Entry(frm, width=30)
    entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
    entry_fecha.grid(row=4, column=1, sticky="ew", pady=5)
    
    ttk.Label(frm, text="Hora (0–23):").grid(row=5, column=0, sticky="w", pady=5)
    spin_hora = ttk.Spinbox(frm, from_=0, to=23, width=5)
    spin_hora.set(7)
    spin_hora.grid(row=5, column=1, sticky="w", pady=5)
    
    ttk.Label(frm, text="Calificación de seguridad (1-5):").grid(row=6, column=0, sticky="w", pady=5)
    spin_cal = ttk.Spinbox(frm, from_=1, to=5, width=5)
    spin_cal.set(2)
    spin_cal.grid(row=6, column=1, sticky="w", pady=5)
    
    def limpiar():
        entry_zona.delete(0, tk.END)
        combo_riesgo.set("")
        entry_fecha.delete(0, tk.END)
        spin_hora.set(0)
        spin_cal.set(1)
        
    def guardar():
        zona = entry_zona.get().strip()
        riesgo = combo_riesgo.get().strip()
        fecha = entry_fecha.get().strip()
        
        try:
            hora = int(spin_hora.get())
            cal = int(spin_cal.get())
        except ValueError:
            messagebox.showerror("Datos inválidos", "La hora y la calificación de seguridad deben ser números enteros.")
            return
            
        if not zona or not riesgo or not fecha:
            messagebox.showerror("Campos vacíos", "Todos los campos son obligatorios.")
            return
            
        ruta = Path(__file__).resolve().parents[2] / "data" / "reportes_riesgo.csv"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        nuevo = not ruta.exists()
        
        with ruta.open("a", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            if nuevo:
                w.writerow(["zona_colonia", "tipo_riesgo", "fecha", "hora", "calificacion"])
            w.writerow([zona, riesgo, fecha, hora, cal])
            
        messagebox.showinfo("Guardado", f"Reporte guardado en {ruta.name}")
        win.destroy()
        
    # Botones inferiores (Limpiar y Guardar reporte)
    frm_botones = ttk.Frame(frm)
    frm_botones.grid(row=7, column=0, columnspan=2, pady=20, sticky="e")
    
    ttk.Button(frm_botones, text="Limpiar", command=limpiar).pack(side=tk.LEFT, padx=5)
    ttk.Button(frm_botones, text="Guardar reporte", command=guardar).pack(side=tk.LEFT, padx=5)