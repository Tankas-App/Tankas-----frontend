tankas_app-frontend/
│
├── app/
│   ├── __init__.py
│   ├── main.py                          # NiceGUI application entry point
│   ├── config.py                        # Frontend configuration (API URLs, etc.)
│   │
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── homepage.py                  # Public landing page (GET ALL EVENTS)
│   │   ├── login.py                     # Login page
│   │   ├── signup.py                    # Signup page
│   │   ├── dashboard.py                 # User dashboard (stats, profile)
│   │   ├── issues.py                    # Browse/create issues page
│   │   ├── issue_detail.py              # Single issue detail page
│   │   ├── warriors.py                  # GET Clean Up Warriors page
│   │   └── rewards.py                   # Rewards and leaderboard page
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── navbar.py                    # Navigation bar component
        ├──  sidebar.py                  # Sidebar component (Dashboard)
│   │   ├── footer.py                    # Footer component
│   │   ├── issue_card.py                # Issue card component
│   │   ├── warrior_card.py              # Warrior card component
│   │   ├── stats_card.py                # Statistics card component
│   │   ├── camera_capture.py            # Camera/image capture component
│   │   ├── location_picker.py           # GPS location picker component
│   │   ├── comment_section.py           # Comments component
│   │   └── map_view.py                  # Map display component (leaflet)
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── api_client.py                # HTTP client for backend API
│   │   ├── auth_service.py              # Authentication service
│   │   ├── user_service.py              # User API calls
│   │   ├── issue_service.py             # Issue API calls
│   │   ├── warrior_service.py           # Warrior API calls
│   │   └── reward_service.py            # Reward API calls
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py                # Form validation helpers
│   │   ├── formatters.py                # Date/time formatters
│   │   ├── storage.py                   # Session/local storage helpers
│   │   └── constants.py                 # Constants (priorities, difficulties)
│   │
│   └── static/
│       ├── css/
│       │   └── custom.css               # Custom CSS styles
│       ├── js/
│       │   ├── geolocation.js           # GPS/location JavaScript
│       │   └── camera.js                # Camera access JavaScript
│       └── images/
│           ├── logo.png
│           └── default-avatar.png
│
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md


═══════════════════════════════════════════════════════════
REQUIREMENTS.TXT
═══════════════════════════════════════════════════════════

nicegui==1.4.0
httpx==0.25.1                    # Async HTTP client
python-dotenv==1.0.0
pydantic==2.5.0
pillow==10.1.0                   # Image handling


═══════════════════════════════════════════════════════════
.ENV.EXAMPLE
═══════════════════════════════════════════════════════════

# Backend API Configuration
API_BASE_URL=http://localhost:8000
API_TIMEOUT=30

# Frontend Configuration
APP_TITLE=Cleanup Warriors
APP_HOST=0.0.0.0
APP_PORT=8080
DEBUG=true

# Session
SESSION_SECRET=your-session-secret-key-change-in-production


═══════════════════════════════════════════════════════════
.GITIGNORE
═══════════════════════════════════════════════════════════

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# NiceGUI storage
.nicegui/

# Logs
*.log


═══════════════════════════════════════════════════════════
NICEGUI FEATURES TO IMPLEMENT
═══════════════════════════════════════════════════════════

PAGES ROUTING:
- Use @ui.page() decorator for each page
- Implement navigation between pages
- Handle authentication guards for protected pages

CAMERA CAPTURE:
- Use ui.upload() for image upload from device
- JavaScript integration for camera access (getUserMedia API)
- Preview captured images before submission

GPS LOCATION:
- JavaScript geolocation API integration
- Display coordinates before submission
- Optional: Leaflet map integration to show location

AUTHENTICATION:
- Store JWT token in app.storage.user (session storage)
- Use decorators to protect authenticated routes
- Automatic redirect to login if not authenticated

UI COMPONENTS:
- ui.card() for issue cards, warrior cards
- ui.table() for leaderboard
- ui.dialog() for modals (create issue, comments)
- ui.notify() for success/error messages
- ui.chart() for dashboard statistics

REAL-TIME FEATURES:
- Use ui.timer() for auto-refresh data
- WebSocket support for real-time updates (optional)


═══════════════════════════════════════════════════════════
APPLICATION FLOW
═══════════════════════════════════════════════════════════

1. LANDING PAGE (/)
   - Public, no authentication required
   - Display all events/issues (GET /api/events)
   - Show "Sign Up" and "Login" buttons
   - Navbar with app branding

