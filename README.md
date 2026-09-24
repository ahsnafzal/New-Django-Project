# Text-to-Speech API

A Django REST Framework backend that integrates with **ElevenLabs** to generate audio from text using different voices.

## Features

* Store ElevenLabs voices in the database
* List all available voices
* Filter voices by gender
* Generate audio from text using a selected voice
* ElevenLabs Text-to-Speech integration
* REST API endpoints using Django REST Framework

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL / SQLite
* ElevenLabs API

## Project Structure

```text
project/
├── app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── services.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── .gitignore
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
ELEVEN_LABS_API_KEY=your_api_key_here
```

Do not commit the `.env` file to GitHub.

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

### Get Voices

```http
GET /voices/
```

Returns all voices stored in the database.

### Filter Voices by Gender

Male voices:

```http
GET /voices/?gender=male
```

Female voices:

```http
GET /voices/?gender=female
```

### Generate Audio

```http
POST /audio/
```

Request body:

```json
{
    "text": "Hello, this is my first generated audio.",
    "voice_id": "YOUR_VOICE_ID"
}
```

The `voice_id` should be obtained from the `/voices/` endpoint.

The API sends the text and selected voice to ElevenLabs and returns the generated audio.

## Example Flow

```text
Client / Postman
       ↓
Django REST API
       ↓
Voice selected from database
       ↓
Text + Voice ID
       ↓
ElevenLabs API
       ↓
Generated Audio
```

## Environment Variables

| Variable              | Description                       |
| --------------------- | --------------------------------- |
| `ELEVEN_LABS_API_KEY` | API key used to access ElevenLabs |

## Development

Run the Django development server:

```bash
python manage.py runserver
```

Use **Postman** or another API client to test the endpoints.

## License

This project is for development and learning purposes.
