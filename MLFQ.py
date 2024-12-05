# mlfq.py
from Cola import Cola
from Proceso import Proceso

class MLFQ:
    def __init__(self):
        self.colas = {}  # Diccionario de colas según el nivel de prioridad
        self.tiempo_actual = 0  # Tiempo de ejecución global
        self.procesos_ejecutados = []  # Lista de procesos ejecutados

    def agregar_cola(self, cola_id, cola):
        self.colas[cola_id] = cola

    def cargar_procesos(self, lista_procesos):
        # Cargar todos los procesos en las colas correctas según su cola asignada
        for proceso in lista_procesos:
            self.colas[proceso.cola].agregar_proceso(proceso)

    def ejecutar(self):
        # Ejecutar los procesos en orden de sus colas y políticas
        while any(not cola.esta_vacia() for cola in self.colas.values()):
            for cola in sorted(self.colas.keys(), reverse=True):  # Prioridad de cola mayor a menor
                if self.colas[cola].esta_vacia():
                    continue
                self.colas[cola].ordenar()
                proceso = self.colas[cola].obtener_siguiente()

                # Asignar tiempo de respuesta (RT) si es el primer momento que se ejecuta el proceso
                if proceso.rt == -1:
                    proceso.rt = self.tiempo_actual - proceso.at

                # Ejecutar el proceso
                tiempo_ejecucion = min(proceso.remanente_bt, self.colas[cola].quantum if self.colas[cola].quantum else proceso.remanente_bt)
                self.tiempo_actual += tiempo_ejecucion
                proceso.remanente_bt -= tiempo_ejecucion

                # Si el proceso termina, registrar su tiempo de finalización
                if proceso.remanente_bt == 0:
                    proceso.ct = self.tiempo_actual
                    proceso.tat = proceso.ct - proceso.at
                    proceso.wt = proceso.tat - proceso.bt
                    self.procesos_ejecutados.append(proceso)

                # Si el proceso no termina, se vuelve a poner en la cola
                if proceso.remanente_bt > 0:
                    self.colas[cola].agregar_proceso(proceso)
                    break

    def generar_salida(self):
        # Generar el archivo de salida con el estado de cada proceso
        salida = []
        suma_wt = suma_ct = suma_rt = suma_tat = 0
        for proceso in self.procesos_ejecutados:
            salida.append(f"{proceso.etiqueta};{proceso.bt};{proceso.at};{proceso.cola};{proceso.prioridad};{proceso.wt};{proceso.ct};{proceso.rt};{proceso.tat}")
            suma_wt += proceso.wt
            suma_ct += proceso.ct
            suma_rt += proceso.rt
            suma_tat += proceso.tat
        
        promedio_wt = suma_wt / len(self.procesos_ejecutados)
        promedio_ct = suma_ct / len(self.procesos_ejecutados)
        promedio_rt = suma_rt / len(self.procesos_ejecutados)
        promedio_tat = suma_tat / len(self.procesos_ejecutados)
        
        salida.append(f"WT={promedio_wt}; CT={promedio_ct}; RT={promedio_rt}; TAT={promedio_tat}")
        
        # Guardar la salida en un archivo
        with open("salida_mlfq.txt", "w") as f:
            for line in salida:
                f.write(line + "\n")

# Función para cargar los procesos desde un archivo
def cargar_procesos_desde_archivo(archivo):
    lista_procesos = []
    with open(archivo, 'r') as f:
        for line in f:
            if line.startswith("#"):  # Ignorar comentarios
                continue
            etiqueta, bt, at, cola, prioridad = line.strip().split(";")
            lista_procesos.append(Proceso(etiqueta, int(bt), int(at), int(cola), int(prioridad)))
    return lista_procesos