2. LOGIN PAGE (/login)
   - Login form (username, password)
   - Call POST /api/auth/login
   - Store JWT token in session
   - Redirect to dashboard on success

3. SIGNUP PAGE (/signup)
   - Registration form (username, email, password)
   - Call POST /api/auth/signup
   - Store JWT token in session
   - Redirect to dashboard on success

4. DASHBOARD (/dashboard) - PROTECTED
   - Display user stats (points, tasks completed, etc.)
   - Profile edit section (avatar, display name)
   - Recent issues created by user
   - Quick actions (Create Issue, View Warriors)

5. ISSUES PAGE (/issues) - PROTECTED
   - List all issues with filters
   - Create new issue button
   - Issue cards with:
     * Title, description, status
     * Picture, location
     * Priority, difficulty
     * Action buttons (View Details, Resolve)

6. ISSUE DETAIL PAGE (/issues/{id}) - PROTECTED
   - Full issue details
   - Picture display
   - Map showing location
   - Comments section
   - Actions: Edit (if owner), Resolve, Add Comment

7. CREATE ISSUE DIALOG - PROTECTED
   - Form fields: title, description, priority, difficulty
   - Camera capture button for taking picture
   - GPS location capture button
   - Display coordinates before submission
   - Submit button (POST /api/issues with multipart/form-data)

8. WARRIORS PAGE (/warriors) - PROTECTED
   - Display all cleanup warriors (GET /api/warriors)
   - Grid/table view with:
     * Avatar
     * Username/Display name
     * Points
     * Tasks completed
   - Sorted by points (highest first)

9. REWARDS PAGE (/rewards) - PROTECTED
   - Available rewards display
   - Leaderboard (top 10 users)
   - User's current rank and points


═══════════════════════════════════════════════════════════
KEY NICEGUI PATTERNS
═══════════════════════════════════════════════════════════

AUTHENTICATION GUARD:
```python
from functools import wraps
from nicegui import ui, app

def require_auth(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not app.storage.user.get('token'):
            ui.navigate.to('/login')
            return
        return await func(*args, **kwargs)
    return wrapper

@ui.page('/dashboard')
@require_auth
async def dashboard():
    # Protected page content
    pass
```

CAMERA CAPTURE:
```python
async def capture_image():
    # Use ui.upload with camera capture
    ui.upload(
        on_upload=handle_upload,
        auto_upload=True
    ).props('accept="image/*" capture="camera"')
```

GPS LOCATION:
```python
# JavaScript integration
ui.add_head_html('''
<script>
function getLocation(callback) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            position => callback(position.coords.latitude, position.coords.longitude)
        );
    }
}
</script>
''')

# Python side
location = ui.run_javascript('getLocation((lat, lng) => [lat, lng])')
```

API CALLS:
```python
import httpx

async def call_api(endpoint, method='GET', data=None, token=None):
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    
    async with httpx.AsyncClient() as client:
        if method == 'GET':
            response = await client.get(f'{API_BASE_URL}{endpoint}', headers=headers)
        elif method == 'POST':
            response = await client.post(f'{API_BASE_URL}{endpoint}', json=data, headers=headers)
    
    return response.json()
```


═══════════════════════════════════════════════════════════
RECOMMENDED NICEGUI UI ELEMENTS
═══════════════════════════════════════════════════════════

NAVBAR:
- ui.header() with ui.link() for navigation
- ui.button() for logout

CARDS:
- ui.card() for issue cards, warrior cards
- ui.card_section() for content organization
- ui.image() for pictures/avatars

FORMS:
- ui.input() for text fields
- ui.textarea() for descriptions
- ui.select() for dropdowns (priority, difficulty)
- ui.button() for submit

DISPLAY:
- ui.table() for leaderboards, data tables
- ui.label() for text display
- ui.badge() for status indicators
- ui.chip() for tags
- ui.avatar() for user pictures

FEEDBACK:
- ui.notify() for success/error messages
- ui.dialog() for modals
- ui.spinner() for loading states

LAYOUT:
- ui.row() and ui.column() for layout
- ui.grid() for responsive grids
- ui.expansion() for collapsible sections

COLORS
#F7FFF7 - MINT CREAM  // background color of pages
#007F7C - TEAL //buttons, widgets
#ade6e5ff - Light TEAL //
#2E86AB - BLUE(NCS)  //header texts
#0A0A0A - NIGHT
#f8d50eff - GOLD
