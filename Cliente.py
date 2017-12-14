class Cliente:
    """
    Cliente is the owner of an account,
    an account cannot be created without a cliente
    """

    def __init__(self, nome):
        self.__nome = nome
       
    @property   
    def nome(self):
        return self.__nome.title()

