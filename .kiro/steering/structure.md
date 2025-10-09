# Project Structure

## Directory Organization

```
tankas_app/
├── main.py                    # Application entry point and routing setup
├── requirements.txt           # Python dependencies
├── README.md                 # Project documentation
├── .gitignore               # Git ignore patterns
│
├── pages/                   # Page components with @ui.page() decorators
│   ├── homepage.py          # Public landing page (/)
│   ├── signin.py            # Login page (/login)
│   ├── signup.py            # Registration page (/signup)
│   ├── dashboard.py         # User dashboard (/dashboard) - protected
│   ├── issues.py            # Browse/create issues (/issues) - protected
│   ├── issue_detail.py      # Issue detail view (/issues/{id}) - protected
│   ├── warrior.py           # Warriors leaderboard (/warriors) - protected
│   └── rewards.py           # Rewards system (/rewards) - protected
│
└── components/              # Reusable UI components
    ├── navbar.py            # Navigation bar component
    ├── sidebar.py           # Dashboard sidebar component
    ├── footer.py            # Footer component
    ├── issue_card.py        # Issue display card
    ├── warrior_card.py      # Warrior profile card
    ├── stats_card.py        # Statistics display card
    ├── camera_capture.py    # Camera/image capture component
    ├── location_picker.py   # GPS location picker component
    ├── comment_section.py   # Comments component
    └── map_view.py          # Map display component
```

## Coding Conventions

### Page Structure
- Each page file contains one `@ui.page()` decorated function
- Pages import and use shared components
- Protected pages should implement authentication guards
- Use descriptive function names matching the page purpose

### Component Structure
- Components are functions that return UI elements or create them in-place
- Use consistent naming: `show_navbar()`, `create_issue_card()`, etc.
- Components should be reusable and accept parameters when needed
- Import components at the top of page files

### File Naming
- Use snake_case for all Python files
- Page files should match their route purpose (e.g., `issue_detail.py` for `/issues/{id}`)
- Component files should describe their UI purpose

### Import Organization
```python
# Standard library imports first
from functools import wraps

# Third-party imports
from nicegui import ui, app

# Local imports
from components.navbar import show_navbar
from components.footer import show_footer
```

## Planned Extensions
The README indicates plans for additional directories:
- `services/` - API client services for backend communication
- `utils/` - Helper functions and utilities
- `static/` - CSS, JavaScript, and image assets