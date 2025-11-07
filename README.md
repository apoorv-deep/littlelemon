# Little Lemon — Django Restaurant Booking

A small Django app (coursera project) that demonstrates a simple booking system for a restaurant. It includes:

## API Endpoints

- **/bookings**  (GET)         - List bookings for a date. Example: /bookings?date=2025-11-10
- **/bookings**  (POST)        - Create a booking. JSON body: {"first_name":"Alice","reservation_date":"YYYY-MM-DD","reservation_slot":12}
- **/book/**     (GET/HTML)     - Booking form (UI) that posts to /bookings via fetch()
- **/reservations/** (GET/HTML) - Page that shows all bookings (JSON rendered in page)

## Notes
- The main API endpoint for automated testing is /bookings (GET and POST).
- Use application/json for POST requests.
- If a slot is already booked for a date, the POST will return an error response.

## Project Setup Steps

Follow these steps to set up the project:

1. **Clone the repository**
	```sh
	git clone https://github.com/apoorv-deep/littlelemon.git
	cd littlelemon
	```

2. **Create and configure `.env` file**
	- Copy `.env.example` to `.env` (if available) and set your environment variables.
	- Example:
	  ```sh
	  cp .env.example .env
	  # Edit .env and set your values
	  ```

3. **Install dependencies**
	```sh
	pip install -r requirements.txt
	```

4. **Make migrations**
	```sh
	python manage.py makemigrations
	```

5. **Apply migrations**
	```sh
	python manage.py migrate
	```

6. **Run the development server**
	```sh
	python manage.py runserver
	```

## API (DRF) and Authentication

This project includes optional Django REST Framework (DRF) serializers and viewsets for the `Menu` and `Booking` models and Djoser-powered authentication routes.

- API root for viewsets (registered under `/api/`):
	- `/api/menu/`         - Menu list and detail endpoints (GET/POST/PUT/DELETE)
	- `/api/bookings/`     - Booking list and detail endpoints (GET/POST/PUT/DELETE)

- Authentication (Djoser):
	- `/auth/users/`            - Djoser user registration endpoints
	- `/auth/token/login/`      - Obtain auth token (if `rest_framework.authtoken` is installed)

Notes to enable token auth

1. Install required packages if you haven't already:
	 ```powershell
	 pip install djangorestframework djoser djangorestframework-authtoken
	 ```

2. Add `'rest_framework'`, `'rest_framework.authtoken'` and `'djoser'` to `INSTALLED_APPS` in `littlelemon/settings.py` (the project already includes `rest_framework` and `djoser` in `INSTALLED_APPS`; add `rest_framework.authtoken` if you want token endpoints).

3. Run migrations to create the token models:
	 ```sh
	 python manage.py migrate
	 ```

4. Start the server and use the above endpoints.

