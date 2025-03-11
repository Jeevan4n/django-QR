# Django-QR

Django-QR is a web app for generating and managing QR codes using Django and Django REST Framework.

## Features
- Generate QR codes from text or URLs.
- REST API support.
- Stores QR codes in a database.
- Uses Pillow for image processing.
- Serves static files via Whitenoise.

## Tech Stack
- **Backend**: Django 5.1.7, Django REST Framework
- **Database**: SQLite (default), configurable for PostgreSQL/MySQL
- **Frontend**: Django Templates & Bootstrap
- **Deployment**: Hosted on Render

## Installation
**Prerequisites**: Python 3.11+, pip

1. **Clone the Repository**
   ```sh
   git clone https://github.com/Jeevan4n/django-QR.git
   cd django-QR
   ```
2. **Setup Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows: `venv\Scripts\activate`
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply Migrations & Run Server**
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```
   Access at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Deployment on Render
Ensure `gunicorn` is installed and added to `requirements.txt`, then push changes:
```sh
git add requirements.txt
git commit -m "Added Gunicorn for production"
git push origin main
```
Set Render Start Command:
```sh
gunicorn django_QR.wsgi:application
```
Redeploy with "Clear Build Cache & Deploy."

## API Endpoints
- **Generate QR Code**: `POST /api/generate_qr/`  
  Payload: `{ "data": "https://example.com" }`
- **Get All QR Codes**: `GET /api/qrcodes/`

## Contributing
1. Fork & create a branch (`git checkout -b feature-branch`)
2. Commit & push (`git commit -m "Add feature"`)
3. Open a Pull Request

## License
MIT License
