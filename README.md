# AI-project

Ce projet propose l'implementation d'un assitant AI, développé avec le framework Langchain. L'assitant peut réaliser différentes actions liées à la gestion d'une base de données d'utilisateurs.

### Prérequis
- Avant de commencer, assurez-vous d'avoir les éléments suivants installés dans votre environnement virtuel (voir ci-dessous pour sa création) :
  - Python 3.8 au minimum, version utilisé : Python 3.12.3
  - openai
  - pymongo
  - python-dotenv
  - langchain-openai
  - langchain-community


- Il vous faudra aussi créer un compte sur MongoDB Atlas (https://account.mongodb.com/account/register). Une option gratuite est disponible.
- Une clé API OpenAI est nécessaire.

### Créez un environnement virtuel :
Avant d'éxécuter la ligne de code suivante, créer un dossier qui contiendra votre environnement et le reste des fichiers.

python -m venv venv

### Activez l'environnement virtuel :
Sur Windows :
  venv\Scripts\activate

Sur Linux/MacOS :
  source venv/bin/activate

### Installez les dépendances requises :
  pip install -r requirements.txt

### Utilisation
Lancer le script : python main.py 

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

## Configuration
Vous devez modifiez le fichier settings.py, dans le dossier config/ en ajoutant :
- votre clé API,
- votre chaine de connexion pour votre base de données mongoDB
- le nom de votre base de données.

## Contribution
Plusieurs fonctions sont encore en développement :

- Update_tool est encore en phase de test.
  
- Les prompts des différentes templates, notamment pour update_tool et delete_tool, nécessitent des améliorations.

- L'assistant permettant d'extraire les données à mettre à jour est également en cours de développement.
