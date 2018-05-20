DROP TABLE IF EXISTS proprietaire;
DROP TABLE IF EXISTS appartement;
DROP TABLE IF EXISTS ville;

CREATE TABLE proprietaire (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT UNIQUE NOT NULL,
  age INTEGER,
  profession TEXT,
  password TEXT NOT NULL
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
    departement TEXT,
    nombre_habitant INTEGER
);