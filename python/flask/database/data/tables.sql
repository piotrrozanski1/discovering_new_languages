CREATE DATABASE flask_db;
CREATE USER sammy WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE flask_db TO sammy;
ALTER DATABASE flask_db OWNER TO sammy;
