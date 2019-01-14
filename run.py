import os 
from app import create_app

environment = os.environ.get('IREPORTER_ENV', 'development')
app = create_app(environment)

if __name__ == '__main__':
  app.run()
