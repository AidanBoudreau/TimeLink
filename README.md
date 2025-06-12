# TimeLink - Employee Time and Task Management System

A modern web-based time tracking and labor management system designed to streamline workforce management for businesses. Built with React and Flask, TimeLink provides an intuitive interface for both employees and managers to track work hours, monitor task progress, and analyze labor costs.

## 🚀 Current Status

The application is currently in active development with core authentication and routing infrastructure complete. The system is ready for feature implementation.

### ✅ Completed Features
- **Authentication System**: JWT-based authentication with role-based access control
- **User Roles**: Support for Employee, Manager, and Admin roles
- **Database Schema**: Complete SQLite database with all necessary tables
- **API Structure**: RESTful API endpoints with Flask blueprints
- **Frontend Routing**: Protected routes based on user roles
- **Sample Data**: Pre-populated with test users and jobs

### 🔄 In Progress
- Employee clock in/out functionality
- Task logging and time entry
- Manager dashboards and reporting
- Admin user management

## 👥 Team: The Incredibles

- **Product Owner**: Aidan Boudreau
- **Scrum Master**: Elan Wygodski
- **Development Team**: Ilan Danial, Matt Beutel

## 📋 Project Vision

FOR managers that need to monitor work hours and labour costs in an effective manner. THE TimeLink system is an online bookkeeping product that records labor hours and connected labor costs of each past and ongoing job. Unlike the DBA Manufacturing Next Generation system, TimeLink provides a modern and simple user interface for employees and managers to interact with. OUR product gives managers the ability to easily generate reports on labour hours, labor costs, and payments with daily, weekly and monthly views via an easily readable dashboard.

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 18.2.0 with TypeScript
- **Routing**: React Router DOM 6.20.0
- **Styling**: Bootstrap 5.3.2 + SASS
- **HTTP Client**: Axios
- **Build Tool**: Webpack 5
- **Desktop App**: Electron (optional)

### Backend
- **Framework**: Flask 3.0.0 (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-JWT-Extended
- **CORS**: Flask-CORS
- **Password Security**: Werkzeug

### Development Tools
- **Version Control**: Git + GitHub
- **Package Management**: npm (frontend), pip (backend)
- **Environment Management**: python-dotenv

## 🚦 Quick Start

### Prerequisites
- Node.js (v14.0.0 or higher)
- Python (3.8 or higher)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/[your-username]/TimeLink.git
   cd TimeLink
   ```

2. **Set up the backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python init_db.py  # Initialize database with sample data
   ```

3. **Configure backend environment**
   Create a `.env` file in the backend directory:
   ```env
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=dev-secret-key-123
   JWT_SECRET_KEY=dev-jwt-secret-456
   PORT=5001
   ```

4. **Set up the frontend**
   ```bash
   cd ../frontend
   npm install
   ```

5. **Configure frontend environment**
   Create a `.env` file in the frontend directory:
   ```env
   REACT_APP_API_URL=http://localhost:5001/api
   ```

### Running the Application

1. **Start the backend server** (in backend directory with venv activated):
   ```bash
   cd ../backend
   python run.py
   ```
   The API will be available at `http://localhost:5001`

2. **Start the frontend** (in a new terminal, in frontend directory):
   ```bash
   cd TimeLink
   cd frontend
   npm start
   ```
   The application will open at `http://localhost:3000`

## 🔐 Test Credentials

| Role     | Employee ID | Password      |
|----------|-------------|---------------|
| Admin    | ADMIN001    | admin123      |
| Manager  | MGR001      | manager123    |
| Employee | EMP001      | employee123   |
| Employee | EMP002      | employee123   |
| Employee | EMP003      | employee123   |

## 📁 Project Structure

```
labor-tracking-system/
├── frontend/                    # React TypeScript frontend
│   ├── src/
│   │   ├── components/         # Reusable React components
│   │   ├── contexts/           # React contexts (Auth)
│   │   ├── pages/              # Page components
│   │   ├── styles/             # SCSS styles
│   │   ├── App.tsx             # Main App component
│   │   └── index.tsx           # React entry point
│   ├── public/                 # Static files
│   ├── package.json            # Node dependencies
│   ├── tsconfig.json           # TypeScript config
│   └── webpack.config.js       # Webpack config
├── backend/                     # Flask Python backend
│   ├── app/
│   │   ├── __init__.py        # Flask app factory
│   │   ├── models.py          # SQLAlchemy models
│   │   └── routes/            # API endpoints
│   ├── requirements.txt        # Python dependencies
│   ├── config.py              # Flask configuration
│   ├── run.py                 # Flask entry point
│   └── init_db.py             # Database initialization
├── database/                   # Database files
│   └── schema.sql             # SQLite schema
└── docs/                       # Documentation
```

## 🔧 API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user
- `POST /api/auth/refresh` - Refresh access token

### Employee Endpoints
- `GET /api/employee/dashboard` - Employee dashboard data
- `POST /api/employee/clock-in` - Clock in (to be implemented)
- `POST /api/employee/clock-out` - Clock out (to be implemented)

### Manager Endpoints
- `GET /api/manager/dashboard` - Manager dashboard data
- `GET /api/manager/reports` - Generate reports (to be implemented)

### Admin Endpoints
- `GET /api/admin/dashboard` - Admin dashboard data
- `GET /api/admin/users` - User management (to be implemented)

## 📊 Database Schema

The SQLite database includes the following tables:

- **users** - Employee, manager, and admin accounts
- **time_entries** - Clock in/out records
- **jobs** - Projects and job information
- **task_entries** - Work descriptions and materials used
- **break_entries** - Break time tracking
- **reports** - Generated report storage

## 🐛 Troubleshooting

### Common Issues

1. **Port 5000 already in use**
   - The backend is configured to use port 5001 to avoid conflicts with macOS AirPlay

2. **CORS errors**
   - Ensure the backend is running on port 5001
   - Check that frontend .env has correct API URL

3. **"Process is not defined" error**
   - This has been fixed in the webpack configuration
   - Ensure you have the latest webpack.config.js

4. **SASS deprecation warnings**
   - These are non-critical warnings about future SASS changes
   - The app will work normally despite these warnings

## 🚧 Planned Features

### Phase 1: Core Functionality
- [ ] Employee clock in/out with real-time status
- [ ] Task entry with job selection and materials
- [ ] Break tracking
- [ ] Basic time calculations

### Phase 2: Manager Features
- [ ] Real-time employee status dashboard
- [ ] Daily/weekly/monthly reports
- [ ] Time entry approval/modification
- [ ] Labor cost calculations
- [ ] Export functionality (CSV/PDF)

### Phase 3: Advanced Features
- [ ] Email notifications
- [ ] Mobile responsive design
- [ ] Offline capability
- [ ] Advanced analytics
- [ ] Integration with payroll systems

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Commit Message Convention
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

## 📝 License

This project is part of a university course project.

## 📞 Support

For questions or issues:
1. Check the [Issues](https://github.com/[your-username]/labor-tracking-system/issues) page
2. Review the documentation in the `docs/` folder
3. Contact team members through the course channels

---

**Note**: This is an active development project. Features and documentation are being continuously updated.
