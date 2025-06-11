import React from 'react';
import { useAuth } from '../contexts/AuthContext';

const EmployeeDashboard: React.FC = () => {
  const { user } = useAuth();

  return (
    <div className="container mt-4">
      <h1>Employee Dashboard</h1>
      <p>Welcome, {user?.name}!</p>
      <div className="alert alert-info">
        Employee dashboard functionality coming soon...
      </div>
    </div>
  );
};

export default EmployeeDashboard;