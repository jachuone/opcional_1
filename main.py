
# main.py
from MLFQ import MLFQ
from Cola import Cola
from Proceso import Proceso
from MLFQ import MLFQ, cargar_procesos_desde_archivo

def generar_archivo_entrada():
    # Contenido de ejemplo para el archivo mlq001.txt
    contenido = """# archivo: mlq001.txt
# etiqueta; BT; AT; Q; Pr
A;6;0;1;5
B;9;0;1;4
C;10;0;2;3
D;15;0;2;3
E;8;0;3;2
"""

    # Crear el archivo 'mlq001.txt' con el contenido
    with open('mlq001.txt', 'w') as f:
        f.write(contenido)
    print("Archivo 'mlq001.txt' generado con éxito.")

def main():
    # Generar el archivo de entrada
    generar_archivo_entrada()

    # Leer los datos de los procesos desde el archivo de texto
    archivo = "mlq001.txt"  # El archivo que contiene los procesos
    procesos = cargar_procesos_desde_archivo(archivo)
    
    # Crear instancia de MLFQ
    mlfq = MLFQ()
    mlfq.agregar_cola(1, Cola('RR', quantum=1))
    mlfq.agregar_cola(2, Cola('RR', quantum=2))
    mlfq.agregar_cola(3, Cola('SJF'))

    # Cargar los procesos a las colas correspondientes
    mlfq.cargar_procesos(procesos)

    # Ejecutar el algoritmo MLFQ
    mlfq.ejecutar()
    
    # Generar archivo de salida con los resultados
    mlfq.generar_salida()

if __name__ == "__main__":
    main()



