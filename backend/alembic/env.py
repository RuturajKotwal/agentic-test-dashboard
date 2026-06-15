# ... other imports ...
import asyncio
from sqlalchemy.ext.asyncio import async_engine_from_config
from app.db.session import Base
from app.models.db_models import DBTestRun # Import the model so Alembic sees it

# 1. Update target_metadata
target_metadata = Base.metadata

# ... scroll down to the run_migrations_online function ...

# 2. Because we are using an async driver, Alembic needs an async execution wrapper.
# Replace the ENTIRE run_migrations_online function with this:

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations():
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    # Force Alembic to use our .env URL
    config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))
    
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    asyncio.run(run_async_migrations())