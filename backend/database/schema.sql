DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS ratings;


CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE movies(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    release_date TEXT,
    runtime TEXT NOT NULL,
    plot TEXT,
    average_rating TEXT NOT NULL
);

CREATE TABLE ratings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES users(id),
    FOREIGN KEY (movie_id)
        REFERENCES movies(id),
    value INTEGER CHECK (value > 0 AND value <= 5),
    UNIQUE(user_id, movie_id)

);
