CREATE SCHEMA survey;

CREATE TABLE survey.survey (
    name VARCHAR(32) PRIMARY KEY,
    favorite_color VARCHAR(32),
    favorite_pet VARCHAR(8)
);

CREATE USER survey WITH PASSWORD 'my_secret_password';

GRANT USAGE ON SCHEMA survey TO survey;
GRANT INSERT ON TABLE survey.survey TO survey;