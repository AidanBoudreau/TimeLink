import React from 'react';
import { useAuth } from '../contexts/AuthContext';

const ManagerDashboard: React.FC = () => {
  const { user } = useAuth();

  return (
    <div className="container mt-4">
      <h1>Manager Dashboard</h1>
      <p>Welcome, {user?.name}!</p>
      <div className="alert alert-info">
        Manager dashboard functionality coming soon...
      </div>
    </div>
  );
};

export default ManagerDashboard;