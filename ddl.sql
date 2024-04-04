CREATE DATABASE IF NOT EXISTS loscuentos;
USE loscuentos;

CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY,
    username VARCHAR(14) NOT NULL,
    email VARCHAR(54) NOT NULL,
    password VARCHAR(54) NOT NULL,
    bio VARCHAR(150),
    created_on DATE NOT NULL,
    image_path TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS social_links (
    user_id BIGINT NOT NULL,
    name VARCHAR(24) NOT NULL,
    PRIMARY KEY (user_id, name),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS stories (
    story_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(84) NOT NULL,
    created_on DATE NOT NULL,
    author_id BIGINT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS favorites (
    user_id BIGINT NOT NULL,
    story_id INT NOT NULL,
    PRIMARY KEY (user_id, story_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (story_id) REFERENCES stories(story_id)
);

CREATE TABLE IF NOT EXISTS chapters (
    chapter_id INT PRIMARY KEY AUTO_INCREMENT,
    content VARCHAR(1500) NOT NULL,
    created_on DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS interactions (
    user_id BIGINT NOT NULL,
    chapter_id INT NOT NULL,
    action INT NOT NULL,
    PRIMARY KEY (user_id, chapter_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (chapter_id) REFERENCES chapters(chapter_id)
);

CREATE TABLE IF NOT EXISTS comments (
    comment_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    chapter_id INT NOT NULL,
    content varchar(250) NOT NULL,
    parent_comment_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (chapter_id) REFERENCES chapters(chapter_id)
);

CREATE TABLE IF NOT EXISTS tags (
    tag_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(14)
);

CREATE TABLE IF NOT EXISTS story_tags (
    tag_id INT NOT NULL,
    story_id INT NOT NULL,
    PRIMARY KEY (tag_id, story_id),
    FOREIGN KEY (tag_id) REFERENCES tags (tag_id),
    FOREIGN KEY (story_id) REFERENCES stories (story_id)
);

CREATE TABLE IF NOT EXISTS favorite_tags (
    user_id BIGINT NOT NULL,
    tag_id INT NOT NULL,
    score INT NOT NULL,
    PRIMARY KEY (user_id, tag_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);
