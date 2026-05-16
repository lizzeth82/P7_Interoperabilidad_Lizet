# Práctica 7: Interoperabilidad WSL y Windows
Estudiante: Lizet (24760082)
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
