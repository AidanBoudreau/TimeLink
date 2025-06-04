# Labor Tracking System - GitHub Setup Files

## README.md

```markdown
# Labor Tracking System

A modern web application for managers to track employee labor hours and costs for past and ongoing jobs.

## Team: The Incredibles

### Team Members
- **Frontend Development**: Ilan Danial, Aidan Boudreau
- **Backend Development**: Elan Wygodski, Matt

## Project Vision

For **managers** that need to **monitor work hours**, this is a **bookkeeping product** that **records total labor hours and labor costs of each past and ongoing job**. Unlike the **DBA Manufacturing Next Generation system**, our product **provides a modern and simple user interface for employees and managers to interact with**. The system gives abilities to output reports with daily, weekly, and monthly viewpoints on labor hours, labor costs, and labor payments.

## Tech Stack

### Frontend
- **Languages**: HTML, CSS, JavaScript, TypeScript
- **Framework**: React with Electron
- **Bundler**: Webpack
- **CSS Preprocessor**: SASS
- **CSS Framework**: Bootstrap

### Backend
- **Language**: Python
- **Framework**: Flask
- **Package Manager**: pip

### Infrastructure
- **Hosting**: UF Server
- **Database**: SQLite
- **Version Control**: Git + GitHub

## Quick Start

1. Clone the repository
   ```bash
   git clone https://github.com/[your-username]/TimeLink.git
   cd labor-tracking-system
   ```

2. Set up the backend
   ```bash
   cd backend
   pip install -r requirements.txt
   python run.py
   ```

3. Set up the frontend
   ```bash
   cd frontend
   npm install
   npm start
   ```

For detailed setup instructions, see [SETUP.md](docs/SETUP.md).

## Features

- Employee time tracking
- Job cost calculation
- Labor hour reporting (daily/weekly/monthly)
- Modern, user-friendly interface
- Manager dashboard
- Employee portal
- Export capabilities for reports

## Contributing

Please read our contributing guidelines before submitting pull requests.


## .gitignore (Root)

```
# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Environment variables
.env
.env.local
.env.*.local

# Logs
*.log
logs/

# Database
*.db
*.sqlite
*.sqlite3
database/*.db

# Compiled files
*.pyc
__pycache__/
*.pyo
*.pyd
.Python

# Distribution / packaging
build/
dist/
*.egg-info/
```

## frontend/.gitignore

```
# Dependencies
node_modules/
/.pnp
.pnp.js

# Testing
coverage/

# Production
build/
dist/
out/

# Misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# TypeScript
*.tsbuildinfo

# Electron
electron-builder.yml
```

## backend/.gitignore

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv

# Flask
instance/
.webassets-cache

# Database
*.db
*.sqlite
*.sqlite3

# PyCharm
.idea/

# VS Code
.vscode/

# Environment variables
.env
.flaskenv
```

## frontend/package.json

```json
{
  "name": "labor-tracking-frontend",
  "version": "1.0.0",
  "description": "Frontend for Labor Tracking System",
  "main": "electron/main.js",
  "scripts": {
    "start": "webpack serve --mode development",
    "build": "webpack --mode production",
    "electron": "electron .",
    "electron-build": "npm run build && electron-builder",
    "test": "jest",
    "lint": "eslint src/**/*.{ts,tsx}"
  },
  "keywords": ["labor", "tracking", "management"],
  "author": "The Incredibles",
  "license": "MIT",
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.8.0",
    "bootstrap": "^5.3.0",
    "axios": "^1.3.0"
  },
  "devDependencies": {
    "@types/react": "^18.0.0",
    "@types/react-dom": "^18.0.0",
    "typescript": "^4.9.0",
    "webpack": "^5.75.0",
    "webpack-cli": "^5.0.0",
    "webpack-dev-server": "^4.11.0",
    "ts-loader": "^9.4.0",
    "css-loader": "^6.7.0",
    "sass-loader": "^13.2.0",
    "sass": "^1.57.0",
    "style-loader": "^3.3.0",
    "html-webpack-plugin": "^5.5.0",
    "electron": "^22.0.0",
    "electron-builder": "^23.6.0",
    "@typescript-eslint/eslint-plugin": "^5.48.0",
    "@typescript-eslint/parser": "^5.48.0",
    "eslint": "^8.31.0",
    "jest": "^29.3.0"
  }
}
```

## backend/requirements.txt

```
Flask==2.3.2
Flask-SQLAlchemy==3.0.5
Flask-CORS==4.0.0
Flask-JWT-Extended==4.5.2
python-dotenv==1.0.0
SQLAlchemy==2.0.19
Werkzeug==2.3.6
pytest==7.4.0
pytest-flask==1.2.0
```

## .github/workflows/ci.yml

```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        cd backend
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        cd backend
        pytest

  frontend-tests:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
    
    - name: Install dependencies
      run: |
        cd frontend
        npm ci
    
    - name: Run linter
      run: |
        cd frontend
        npm run lint
    
    - name: Run tests
      run: |
        cd frontend
        npm test -- --passWithNoTests
```

## docs/SETUP.md

```markdown
# Setup Guide

## Prerequisites

- Python 3.8+
- Node.js 16+
- Git

## Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file with the following:
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///labor_tracking.db
   ```

6. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

7. Run the backend:
   ```bash
   python run.py
   ```

## Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file:
   ```
   REACT_APP_API_URL=http://localhost:5000
   ```

4. Start the development server:
   ```bash
   npm start
   ```

## Database Schema

The SQLite database includes the following tables:
- `users` - Employee and manager accounts
- `jobs` - Job information
- `time_entries` - Labor hour records
- `reports` - Generated reports

See `database/schema.sql` for the complete schema.
```

## Contributing Guidelines (CONTRIBUTING.md)

```markdown
# Contributing to Labor Tracking System

## Workflow

1. Create a feature branch from `develop`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit with descriptive messages
   ```bash
   git commit -m "feat: add employee time entry form"
   ```

3. Push to your branch
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request to `develop` branch

## Commit Message Convention

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc)
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

## Code Style

### Frontend (TypeScript/React)
- Use functional components with hooks
- Follow ESLint configuration
- Use meaningful variable names

### Backend (Python/Flask)
- Follow PEP 8
- Use type hints where applicable
- Write docstrings for functions

## Testing

- Write unit tests for new features
- Ensure all tests pass before submitting PR
- Aim for >80% code coverage

## Pull Request Process

1. Update documentation if needed
2. Ensure CI/CD pipeline passes
3. Request review from at least one team member
4. Squash commits before merging
```
