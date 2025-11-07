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
