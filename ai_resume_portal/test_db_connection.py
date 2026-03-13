import psycopg2
from psycopg2 import OperationalError

def test_database_connection():
    """Test connection to Render PostgreSQL database"""
    
    # Your Render database credentials
    db_config = {
        'dbname': 'aidb_t5fe',
        'user': 'aidb_t5fe_user',
        'password': 'yw1WOk7SlwrCJ6yRpjo7ALX3MLpu7cDN',
        'host': 'dpg-d6oqp27kijhs73aup0j0-a.oregon-postgres.render.com',
        'port': '5432'
    }
    
    print("Testing Render PostgreSQL Database Connection...")
    print(f"Host: {db_config['host']}")
    print(f"Database: {db_config['dbname']}")
    print(f"User: {db_config['user']}")
    print("-" * 60)
    
    try:
        # Attempt to connect
        connection = psycopg2.connect(**db_config)
        
        # Create a cursor
        cursor = connection.cursor()
        
        # Execute a test query
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        
        print("[SUCCESS] CONNECTION SUCCESSFUL!")
        print(f"PostgreSQL Version: {db_version[0]}")
        
        # Get database size
        cursor.execute("""
            SELECT pg_size_pretty(pg_database_size(current_database())) as size;
        """)
        db_size = cursor.fetchone()
        print(f"Database Size: {db_size[0]}")
        
        # List existing tables
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        tables = cursor.fetchall()
        
        if tables:
            print(f"\nExisting Tables ({len(tables)}):")
            for table in tables:
                print(f"  - {table[0]}")
        else:
            print("\n[WARNING] No tables found (database is empty - migrations needed)")
        
        # Close cursor and connection
        cursor.close()
        connection.close()
        
        print("\n" + "=" * 60)
        print("DATABASE IS READY FOR DJANGO!")
        print("=" * 60)
        return True
        
    except OperationalError as e:
        print("[FAILED] CONNECTION FAILED!")
        print(f"Error: {e}")
        return False
    except Exception as e:
        print("[ERROR] UNEXPECTED ERROR!")
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_database_connection()
