/bookings  (GET)         - List bookings for a date. Example: /bookings?date=2025-11-10
/bookings  (POST)        - Create a booking. JSON body: {"first_name":"Alice","reservation_date":"YYYY-MM-DD","reservation_slot":12}
/book/     (GET/HTML)     - Booking form (UI) that posts to /bookings via fetch()
/reservations/ (GET/HTML) - Page that shows all bookings (JSON rendered in page)

Notes:
- The main API endpoint for automated testing is /bookings (GET and POST).
- Use application/json for POST requests.
- If a slot is already booked for a date, the POST will return an error response.
