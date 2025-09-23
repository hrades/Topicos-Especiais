class LeiDeOhm:
    def __init__(self):
        pass

    @staticmethod
    def primeira_lei(tensao=None, corrente=None, resistencia=None):
        try:
            if tensao==None:
                return corrente*resistencia
            elif corrente==None:
                return tensao/resistencia
            elif resistencia==None:
                return tensao/corrente
        except Exception as e:
            return e
        
    @staticmethod
    def segunda_lei(resistencia=None):
        pass