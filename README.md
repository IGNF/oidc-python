# keycloak-auth

Exemple d'une implémentation de l'authentification OpenID-Connect Keycloak dans un programme python (par exemple CLI, plugin qgis etc.)

Dans ce dépôt, il y a :

-   un mini-module en python qui implémente la connexion et la déconnexion à Keycloak que vous pouvez tester en exécutant la commande suivante :

```bash
python ign_keycloak/example.py
```

-   un plugin qgis bidon pour tester le module python en copiant le dossier `keycloak_auth_plugin` dans `C:\Users\<USERNAME>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`

## Installation

Consulter les dépendances python dans le fichier [./environment.yml](./environment.yml)

Créer ou mettre à jour l'environnement virtuel python (conda-like) :

```sh
micromamba env create --file "./environment.yml"
```

Activer l'environnement virtuel python :

```sh
micromamba activate keycloak
```

Supprimer l'environnement virtuel :

```sh
micromamba env remove --name keycloak
```

> https://iq.opengenus.org/delete-conda-environment/

Export environnement virtuel :

```sh
echo "# Export date:" $(date) > environment.export.yml && micromamba env export >> environment.export.yml
```

> Aide mémoire commandes conda : https://www.machinelearningplus.com/deployment/conda-create-environment-and-everything-you-need-to-know-to-manage-conda-virtual-environment/

Copier la librairie ign_keycloak dans le projet du plugin qgis :

```sh
cp ign_keycloak/ign_keycloak -R keycloak_auth_plugin/lib/ && rm -rf keycloak_auth_plugin/lib/ign_keycloak/__pycache__/
```
