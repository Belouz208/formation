import importlib
import pkgutil
import os


def document_library(lib_name):
    try:
        # Importer la bibliothèque principale
        lib = importlib.import_module(lib_name)
    except ModuleNotFoundError:
        print(f"La bibliothèque '{lib_name}' est introuvable.")
        return

    # Créer le dossier BIBLO_OBJECTS s'il n'existe pas
    output_folder = "BIBLO_OBJECTS"
    os.makedirs(output_folder, exist_ok=True)

    # Nom du fichier de sortie
    filename = os.path.join(output_folder, f"{lib_name}_documentation.txt")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Documentation des sous-modules, classes et fonctions de '{lib_name}'\n\n")

        # Fonction pour documenter les sous-modules et classes
        def document_module(module, module_name=""):
            # Vérifier si le module est un package et possède __path__
            if hasattr(module, '__path__'):
                for submodule_info in pkgutil.walk_packages(module.__path__, prefix=module.__name__ + "."):
                    submodule_name = submodule_info.name
                    file.write(f"Module: {submodule_name}\n")

                    # Importer le sous-module
                    try:
                        submodule = importlib.import_module(submodule_name)

                        # Énumérer les classes et fonctions dans chaque sous-module
                        for name, obj in vars(submodule).items():
                            if isinstance(obj, type):  # Classes
                                file.write(f"  Classe: {name}\n")
                            elif callable(obj):  # Fonctions ou méthodes
                                file.write(f"  Fonction: {name}\n")
                    except (ImportError, AttributeError, Exception) as e:
                        # Enregistrer les erreurs sans arrêter le script
                        file.write(f"  Impossible d'importer le sous-module: {submodule_name} - Erreur: {e}\n")
            else:
                # Pour les modules sans __path__, lister simplement leurs classes et fonctions
                for name, obj in vars(module).items():
                    if isinstance(obj, type):
                        file.write(f"  Classe: {name}\n")
                    elif callable(obj):
                        file.write(f"  Fonction: {name}\n")

        # Documenter le module principal et ses sous-modules
        document_module(lib)

    print(f"La documentation pour '{lib_name}' a été enregistrée dans le fichier '{filename}'.")


# Exécution du script
if __name__ == "__main__":
    library_name = input("Entrez le nom de la bibliothèque: ")
    document_library(library_name)
