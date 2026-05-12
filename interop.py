import os
import subprocess
from datetime import datetime
# ───────────────────────────────────────────────────────
# ACTIVIDAD 5 — Preguntas de reflexión
# ───────────────────────────────────────────────────────
#
# 1. ¿Cuál es la diferencia entre /mnt/c/ y \\wsl$\Ubuntu\?
#    /mnt/c/ se usa desde Ubuntu/WSL para acceder al disco
#    de Windows (NTFS). \\wsl$\Ubuntu\ se usa desde Windows
#    para acceder al sistema de archivos de Ubuntu (ext4).
#    Cada ruta apunta en dirección contraria pero al mismo
#    disco físico.
#
# 2. ¿Por qué Ubuntu puede leer archivos NTFS sin instalar nada?
#    WSL monta automáticamente las particiones de Windows al
#    arrancar usando "puntos de montaje". Un mount point es
#    una carpeta que representa otro sistema de archivos.
#    WSL mapea C:\ a /mnt/c/ para que Linux pueda acceder
#    sin drivers adicionales.
#
# 3. ¿Relación con temas del semestre?
#    Se aplica el concepto de sistema de archivos visto en
#    prácticas anteriores, donde el SO administra el acceso
#    a archivos. Aquí dos SO comparten recursos a través de
#    puntos de montaje, similar a como un proceso accede
#    a memoria compartida.
# ───────────────────────────────────────────────────────
# configuracion
USUARIO_WINDOWS = "Lenovo"
USUARIO_UBUNTU = "lenovo"

# Rutas
carpeta_windows = f"/mnt/c/Users/{USUARIO_WINDOWS}/Desktop/practica_so"
carpeta_ubuntu = f"/home/{USUARIO_UBUNTU}/datos_ubuntu"

# 1. Leer archivo que está en Windows
ruta_origen = os.path.join(carpeta_windows, "reporte.txt")
print("\n📂 Leyendo desde Windows...")
with open(ruta_origen, 'r') as f:
    contenido = f.read()
print(contenido)

# 2. Recolectar info adicional desde Ubuntu
info_ubuntu = subprocess.run(
    ['bash', '-c', 'free -h | grep Mem'],
    capture_output=True, text=True
).stdout.strip()

# 3. Guardar reporte combinado en Ubuntu
ruta_destino = os.path.join(carpeta_ubuntu, "reporte_combinado.txt")
with open(ruta_destino, 'w') as f:
    f.write("=== REPORTE COMBINADO Windows + Ubuntu ===\n")
    f.write(f"Generado: {datetime.now()}\n\n")
    f.write("--- Datos leídos desde Windows ---\n")
    f.write(contenido + "\n")
    f.write("--- Datos de Ubuntu ---\n")
    f.write(f"Memoria: {info_ubuntu}\n")

print(f"\n✅ Reporte combinado guardado en Ubuntu:")
print(f"   {ruta_destino}")
print(f"   También visible en Windows: \\\\wsl$\\Ubuntu{ruta_destino}")
