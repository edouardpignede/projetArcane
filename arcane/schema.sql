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
  appartement_id INTEGER NOT NULL,
  nom TEXT UNIQUE NOT NULL,
  description_appart TEXT,
  type_de_bien TEXT,
  ville TEXT,
  pieces TEXT,
  FOREIGN KEY (proprietaire_id) REFERENCES proprietaire (id),
  FOREIGN KEY (appartement_id) REFERENCES ville (id)
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