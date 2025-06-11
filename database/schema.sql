-- TimeLink Database Schema
-- SQLite Database

-- Users table (for both employees and managers)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('employee', 'manager', 'admin')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Time entries table
CREATE TABLE IF NOT EXISTS time_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    clock_in TIMESTAMP NOT NULL,
    clock_out TIMESTAMP,
    break_duration INTEGER DEFAULT 0, -- in minutes
    total_hours DECIMAL(5,2),
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'completed', 'modified')),
    modified_by INTEGER,
    modification_reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (modified_by) REFERENCES users(id)
);

-- Jobs/Projects table
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_number VARCHAR(50) UNIQUE NOT NULL,
    job_name VARCHAR(200) NOT NULL,
    description TEXT,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'completed', 'on_hold', 'cancelled')),
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- Task entries table
CREATE TABLE IF NOT EXISTS task_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_entry_id INTEGER NOT NULL,
    job_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    materials_used TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (time_entry_id) REFERENCES time_entries(id),
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);

-- Break entries table
CREATE TABLE IF NOT EXISTS break_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_entry_id INTEGER NOT NULL,
    break_start TIMESTAMP NOT NULL,
    break_end TIMESTAMP,
    duration INTEGER, -- in minutes
    FOREIGN KEY (time_entry_id) REFERENCES time_entries(id)
);

-- Reports table (for storing generated reports)
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    report_type VARCHAR(50) NOT NULL,
    generated_by INTEGER NOT NULL,
    date_from DATE NOT NULL,
    date_to DATE NOT NULL,
    report_data JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (generated_by) REFERENCES users(id)
);

-- Create indexes for better performance
CREATE INDEX idx_time_entries_user_id ON time_entries(user_id);
CREATE INDEX idx_time_entries_clock_in ON time_entries(clock_in);
CREATE INDEX idx_task_entries_job_id ON task_entries(job_id);
CREATE INDEX idx_users_employee_id ON users(employee_id);

-- Create triggers to update timestamps
CREATE TRIGGER update_users_timestamp 
AFTER UPDATE ON users
BEGIN
    UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

CREATE TRIGGER update_jobs_timestamp 
AFTER UPDATE ON jobs
BEGIN
    UPDATE jobs SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;