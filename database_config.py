import os
import psycopg2
import redis

def get_postgres_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("POSTGRES_DB", "your_database_name"),
        user=os.getenv("POSTGRES_USER", "your_username"),
        password=os.getenv("POSTGRES_PASSWORD", "your_password")
    )

def get_redis_connection():
    return redis.StrictRedis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        decode_responses=True
    )

if __name__ == "__main__":
    try:
        conn = get_postgres_connection()
        print("Connected to PostgreSQL")
        conn.close()
    except Exception as e:
        print("PostgreSQL connection error:", e)

    try:
        r = get_redis_connection()
        r.ping()
        print("Connected to Redis")
    except Exception as e:
        print("Redis connection error:", e)