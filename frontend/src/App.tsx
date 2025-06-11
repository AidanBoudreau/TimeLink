import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/App.scss';

// Import pages (to be created)
import LoginPage from './pages/LoginPage';
import EmployeeDashboard from './pages/EmployeeDashboard';
import ManagerDashboard from './pages/ManagerDashboard';
import AdminDashboard from './pages/AdminDashboard';
import NotFound from './pages/NotFound';

// Import components
import PrivateRoute from './components/PrivateRoute';
import Navbar from './components/Navbar';

const App: React.FC = () => {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <main className="main-content">
          <Routes>
            {/* Public routes */}
            <Route path="/login" element={<LoginPage />} />
            <Route path="/" element={<Navigate to="/login" replace />} />
            
            {/* Protected routes */}
            <Route path="/employee" element={
              <PrivateRoute allowedRoles={['employee', 'manager', 'admin']}>
                <EmployeeDashboard />
              </PrivateRoute>
            } />
            
            <Route path="/manager" element={
              <PrivateRoute allowedRoles={['manager', 'admin']}>
                <ManagerDashboard />
              </PrivateRoute>
            } />
            
            <Route path="/admin" element={
              <PrivateRoute allowedRoles={['admin']}>
                <AdminDashboard />
              </PrivateRoute>
            } />
            
            {/* 404 route */}
            <Route path="*" element={<NotFound />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;