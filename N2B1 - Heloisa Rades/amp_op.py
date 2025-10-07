
class Calculos:
    def __init__(self):
        pass
    
    @staticmethod
    def calcular_vout(vin, rf, rin):
        return vin * (1 + (rf / rin))

    @staticmethod
    def calcular_vin(vout, rf, rin):
        return vout / (1 + (rf / rin))
    
    @staticmethod
    def calcular_res(vin, vout, rf = None, rin = None):
        if rf is None and rin is None:
            return None
        if rf is None:
            return rin * ((vout / vin) - 1)
        elif rin is None:
            return rf / ((vout / vin) - 1)
        
if __name__ == "__main__":
    pass
