
# Clase Cola
class Cola:
    def __init__(self, politica, quantum=None):
        self.politica = politica  # Tipo de política RR, SJF, STCF
        self.procesos = []  # Lista de procesos en la cola
        self.quantum = quantum  # Si es RR, tamaño del quantum

    def agregar_proceso(self, proceso):
        self.procesos.append(proceso)

    def ordenar(self):
        if self.politica == 'SJF':
            # Ordenar por Burst time (BT)
            self.procesos.sort(key=lambda p: p.bt)
        elif self.politica == 'STCF':
            # Ordenar por Ráfaga restante (menor primero)
            self.procesos.sort(key=lambda p: p.remanente_bt)
        elif self.politica.startswith('RR'):
            # Round Robin: No se necesita ordenar
            pass

    def obtener_siguiente(self):
        if self.politica == 'RR':
            return self.procesos.pop(0)  # Round Robin, el primer proceso
        elif self.politica == 'SJF' or self.politica == 'STCF':
            return self.procesos.pop(0)  # SJF/STCF, el proceso con el menor BT/tiempo restante

    def esta_vacia(self):
        return len(self.procesos) == 0
    

    