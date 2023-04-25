from classLocal import *


class LocalTechnique (Local):
    """
    Classe enfant de la classe Local
    a pour attributs personnels :
    Projecteur = PUBLIC, (oui ou non)
    Marque d'ordinateurs = PRIVÉ (string de longueur 25)
    Nombre d'ordinateurs
    """
    def __init__(self, p_type_local="", p_numero_local="", p_lieu_local="", p_dimention_local="", p_nbr_places="",
                 p_nb_ordinateurs="", p_marque_ordi="", p_projecteur=""):
        """
        Constructeur de la classe Local technique avec ses attributs personnels
        :param p_nb_ordinateurs: PRIVÉ = doit être un int d'une valeur inférieure ou égale a 25
        :param p_marque_ordi: PRIVÉ = doit être composé de lettres et d'une longueur maximale de 25
        :param p_projecteur: PUBLIC = oui ou non (combo box)
        """
        Local.__init__(self, p_type_local="", p_numero_local="", p_lieu_local="", p_dimention_local="", p_nbr_places="")
        """
        Classe mère de la classe LocalTechnique
        """
        self._marque_ordi = p_marque_ordi
        self._nb_ordi = p_nb_ordinateurs
        self.Projecteur = p_projecteur

    @property
    def marque(self):
        return self._marque_ordi

    @marque.setter
    def marque(self, p_marque_ordi):
        if len(p_marque_ordi) < 100:
            self._marque_ordi = p_marque_ordi

    @property
    def nombre_ordi(self):
        return self._nb_ordi

    @nombre_ordi.setter
    def nombre_ordi(self, p_nb_ordinateurs):
        if p_nb_ordinateurs.isnumeric() and 0 < p_nb_ordinateurs < 25:
            self._nb_ordi = p_nb_ordinateurs

    # Méthode magique
    def __str__(self):
        """
        Fonction magique __str__
        :return: La chaine à afficher
        """
        chaine = f"""
        La marque des ordinateurs de la classe: {self._marque_ordi}
        Le nombre d'ordinateurs de la classe :  {self._nb_ordi}
        La classe contient un ordinateur : {self.Projecteur}
                """
        return chaine
