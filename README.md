Flight Tracking System — Django REST Framework

Real-time flight tracking system for routes from Pakistan to international 
destinations, built with Django REST Framework and the AviationStack API.


Features

1. Search flights by departure and arrival airport codes
2. Real-time flight schedule, status (scheduled/landed), and timing data
3. Supports major Pakistani airports (KHI, ISB, LHR) and international hubs (JFK, LAX, LHR, DXB, DOH).
4. Clean frontend interface displaying live flight data in a structured table

Tech Stack

1. Backend: Django, Django REST Framework
API Integration: AviationStack API
Frontend: HTML, CSS, JavaScript
Environment Management: python-dotenv (.env for API key security)

How It Works

1. User enters departure and arrival airport codes (e.g., KHI → DOH)
2. Django backend sends a request to AviationStack API with the route filters
3. API response is parsed and serialized through DRF
4. Frontend displays flight number, airline, scheduled times, and live status

Challenges Solved

1. Debugged authentication issues between Django and the external API
2. Resolved routing conflicts between API endpoints and frontend URL patterns
3. Fixed HTML template serving issues within the DRF project structure
4. Implemented environment variable management to keep API keys secure

Setup

```bash
git clone https://github.com/Arslan-32005/Flight-Tracking-DRF-API.git
cd Flight-Tracking-DRF-API
pip install -r requirements.txt

# Create a .env file with your own AviationStack API key:
# AVIATIONSTACK_API_KEY=your_key_here

python manage.py runserver
```

Screenshots
<img width="814" height="608" alt="image" src="https://github.com/user-attachments/assets/d37d32b0-2b1a-4d08-8526-fbc6e0e98f0b" />

Skills Demonstrated

1. REST API design and integration
2. Working with third-party APIs and API key management
3. Django REST Framework (serializers, views, URL routing)
4. Debugging full-stack issues (backend ↔ frontend ↔ external API)
