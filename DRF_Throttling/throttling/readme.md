# Django REST API with Rate Limiting and JWT Authentication

## Overview
This Django REST API demonstrates rate limiting and JWT authentication for a weather endpoint.

## API Endpoint
- **URL**: `GET http://127.0.0.1:8000/weather/`

## Authentication
Add the JWT token to the Authorization header:
```
Authorization: token <your_jwt_token>
```

## Token Generation
Generate a token for a user:
```bash
python manage.py drf_create_token <username>
```

## Rate Limiting
- **Anonymous users**: 5 requests per minute
- **Authenticated users**: 10 requests per minute

### Rate Limit Behavior
- Returns **429 Too Many Requests** when limit is exceeded
- Error message includes wait time in seconds

Example error response:
```json
{
    "detail": "Request was throttled. Expected available in 3578 seconds."
}
```

## Installation

### Prerequisites
- Python
- Django
- Django REST Framework

### Setup Steps
1. Clone the repository
2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python manage.py runserver
```

## Testing
1. Use Postman or similar API testing tool
2. Add Authorization header with JWT token
3. Send GET request to `/weather/` endpoint
4. Monitor response status and rate limit messages

## Notes
- Exceeding rate limit results in `429 Too Many Requests` error
- Wait time indicates when you can retry the request