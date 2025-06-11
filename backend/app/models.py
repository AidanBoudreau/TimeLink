"""
Database models for TimeLink
"""
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    """User model for employees, managers, and admins"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='employee')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    time_entries = db.relationship('TimeEntry', backref='user', lazy='dynamic', foreign_keys='TimeEntry.user_id')
    modified_entries = db.relationship('TimeEntry', backref='modifier', lazy='dynamic', foreign_keys='TimeEntry.modified_by')
    created_jobs = db.relationship('Job', backref='creator', lazy='dynamic')
    generated_reports = db.relationship('Report', backref='generator', lazy='dynamic')
    
    def set_password(self, password):
        """Set password hash"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if password matches"""
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class TimeEntry(db.Model):
    """Time entry model for tracking employee hours"""
    __tablename__ = 'time_entries'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    clock_in = db.Column(db.DateTime, nullable=False)
    clock_out = db.Column(db.DateTime)
    break_duration = db.Column(db.Integer, default=0)  # in minutes
    total_hours = db.Column(db.Float)
    status = db.Column(db.String(20), default='active')
    modified_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    modification_reason = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    task_entries = db.relationship('TaskEntry', backref='time_entry', cascade='all, delete-orphan')
    break_entries = db.relationship('BreakEntry', backref='time_entry', cascade='all, delete-orphan')
    
    def calculate_total_hours(self):
        """Calculate total hours worked"""
        if self.clock_out:
            duration = (self.clock_out - self.clock_in).total_seconds() / 3600
            break_hours = self.break_duration / 60 if self.break_duration else 0
            self.total_hours = round(duration - break_hours, 2)
            return self.total_hours
        return 0
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'clock_in': self.clock_in.isoformat() if self.clock_in else None,
            'clock_out': self.clock_out.isoformat() if self.clock_out else None,
            'break_duration': self.break_duration,
            'total_hours': self.total_hours,
            'status': self.status,
            'modified_by': self.modified_by,
            'modification_reason': self.modification_reason
        }


class Job(db.Model):
    """Job/Project model"""
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    job_number = db.Column(db.String(50), unique=True, nullable=False)
    job_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='active')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    task_entries = db.relationship('TaskEntry', backref='job', lazy='dynamic')
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'job_number': self.job_number,
            'job_name': self.job_name,
            'description': self.description,
            'status': self.status,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class TaskEntry(db.Model):
    """Task entry model for tracking work done"""
    __tablename__ = 'task_entries'
    
    id = db.Column(db.Integer, primary_key=True)
    time_entry_id = db.Column(db.Integer, db.ForeignKey('time_entries.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    materials_used = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'time_entry_id': self.time_entry_id,
            'job_id': self.job_id,
            'job': self.job.to_dict() if self.job else None,
            'description': self.description,
            'materials_used': self.materials_used,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class BreakEntry(db.Model):
    """Break entry model for tracking breaks"""
    __tablename__ = 'break_entries'
    
    id = db.Column(db.Integer, primary_key=True)
    time_entry_id = db.Column(db.Integer, db.ForeignKey('time_entries.id'), nullable=False)
    break_start = db.Column(db.DateTime, nullable=False)
    break_end = db.Column(db.DateTime)
    duration = db.Column(db.Integer)  # in minutes
    
    def calculate_duration(self):
        """Calculate break duration"""
        if self.break_end:
            self.duration = int((self.break_end - self.break_start).total_seconds() / 60)
            return self.duration
        return 0
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'time_entry_id': self.time_entry_id,
            'break_start': self.break_start.isoformat() if self.break_start else None,
            'break_end': self.break_end.isoformat() if self.break_end else None,
            'duration': self.duration
        }


class Report(db.Model):
    """Report model for storing generated reports"""
    __tablename__ = 'reports'
    
    id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.String(50), nullable=False)
    generated_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_from = db.Column(db.Date, nullable=False)
    date_to = db.Column(db.Date, nullable=False)
    report_data = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'report_type': self.report_type,
            'generated_by': self.generated_by,
            'date_from': self.date_from.isoformat() if self.date_from else None,
            'date_to': self.date_to.isoformat() if self.date_to else None,
            'report_data': self.report_data,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }