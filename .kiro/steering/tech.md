# Technology Stack

## Framework & Core Libraries
- **NiceGUI**: Python-based web framework for building reactive web applications
- **Python 3.x**: Primary programming language
- **HTTPX**: Async HTTP client for API communication (planned)
- **Requests**: HTTP library for backend API calls

## Frontend Technologies
- **NiceGUI Components**: Native UI components (ui.card, ui.button, ui.input, etc.)
- **JavaScript Integration**: For camera access and GPS geolocation
- **Leaflet Maps**: For location display and mapping features
- **Custom CSS**: For styling and responsive design

## Development Environment
- **Static Assets**: Served from `/assets` directory
- **Hot Reload**: NiceGUI's built-in development server
- **Environment Variables**: Configuration via `.env` files

## Common Commands

### Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python main.py

# Run with specific host/port (if configured)
python main.py --host 0.0.0.0 --port 8080
```

### Project Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Architecture Patterns
- **Page-based routing**: Each page is a separate Python module with `@ui.page()` decorator
- **Component-based UI**: Reusable UI components in separate modules
- **Service layer**: Planned API client services for backend communication
- **Static file serving**: Assets served from dedicated directory