# TimeLink Setup Guide

## Prerequisites

Before setting up TimeLink, ensure you have the following installed:

- **Node.js** (v14.0.0 or higher)
- **Python** (3.8 or higher)
- **Git**
- **npm** or **yarn**
- **pip** (Python package manager)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/labor-tracking-system.git
cd labor-tracking-system
```

### 2. Backend Setup

#### 2.1 Create Python Virtual Environment

```bash
cd backend
python -m venv venv
```

#### 2.2 Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

#### 2.3 Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### 2.4 Set Up Environment Variables

Create a `.env` file in the backend directory:

```bash
cp .env.example .env
```

Edit the `.env` file with your configuration:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
DATABASE_URL=sqlite:///../database/timelink.db
```

#### 2.5 Initialize the Database

```bash
python init_db.py
```

### 3. Frontend Setup

#### 3.1 Install Node Dependencies

```bash
cd ../frontend
npm install
```

#### 3.2 Set Up Environment Variables

Create a `.env` file in the frontend directory:

```bash
cp .env.example .env
```

Edit the `.env` file:

```env
REACT_APP_API_URL=http://localhost:5000/api
```

### 4. Running the Application

#### 4.1 Start the Backend Server

In the backend directory with virtual environment activated:

```bash
python run.py
```

The Flask API will start on `http://localhost:5000`

#### 4.2 Start the Frontend Development Server

In a new terminal, navigate to the frontend directory:

```bash
cd frontend
npm start
```

The React app will start on `http://localhost:3000`

## Building for Production

### Backend

1. Set `FLASK_ENV=production` in your environment
2. Use a production WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Frontend

Build the production bundle:

```bash
npm run build
```

The optimized files will be in the `frontend/build` directory.

### Electron App (Optional)

To build the desktop application:

```bash
npm run electron-build
```

## Database Management

### Running Migrations

```bash
cd backend
python manage.py db migrate -m "Description of changes"
python manage.py db upgrade
```

### Creating Initial Admin User

```bash
cd backend
python create_admin.py
```

## Testing

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   - Change the port in the configuration files
   - Or kill the process using the port

2. **Database Connection Error**
   - Ensure the database file exists
   - Check file permissions
   - Verify the database URL in .env

3. **CORS Issues**
   - Ensure the backend is running
   - Check that CORS is properly configured in Flask
   - Verify the API URL in frontend .env

### Getting Help

If you encounter issues:

1. Check the console logs for error messages
2. Ensure all dependencies are installed correctly
3. Verify environment variables are set properly
4. Check the [Issues](https://github.com/yourusername/labor-tracking-system/issues) page

## Next Steps

- Read the [User Guide](USER_GUIDE.md) for usage instructions
- Review the [API Documentation](API.md) for endpoint details
- Set up your development environment and start coding!