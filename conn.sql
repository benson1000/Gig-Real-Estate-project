CREATE DATABASE gig;


--define a new sequence generator
CREATE SEQUENCE users_seq;

CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY DEFAULT NEXTVAL('users_seq'),
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL UNIQUE
);

--define a new sequence contact
CREATE SEQUENCE contact_seq;

CREATE TABLE contact(
    id INTEGER NOT NULL PRIMARY KEY DEFAULT NEXTVAL('contact_seq'),
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL
);
