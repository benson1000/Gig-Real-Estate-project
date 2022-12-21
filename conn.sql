CREATE DATABASE gig;


--define a new sequence generator
CREATE SEQUENCE users_seq;

CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY DEFAULT NEXTVAL('users_seq'),
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL UNIQUE
);
