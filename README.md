# projetArcane

## Installation
Pour executer le programme, il vous suffit d'installer Pipenv, puis executer: 
`pipenv install`
Puis rentrer:
`export FLASK_APP=arcane`
et enfin:
`flask init-db` et `flask run`pour lancer l'application.

## Guide de l'API REST
Les requêtes ont été testé avec Postman
- localhost:5000/appartements  possède une requête GET et une requête POST, qui permettent à l'utilisateur d'afficher ou d'ajouter un élément à  la base de donnée des différents appartements.
- localhost:5000/appartement/id  possède des requêtes GET, PUT et DELETE, qui permettent à l'utilistaeur d'afficher, de modifier ou de supprimer l'élément id de la base de donnée des appartements.
- localhost:5000/proprietaires  possède une requête GET et une requête POST, qui permettent à l'utilisateur d'afficher ou d'ajouter un élément à  la base de donnée des différents proprietaires
- localhost:5000/proprietaire/id   possède des requêtes GET, PUT et DELETE, qui permettent à l'utilistaeur d'afficher, de modifier ou de supprimer l'élément id de la base de donnée des proprietaires.
- localhost:5000/ville/<ville_id>/appartements  possède une requête GET qui permet d'afficher les différents appartements de la ville <ville_id>
