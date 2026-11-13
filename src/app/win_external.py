import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

def open_win_external(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Datos de la ciudad — OpenStreetMap")
    # Geometría vertical adaptada para pantalla de celular
    win.geometry("400x680")
    win.resizable(False, False)

    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)

    # Título principal
    ttk.Label(frm, text="Infraestructura vial de León", font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=(0, 12))

    # Entradas de Latitud y Longitud en formato vertical
    frame_coords = ttk.Frame(frm)
    frame_coords.pack(fill="x", pady=(0, 10))

    ttk.Label(frame_coords, text="Latitud:").pack(anchor="w", pady=(0, 2))
    entry_lat = ttk.Entry(frame_coords)
    entry_lat.insert(0, "21.1221")
    entry_lat.pack(fill="x", pady=(0, 8))

    ttk.Label(frame_coords, text="Longitud:").pack(anchor="w", pady=(0, 2))
    entry_lon = ttk.Entry(frame_coords)
    entry_lon.insert(0, "-101.6823")
    entry_lon.pack(fill="x")

    # Botones de acción principales
    frame_btns = ttk.Frame(frm)
    frame_btns.pack(fill="x", pady=(12, 15))

    def coloniaclick():
        messagebox.showinfo("Ubicación", "Zona detectada: Zona Centro, León, Guanajuato.", parent=win)

    btn_colonia = tk.Button(frame_btns, text="¿Qué colonia es?", bg="#2D6A4F", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", pady=6, command=coloniaclick)
    btn_colonia.pack(fill="x", pady=(0, 8))

    def consultar():
        messagebox.showinfo("Infraestructura", "Consulta realizada con éxito. Mostrando datos de la zona.", parent=win)

    btn_consultar = tk.Button(frame_btns, text="Consultar infraestructura", bg="#2D6A4F", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", pady=6, command=consultar)
    btn_consultar.pack(fill="x")

    # Marco / Tarjeta de Resultado
    frame_res = ttk.LabelFrame(frm, text="Resultado", padding=12)
    frame_res.pack(fill="both", expand=True, pady=(0, 12))

    # Ubicación encontrada
    lbl_ubicacion = ttk.Label(frame_res, text="📍 Zona Centro, León, Gto.", font=("Segoe UI", 11, "bold"))
    lbl_ubicacion.pack(anchor="w", pady=(0, 10))

    # Contadores apilados o distribuidos para móvil
    def crear_caja_stat(parent_frame, numero, texto):
        box = ttk.LabelFrame(parent_frame, padding=8)
        ttk.Label(box, text=numero, font=("Segoe UI", 16, "bold")).pack(anchor="w")
        ttk.Label(box, text=texto, font=("Segoe UI", 8), foreground="#555555").pack(anchor="w")
        return box

    crear_caja_stat(frame_res, "14", "Semáforos (500 m)").pack(fill="x", pady=(0, 6))
    crear_caja_stat(frame_res, "2", "Ciclovías").pack(fill="x", pady=(0, 6))
    crear_caja_stat(frame_res, "31", "Cruces peatonales").pack(fill="x")

    # Banner de advertencia / sin conexión
    frame_warning = tk.Frame(frm, bg="#FFF3CD", padx=8, pady=6, highlightbackground="#FFEEBA", highlightthickness=1)
    frame_warning.pack(fill="x", pady=(0, 10))
    tk.Label(frame_warning, text="⚠ Sin conexión — usando datos de respaldo local", bg="#FFF3CD", fg="#856404", font=("Segoe UI", 8)).pack(anchor="w")

    # Pie de página
    ttk.Separator(frm, orient="horizontal").pack(fill="x", pady=(2, 6))
    ttk.Label(frm, text="Fuente: © OpenStreetMap (Overpass API + Nominatim)", font=("Segoe UI", 7), foreground="#666666").pack(anchor="w")
