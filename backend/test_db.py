import asyncio
from sqlalchemy import text
from app.db.session import engine

async def test_connection():
    print("Attempting to connect to MySQL...")
    try:
        # We try to acquire a connection from the engine
        async with engine.begin() as conn:
            # Run a simple query that all SQL databases understand
            result = await conn.execute(text("SELECT 1"))
            print("✅ SUCCESS: The database is connected and responding!")
            
    except Exception as e:
        print("\n❌ FAILURE: Could not connect to the database.")
        print(f"Error details: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())