class Local:
    """
    classe Local (chque étudiant a une seule classe attiribuée)
    """

    def __init__(self, p_type_local="", p_numero_local="", p_lieu_local="", p_dimention_local="", p_nbr_places=""):
        """
        costructeur de la classe Local avec les parametres suivants:
        tupe_local: "Technique" ou "Normal"
        numero_local: composé d'une lettre suivi par un tiret suivi de 3 chiffres (A-123)
        lieu_local: Bloc A, B ou C
        dimension_local: Mesure en mètre carré, doit être un entier positif
        nbr_places: doit être un entier positif inferieur a 25
        """

        self._numero_local = p_numero_local  # Privé (A-123)
        self._mesure_local = p_dimention_local  # Privé (Entier positif)
        self._nbr_places = p_nbr_places  # Privé (Entier positif <25)
        self.type_local = p_type_local  # Public (Technique ou Normal)
        self.lieu_local = p_lieu_local  # Public (A, B, C)

    @property
    def Numero_local(self):
        return self._numero_local

    @Numero_local.setter
    def Numero_local(self, p_numero_local):
        if len(p_numero_local) == 5 and p_numero_local[0].isalpha() and p_numero_local[1] == "-" and p_numero_local[2:5].isnumeric():
            self._numero_local = p_numero_local

    @property
    def Mesure_local(self):
        return self._mesure_local

    @Mesure_local.setter
    def Mesure_local(self, p_dimention_local):
        if p_dimention_local.isnumeric():
            self._mesure_local = p_dimention_local

    @property
    def Nombre_places(self):
        return self._nbr_places

    @Nombre_places.setter
    def Nombre_places(self, p_nbr_places):
        if p_nbr_places.isnumeric() and len(p_nbr_places) <= 25:
            self._nbr_places = p_nbr_places

    # Methode magique
    def __str__(self):
        chaine = f"""
        Numéro du local :{self._numero_local}
        Mesure du local :{self._mesure_local}
        Nombre de places du local :{self._nbr_places}
        Type du local :{self.type_local}
        Lieu du local :Secteur {self.lieu_local} 
        """
