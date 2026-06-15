import asyncio
from app.db.session import engine
from app.models.db_models import Base

async def create_tables():
    print("Connecting to the database...")
    try:
        # This tells SQLAlchemy to look at our Base models and generate the tables directly
        async with engine.begin() as conn:
            print("Executing table creation...")
            await conn.run_sync(Base.metadata.create_all)
        print("✅ SUCCESS: All tables created successfully!")
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    asyncio.run(create_tables())