#!/usr/bin/env python3
"""
Initialize the TimeLink database with default data
"""
import os
import sys
from datetime import datetime, timedelta
from app import create_app, db
from app.models import User, Job

def init_database():
    """Initialize the database with default data"""
    app = create_app('development')
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✓ Database tables created successfully")
        
        # Check if admin exists
        admin = User.query.filter_by(employee_id='ADMIN001').first()
        if not admin:
            # Create default admin user
            admin = User(
                employee_id='ADMIN001',
                name='Admin User',
                email='admin@timelink.com',
                role='admin'
            )
            admin.set_password('admin123')  # Change this in production!
            db.session.add(admin)
            print("✓ Default admin user created (ID: ADMIN001, Password: admin123)")
        
        # Create sample manager if doesn't exist
        manager = User.query.filter_by(employee_id='MGR001').first()
        if not manager:
            manager = User(
                employee_id='MGR001',
                name='John Manager',
                email='manager@timelink.com',
                role='manager'
            )
            manager.set_password('manager123')
            db.session.add(manager)
            print("✓ Sample manager created (ID: MGR001, Password: manager123)")
        
        # Create sample employees if don't exist
        employees_data = [
            ('EMP001', 'Alice Johnson', 'alice@timelink.com'),
            ('EMP002', 'Bob Smith', 'bob@timelink.com'),
            ('EMP003', 'Carol Davis', 'carol@timelink.com')
        ]
        
        for emp_id, name, email in employees_data:
            employee = User.query.filter_by(employee_id=emp_id).first()
            if not employee:
                employee = User(
                    employee_id=emp_id,
                    name=name,
                    email=email,
                    role='employee'
                )
                employee.set_password('employee123')
                db.session.add(employee)
                print(f"✓ Sample employee created ({emp_id}: {name})")
        
        # Create sample jobs if don't exist
        jobs_data = [
            ('JOB001', 'Website Redesign', 'Complete redesign of company website'),
            ('JOB002', 'Mobile App Development', 'Develop iOS and Android apps'),
            ('JOB003', 'Database Migration', 'Migrate from MySQL to PostgreSQL'),
            ('JOB004', 'Security Audit', 'Comprehensive security assessment'),
            ('JOB005', 'API Integration', 'Integrate third-party APIs')
        ]
        
        for job_num, job_name, desc in jobs_data:
            job = Job.query.filter_by(job_number=job_num).first()
            if not job:
                job = Job(
                    job_number=job_num,
                    job_name=job_name,
                    description=desc,
                    created_by=admin.id if admin else 1,
                    status='active'
                )
                db.session.add(job)
                print(f"✓ Sample job created ({job_num}: {job_name})")
        
        # Commit all changes
        db.session.commit()
        print("\n✅ Database initialization completed successfully!")
        print("\n📝 Default Login Credentials:")
        print("   Admin: ADMIN001 / admin123")
        print("   Manager: MGR001 / manager123")
        print("   Employee: EMP001 / employee123")
        print("\n⚠️  Remember to change these passwords in production!")

if __name__ == '__main__':
    init_database()