# University Management System


<br />
<div align="center">

<h3 align="center">University Management System</h3>

  <p align="center">
    A comprehensive Django-based web application for managing university resources including students, courses, and staff.
    
  </p>
</div>

## Table of Contents

<details>
  <summary>Click to expand</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#data-seeding">Data Seeding</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

The University Management System is a comprehensive web application designed to streamline the administrative processes of educational institutions. This platform provides an integrated solution for managing students, courses, academic staff, and departmental information.

### Built With

* [Django](https://www.djangoproject.com/) - The web framework
* [SQLite](https://www.sqlite.org/) - Database (configurable to other DB engines)
* [HTML/CSS](https://developer.mozilla.org/en-US/docs/Web/HTML) - Frontend

### Features

* **User Authentication System**
  * User registration with email validation (.edu addresses only)
  * Secure login/logout functionality
  * Role-based access control

* **Student Management**
  * Add, view, and manage student records
  * Track student course enrollments
  * Store student details including registration numbers

* **Course Management**
  * Create and manage course offerings
  * Course detail storage (code, credits, description)
  * Data validation for course information

* **Staff Management**
  * Faculty and administrative staff records
  * Department assignments
  * Position tracking and history

* **Department Organization**
  * Departmental structure management
  * Assignment of department heads

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.8 or higher
* pip (Python package manager)
* Git

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/SophieBlessed/university-management-system.git
   cd university-mgmt
   ```

2. Create and activate a virtual environment (optional but recommended)
   ```sh
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install required packages
   ```sh
   pip install -r requirements.txt
   ```

4. Run migrations
   ```sh
   python manage.py migrate
   ```

5. Create a superuser (admin)
   ```sh
   python manage.py createsuperuser
   ```

6. Start the development server
   ```sh
   python manage.py runserver
   ```

7. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin SophieBlessed/university-management-system
   git remote -v # confirm the changes
   ```

## Usage

After installation, you can access the system at `http://127.0.0.1:8000/`.

* Admin panel: `http://127.0.0.1:8000/admin/`
* Student management: `http://127.0.0.1:8000/students/`
* Course management: `http://127.0.0.1:8000/courses/`
* Staff management: `http://127.0.0.1:8000/staff/`

For new users, registration is available at `http://127.0.0.1:8000/accounts/register/`

## Data Seeding

The project includes a data seeding command to populate the database with sample departments and courses:

```sh
python manage.py seed_courses
```

This will create sample departments and course records to help you get started with testing.

## Project Structure

The system is organized into several Django apps:

* **accounts**: Handles user authentication and management
* **students**: Manages student information and enrollments
* **courses**: Handles course and department data
* **staff**: Manages faculty and administrative staff records

Each app contains its own models, views, forms, and templates following Django's MVT architecture.

## Roadmap

- [ ] Add advanced reporting features
- [ ] Implement grade management system
- [ ] Add calendar and scheduling functionality
- [ ] Create API endpoints for mobile application
- [ ] Implement document management for student records



## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Contact

Your Name - sophieblessed12@gmail.com

Project Link: [https://github.com/SophieBlessed/university-management-system.git](https://github.com/SophieBlessed/university-management-system.git)

