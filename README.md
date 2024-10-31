
# DRFjwt

DRFjwt is a framework designed for rapidly launching new Django REST Framework projects with JWT authentication enabled using Djoser. It includes essential features like a custom user model, user management (login/logout/signup), and more for quick project setup.

![logo](https://github.com/anomalous254/drf-jwt/blob/main/logo.jpg)

## Features

- **Django 5.1**, **Django REST Framework 3.12**, and **Python 3.8** support
- **Custom user model** for extended user profiles
- **JWT-based authentication** for secure API access
- **Automatic addition of access and refresh tokens to cookies** for seamless authentication
- User management: **signup**, **login**, and **logout** endpoints
- **Djoser user endpoints** via `djoser` — check the [Djoser documentation](https://djoser.readthedocs.io/en/latest/index.html) for details
- **API documentation** available at http://127.0.0.1:8000`/redoc/` for easy access to API endpoints
- **virtualenv** for virtual environment management

## Prerequisites

Ensure `virtualenv` is installed on your computer. You can install it with:
```bash
pip install virtualenv
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anomalous254/drf-jwt.git
   cd drf-jwt
   ```

2. **Set up a virtual environment**:
   ```bash
   virtualenv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install project dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## Additional Documentation

For more details on user authentication and endpoint setup, check the [Djoser documentation](https://djoser.readthedocs.io/en/latest/index.html).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
