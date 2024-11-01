import random
import os
import shutil

Eliminar = "C:\\Users\\Josue\\Documents\\Programacion\\src\\Eliminar"
aleatorio = random.randint(1, 5)
print(f"Resultado: {aleatorio}")


if aleatorio == 4 and 3:
    if os.path.exists(Eliminar):
        shutil.rmtree(Eliminar)
        print(f"La carpeta '{Eliminar}' Se a eliminado.")
    else:
        print(f"La carpeta '{Eliminar}' No existe.") 

else:
    print("No se elimino ninguna carpeta ")   
