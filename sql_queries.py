# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ('''
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id     SERIAL PRIMARY KEY NOT NULL,
    start_time      bigint NOT NULL,
    user_id         bigint NOT NULL,
    level           varchar(16),
    song_id         varchar(64),
    artist_id       varchar(64),
    session_id      int,
    location        varchar(265),
    user_agent      varchar(256));
''')

user_table_create = ('''
CREATE TABLE IF NOT EXISTS users(
    user_id     bigint PRIMARY KEY NOT NULL,
    first_name  varchar(256),
    last_name   varchar(256),
    gender      varchar(8),
    level       varchar(16));
''')

song_table_create = ('''
CREATE TABLE IF NOT EXISTS songs(
    song_id     varchar(64) PRIMARY KEY NOT NULL,
    title       varchar(256),
    artist_id   varchar(64) NOT NULL,
    year        int,
    duration    float8);
''')

artist_table_create = ('''
CREATE TABLE IF NOT EXISTS artists
(
    artist_id   varchar(64) PRIMARY KEY  NOT NULL,
    name        varchar(256),
    location    varchar(256),
    latitude    float,
    longitude   float);
''')

time_table_create = ('''
CREATE TABLE IF NOT EXISTS time(
    start_time  bigint PRIMARY KEY NOT NULL,
    hour        int4,
    day         int4,
    week        int4,
    month       int4,
    year        int4,
    weekday     int4);
''')

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays 
(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users 
(user_id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) 
DO UPDATE
    SET level  = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs 
(song_id, title, artist_id, year, duration) 
VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists 
(artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) 
DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time
(start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) 
DO NOTHING
""")

# FIND SONGS
song_select = ("""
select s.song_id songid, s.artist_id artistid
from songs s inner join artists a on s.artist_id = a.artist_id
where s.title = %s and a.name = %s and s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]