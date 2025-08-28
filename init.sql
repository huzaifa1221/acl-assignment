-- Create tables
CREATE TABLE IF NOT EXISTS mytable (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS othertable (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO mytable (name) VALUES
('Alice'),
('Bob');

INSERT INTO othertable (name) VALUES
('Charlie'),
('Diana');