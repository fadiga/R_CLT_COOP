SAVE = "Enregistrer"
SAVE_AND_CONTINNUES = "Enregistrer et continuer"
#
DATE_DEMANTE = "Date de la demande *"
DENOMINATION_S_SC = "Dénomination Sociale de la société coopérative *"
NOM_COMMERCIAL = "Nom Commercial / Sigle / Enseigne *"
DATE_CREATION_SC = "Date de création de la société coopérative *"
ACTIVITES_E = "Activités exercées *"
FILIERE = "Filière *"
FORME_SC = "Forme de la société coopérative *"
# Capital Social Initial
MONTANT_PART_S = "Montant de la part sociale *"
MONTANT_APPORTS_NUM = "Montant apports en numéraire *"
MONTANT_APPORTS_NAT = "Montant apports en nature *"
MONTANT_APPORTS_INDU = "Montant apports en industrie *"
MONTANT_CAPITAL_SI = "Montant Capital Social Initial *"

ADRESSE_SS = "Adresse du siège social *"
REGION = "Région"
CERCLE = "Cercle"
COMMUNE = "Commune *"
VFQ = "Village/Fraction/Quartier *"
RUE = "Rue"
PORTE = "Porte (n°)"
TEL = "Tel *"
TEL2 = "Tel 2"
BP = "BP"
EMAIL = "E-mail"
DUREE_STATUTAIRE_SC = u"Durée statutaire de la société coopérative (ans) *"

CSS = """
    QGroupBox {
            background-color: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E0E0E0, stop: 1 #FFFFFF);
            border: 2px solid gray;
            border-radius: 5px;
            margin-top: 1ex; /* leave space at the top for the title */
            padding-top: 60px;
            padding-left: 100px;
        }
        QGroupBox::title {
            /*margin-bottom: 10em;  leave space at the top for the title */
            subcontrol-origin: margin;
            background-color: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E0E0E0, stop: 1 #FFFFFF);
            /*subcontrol-origin: margin;*/
            subcontrol-position: top left;
            border-top-left-radius: 15px;
            border-bottom-right-radius: 15px;
            border-bottom-right-radius: 15px;
            padding: 5px 20px;
            background-color: #63707d;
            color: rgb(255, 255, 255);
        }"""

CSS_CENTER = """
    QGroupBox {
            background-color: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E0E0E0, stop: 1 #FFFFFF);
            border: 2px solid gray;
            border-radius: 5px;
            margin-top: 1ex; /* leave space at the top for the title */
            padding: 50px 50px;
        }
        QGroupBox::title {
            /*margin-bottom: 10em;  leave space at the top for the title */
            subcontrol-origin: margin;
            background-color: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E0E0E0, stop: 1 #FFFFFF);
            /*subcontrol-origin: margin;*/
            subcontrol-position: top center;
            border-top-left-radius: 15px;
            border-bottom-right-radius: 15px;
            border-bottom-right-radius: 15px;
            padding: 15px 50px;
            background-color: #63707d;
            color: rgb(255, 255, 255);
        }"""
