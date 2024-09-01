# AI-project

Ce projet propose l'implementation d'un assitant AI, développé avec le framework Langchain. L'assitant peut réaliser des actions liées à la gestion d'une base de données d'utilisateurs.

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés :
- Python 3.8 au minimum, version utilisé : Python 3.12.3
- openai
- pymongo
- python-dotenv
- langchain-openai
- langchain-community


# Créez un environnement virtuel :
Avant d'éxécuter la ligne de code suivante, créer un dossier qui contiendra votre environnement et le reste des fichiers.

python -m venv venv

## Activez l'environnement virtuel :
Sur Windows :
  venv\Scripts\activate

Sur Linux/MacOS :
  source venv/bin/activate

## Installez les dépendances requises :
  pip install -r requirements.txt

## Utilisation
Intéragir avec l'assistant : python main.py

## Structure du Projet
- main.py: Contient le script principal qui gère l'assistant AI.

- config/settings.py: Dossier où les variables d'environnement sont générées.

- database/user_handler.py: Fichier permettant de réaliser des opérations CRUD sur mongoDB.

- handlers/account_handler.py: Fichier permettant la gestion de compte utilisateur. (A un niveau plus haut que pour user_hanlder.py)

- utils/:  Dossier contenant les modules utilitaires, tels que la gestion de la mémoire et l'exécution des agents.

  - utils/common_imports.py : Dossier contenant les modules utilitaires, tels que la gestion de la mémoire et l'exécution des agents.
  
  - utils/db_agent_manager.py :  Gère l'agent et ses outils.
  
  - utils/intent_analysis.py : Propose permettant de déterminer l'intention de l'utilisateur à partir de son message.
  
  - utils/parser_tools.py : Fournit des outils pour la gestion et la vérification d'informations.
  
  - utils/user_info_parser.py : Propose un premier assistant qui permet d'extraire depuis le message utilisateur ses informations personnelles et un second en dévéloppement censé déterminer du message utilisateur les informations qu'ils souhaitent mettre à jour.

### Contribution
Plusieurs fonctions sont encore en développement :

- Update_tool est encore en phase de test.
  
- Les prompts des différentes templates, notamment pour update_tool et delete_tool, nécessitent des améliorations.

- L'assistant permettant d'extraire les données à mettre à jour est également en cours de développement.
