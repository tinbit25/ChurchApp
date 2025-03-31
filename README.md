# Church App Django Project

## Overview
The Church App is a digital platform designed to enhance the experience of church members and administrators. This web application will provide functionality for managing church services, educational content, donations, and community engagement. The app aims to make it easier for users to access church events, educational resources, and donation systems.

## Features
- **User Authentication & Profiles**
  - Users can register and log in with different roles (Admin, Teacher, Member).
  - Profile management for updating personal details and passwords.

- **Church Services & Events**
  - Display upcoming church services and events (e.g., Sunday Mass, special ceremonies).
  - Users can register for events and receive notifications and reminders.

- **Educational Resources**
  - Users can access religious educational content (Bible studies, lessons, and courses).
  - Teachers can upload and manage educational materials (text, audio, video).

- **Donation & Tithing Platform**
  - Allow users to make donations and tithes online.
  - Support for one-time and recurring donations.

## Project Structure

### Django Apps
- **Users App:** Manages user registration, authentication, and profile management.
- **Events App:** Handles church events, services, and event registration.
- **Education App:** Manages educational resources and materials uploaded by teachers.
- **Donations App:** Handles the donation and tithing system, including payment processing.

### Database Schema
- **User Model:** Custom user model with roles (admin, teacher, member).
- **Event Model:** Stores details about church events (date, time, description, location).
- **Educational Content Model:** Stores different types of content (text, audio, video).
- **Donation Model:** Tracks donations, including user, amount, and type (one-time or recurring).

### API Endpoints
- **User Authentication:**
  - `POST /api/register/` - Register a new user.
  - `POST /api/login/` - Log in a user.
  - `GET /api/profile/` - View and update user profile.

- **Event Management:**
  - `GET /api/events/` - List all upcoming events.
  - `POST /api/events/register/` - Register for an event.
  - `GET /api/events/{id}/` - Get event details.

- **Educational Resources:**
  - `GET /api/education/` - List all educational content.
  - `POST /api/education/upload/` - Upload new educational content (teacher role).
  - `GET /api/education/{id}/` - Get content details.

- **Donation:**
  - `POST /api/donations/` - Make a one-time donation.
  - `POST /api/donations/recurring/` - Set up recurring donations.
  - `GET /api/donations/history/` - View donation history.

## Installation

### Prerequisites
- Python 3.x
- Django 3.x or above
- PostgreSQL (or other database of choice)
- Stripe or PayPal API for payment processing (optional)

### Steps to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/church-app.git
   cd church-app
