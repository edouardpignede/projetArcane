DROP TABLE IF EXISTS proprietaire;
DROP TABLE IF EXISTS appartement;
DROP TABLE IF EXISTS ville;

CREATE TABLE proprietaire (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT UNIQUE NOT NULL,
  age INTEGER,
  profession TEXT
);

CREATE TABLE appartement (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  proprietaire_id INTEGER NOT NULL,
  ville_id INTEGER NOT NULL,
  nom TEXT UNIQUE NOT NULL,
  description_appart TEXT,
  type_de_bien TEXT,
  nombre_de_chambres INTEGER,
  surface FLOAT,
  FOREIGN KEY (proprietaire_id) REFERENCES proprietaire (id),
  FOREIGN KEY (ville_id) REFERENCES ville (id)
);

CREATE TABLE ville (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    departement INTEGER,
    nombre_habitant INTEGER
);


INSERT INTO ville VALUES (1, 'Paris', 75, 2220445);
INSERT INTO ville VALUES (2, 'Bayonne', 64, 48178);
INSERT INTO ville VALUES (3, 'Meudon', 92, 44873);
INSERT INTO ville VALUES (4, 'Etretat', 76, 1398);

INSERT INTO proprietaire VALUES (1, 'François Martin', 24, 'intermitant du spectacle');
INSERT INTO proprietaire VALUES (2, 'Jean Dupont', 45, 'Couturier');
INSERT INTO proprietaire VALUES (3, 'Noëlle Denis', 38, 'Femme de ménage');
INSERT INTO proprietaire VALUES (4, 'Julien Franck', 38, 'PDG de Danone' );

INSERT INTO appartement VALUES (1, 1, 1, 'Le cairn', 'Grand appartement dans le centre', 'Appartement', 3, 60);
INSERT INTO appartement VALUES (2, 1, 1, 'A langlès', 'Studio en périphérie', 'Appartement', 1, 25);
INSERT INTO appartement VALUES (3, 3, 4, 'La clé des Champs', 'Maison avec jardin', 'Maison', 3, 150);
INSERT INTO appartement VALUES (4, 4, 2, 'Cesal', 'Grande maison', 'Maison', 5, 320);
INSERT INTO appartement VALUES (5, 2, 3, 'Loiselet', 'Appartement dans le centre', 'Appartement', 2, 90);