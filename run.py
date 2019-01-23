import os
from app import app
from app.models.database import DatabaseConnenction

db = DatabaseConnenction()


if __name__ == '__main__':
  db.create_tables()
  app.run()
