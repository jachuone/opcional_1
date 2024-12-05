# Clase Proceso
class Proceso:
    def __init__(self, etiqueta, bt, at, cola, prioridad):
        self.etiqueta = etiqueta  # Identificación del proceso
        self.bt = bt  # Burst time
        self.at = at  # Arrival time
        self.cola = cola  # Cola a la que pertenece
        self.prioridad = prioridad  # Prioridad en la cola
        self.rt = -1  # Tiempo de respuesta
        self.ct = -1  # Tiempo de completado
        self.wt = -1  # Tiempo de espera
        self.tat = -1  # Turnaround time
        self.remanente_bt = bt  # Ráfaga restante

        
