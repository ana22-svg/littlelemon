Little Lemon Backend API

Setup:
1. Create a virtual environment and install dependencies:
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
2. Run migrations:
   python manage.py migrate
3. Start the server:
   python manage.py runserver

Database:
Set MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, and MYSQL_PORT to use
MySQL. Without MYSQL_DATABASE, local development uses SQLite.

API paths for peer testing:
GET    /api/menu/
GET    /api/menu/<id>/
POST   /api/menu/                 (Token authentication required)
PUT    /api/menu/<id>/            (Token authentication required)
DELETE /api/menu/<id>/            (Token authentication required)
POST   /api/registration/
POST   /api/login/
GET    /api/bookings/             (Token authentication required)
POST   /api/bookings/             (Token authentication required)
PUT    /api/bookings/<id>/        (Token authentication required)
DELETE /api/bookings/<id>/        (Token authentication required)

Send the token as:
Authorization: Token <token>

Run tests with:
python manage.py test
