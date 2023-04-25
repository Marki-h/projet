import json


class Etudiant:
    """
    Classe Etudiant
    """

    def __init__(self, p_numero=0, p_nom="", p_programme="", p_naiss=""):
        """
        Contructeur de la classe Etudiant
        """
        self._numero = p_numero
        self._nom = p_nom
        self.Programme = p_programme  # Attribut public - Pas de validaion - Pas de proproété
        self._naissance = p_naiss

    @property
    def Numero(self):
        return self._numero

    @Numero.setter
    def Numero(self, p_numero):
        if p_numero.isnumeric() and len(p_numero) == 7:
            self._numero = p_numero

    @property
    def Nom(self):
        return self._nom

    @Nom.setter
    def Nom(self, p_nom):
        if p_nom.isalpha():
            self._nom = p_nom

    @property
    def Programme(self):
        return self._programme

    @Programme.setter
    def Programme(self, p_programme):
        self._programme = p_programme

    @property
    def Naissance(self):
        return self._naissance

    @Naissance.setter
    def Naissance(self, p_naissance):
        if self.age(p_naissance) >= 18:
            self._naissance = p_naissance

    def age(self, p_naissance):
        import datetime
        today = datetime.date.today()
        return today.year - p_naissance.year() - ((today.month, today.day) < (p_naissance.month(), p_naissance.day()))

    def serialiser(self, p_fichier):
        """
        Methode permettant de sérialiser un objet de la classe Etudiant
        :param p_fichier: Le nom du fichier qui contiendra l'objet serialisé
        """
        self.__dict__["_Etudiant__date_naiss"] = str(self.Naissance.year()) + "-" + str(self.Naissance.month()) + "-" + \
                                                 str(self.Naissance.day())

        # Validation + Gestion d'erreurs lors de l'ouverture du fichier
        try:
            with open(p_fichier, "w") as fichier:
                try:
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2

    def deserialiser(self, p_fichier):
        """
        Méthode permettant de déserialiser un objet de la clase étudiant
        :param p_fichier: Le nom du fichier qui contient l'objet sérialisé
        """

        with open(p_fichier, "r") as fichier:
            self.__dict__ = json.load(fichier)

    def __str__(self):
        chaine = "*" * 10 + f"\n" + f"Le numéro de l'étudiant est : {self._numero}" + f"\n" + \
                 f"Le nom de l'étudiant est : {self._nom}" + f"\n" + \
                 f"Le programme de l'étudiant est : {self._programme}" + f"\n" + \
                 f"La date de naissance de l'étudiant est : {str(self._naissance.day())}/" + \
                 f"{str(self._naissance.month())}/{str(self._naissance.year())}" + f"\n" + "*" * 10
        return chaine
