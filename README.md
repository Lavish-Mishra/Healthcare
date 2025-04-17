# 🏥 Django Healthcare Backend

This project is a secure healthcare backend system built with **Django**, **Django REST Framework**, **PostgreSQL**, and **JWT Authentication**. It allows users to register/login, manage patients and doctors, and map patients to doctors.

---

## 🚀 Features

- Custom user model using **email** for authentication
- JWT-based authentication with **SimpleJWT**
- CRUD APIs for:
  - **Patients**
  - **Doctors**
  - **Patient-Doctor Mappings**
- Secure access with token authentication
- PostgreSQL integration
- Environment-based configuration using `.env`

---

## 🔧 Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt
- python-decouple
- psycopg2-binary

---

## 📁 Project Structure

```bash
healthcare/ 
    ├── core/ # App for patients, doctors, mappings 
    ├── users/ # App for custom user & auth 
    ├── healthcare/ # Project settings 
    ├── manage.py 
    └── .env
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Lavish-Mishra/Healthcare.git
cd healthcare
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL Database

#### Create database and user:

```bash
CREATE DATABASE healthcare_db;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO your_db_user;
```

### 5. Configure .env

#### Create a .env file in the project root:

```bash
DEBUG=True
SECRET_KEY=your-secret-key

DB_NAME=healthcare_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

ALLOWED_HOSTS=127.0.0.1,localhost
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```
### 8. Start the Server

```bash
python manage.py runserver
```

---

## 🛠️ API Endpoints


🔐 Authentication

```bash
Method	Endpoint	Description
POST	/api/auth/register/	Register a user
POST	/api/auth/login/	Login and get JWT
POST	/api/auth/token/refresh/	Refresh token
```

🧑‍⚕️ Patients

```bash
Method	Endpoint	Description
POST	/api/patients/	Create a patient
GET	/api/patients/	List all your patients
GET	/api/patients/<id>/	Get patient details
PUT	/api/patients/<id>/	Update a patient
DELETE	/api/patients/<id>/	Delete a patient
```

👨‍⚕️ Doctors

```bash
Method	Endpoint	Description
POST	/api/doctors/	Add a doctor
GET	/api/doctors/	List all doctors
GET	/api/doctors/<id>/	Get doctor info
PUT	/api/doctors/<id>/	Update doctor
DELETE	/api/doctors/<id>/	Delete doctor
```

🔁 Patient-Doctor Mappings

```bash
Method	Endpoint	Description
POST	/api/mappings/	Assign a doctor to a patient
GET	/api/mappings/	List all mappings
GET	/api/mappings/<patient_id>/doctors/	Get all doctors assigned to a patient
DELETE	/api/mappings/<id>/	Remove a doctor from a patient
```
