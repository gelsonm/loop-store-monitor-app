import psycopg2

conn = psycopg2.connect(
    dbname="loop_store_monitor",
    user="demouser",
    password="pass123",
    host="localhost"
)

cur = conn.cursor()

# Create table for store status data
cur.execute('''
    CREATE TABLE store_status (
        store_id VARCHAR(50) NOT NULL,
        timestamp_utc TIMESTAMP NOT NULL,
        status VARCHAR(10),
        PRIMARY KEY (store_id, timestamp_utc)
    );
''')

# Create table for store business hours data
cur.execute('''
    CREATE TABLE store_hours (
        id SERIAL PRIMARY KEY,
        store_id VARCHAR(50) NOT NULL,
        day_of_week INTEGER NOT NULL,
        start_time_local TIME WITHOUT TIME ZONE NOT NULL,
        end_time_local TIME WITHOUT TIME ZONE NOT NULL,
        FOREIGN KEY(store_id, timestamp_utc) REFERENCES store_status (store_id, timestamp_utc)
    );
''')

cur.execute('''
    CREATE TABLE store_hours (
        id SERIAL PRIMARY KEY,
        store_id VARCHAR(50) NOT NULL,
        day_of_week INTEGER NOT NULL,
        start_time_local TIME WITHOUT TIME ZONE NOT NULL,
        end_time_local TIME WITHOUT TIME ZONE NOT NULL,
        FOREIGN KEY(store_id, timestamp_utc) REFERENCES store_status (store_id, timestamp_utc)
    );
''')

# Create table for store timezones data
cur.execute('''
    CREATE TABLE store_timezones (
        store_id VARCHAR(50) PRIMARY KEY,
        timezone_str VARCHAR(50) NOT NULL DEFAULT 'America/Chicago'
    );
''')


conn.commit()

cur.close()
conn.close()
