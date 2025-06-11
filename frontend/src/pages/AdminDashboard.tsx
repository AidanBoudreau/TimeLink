import React from 'react';
import { useAuth } from '../contexts/AuthContext';

const AdminDashboard: React.FC = () => {
  const { user } = useAuth();

  return (
    <div className="container mt-4">
      <h1>Admin Dashboard</h1>
      <p>Welcome, {user?.name}!</p>
      <div className="alert alert-info">
        Admin dashboard functionality coming soon...
      </div>
    </div>
  );
};

export default AdminDashboard;