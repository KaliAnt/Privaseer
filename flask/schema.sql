drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    name varchar(255),
    timestamp integer NOT NULL,
    location integer NOT NULL
    
);