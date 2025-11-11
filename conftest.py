# Ce fichier conftest.py ajoute automatiquement la racine du projet au chemin d'import (sys.path)
# afin que les fichiers de test puissent importer les modules métier situés à l'extérieur du dossier tests.

import sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
