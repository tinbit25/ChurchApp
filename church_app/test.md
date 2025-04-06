
---

# API Test Suite for Church App

This README provides the test cases and expected body information for testing the following endpoints of the church app API:

1. **Register**
2. **Login**
3. **Profile**
4. **Events**
5. **Donation**

## 1. **Register API**

**Endpoint:** `/api/auth/register/`  
**Method:** `POST`  
**Description:** Register a new user.

**Body:**

```json
{
    "username": "tinbite_elis",
    "password": "securepassword123",
    "email": "tinbite_elis@example.com",
    "role": "member"
}
```

**Expected Response:**

- Status: `201 Created`
- Message: Successfully registered the user.

---

## 2. **Login API**

**Endpoint:** `/api/auth/login/`  
**Method:** `POST`  
**Description:** Login to the app and get JWT tokens (access and refresh).

**Body:**

```json
{
    "username": "tinbite_elis",
    "password": "securepassword123"
}
```

**Expected Response:**

- Status: `200 OK`
- Tokens:  
  - `access`: Access token used for subsequent requests.
  - `refresh`: Refresh token used to obtain a new access token.

Example response:

```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## 3. **Profile API**

**Endpoint:** `/api/auth/profile/`  
**Method:** `GET`  
**Description:** Get the authenticated user's profile details.

**Headers:**  
- `Authorization: Bearer {access_token}`  

**Expected Response:**

- Status: `200 OK`
- Body: The details of the logged-in user, including `username`, `email`, and `role`.

Example response:

```json
{
    "id": 1,
    "username": "tinbite_elis",
    "email": "tinbite_elis@example.com",
    "role": "member",
    "date_joined": "2025-04-06T10:00:00Z"
}
```

---

## 4. **Events API**

### a. **Create Event**

**Endpoint:** `/api/events/`  
**Method:** `POST`  
**Description:** Create a new event.

**Body:**

```json
{
    "title": "Easter Sunday Service",
    "description": "Join us for the Easter Sunday Service.",
    "date": "2025-04-12",
    "time": "10:00:00",
    "location": "Church Auditorium",
    "created_by": 1  // Use the ID of the logged-in user
}
```

**Expected Response:**

- Status: `201 Created`
- Body: Event details with the `created_by` field set to the logged-in user's ID.

---

### b. **List Events**

**Endpoint:** `/api/events/`  
**Method:** `GET`  
**Description:** List all events.

**Expected Response:**

- Status: `200 OK`
- Body: A list of events.

Example response:

```json
[
    {
        "id": 1,
        "title": "Easter Sunday Service",
        "description": "Join us for the Easter Sunday Service.",
        "date": "2025-04-12",
        "time": "10:00:00",
        "location": "Church Auditorium",
        "created_by": 1
    }
]
```

---

## 5. **Donation API**

### a. **Make a Donation**

**Endpoint:** `/api/donations/`  
**Method:** `POST`  
**Description:** Make a donation to the church.

**Body:**

```json
{
    "donation_type": "one-time",  // or "recurring"
    "amount": 100.00,
    "user": 1  // Use the ID of the logged-in user
}
```

**Expected Response:**

- Status: `201 Created`
- Body: Donation details, including the `user` ID and `donation_type`.

Example response:

```json
{
    "id": 1,
    "donation_type": "one-time",
    "amount": 100.00,
    "user": 1,
    "timestamp": "2025-04-06T12:00:00Z"
}
```

---

## Test Process for Video Presentation:

### **Test 1: Register User**
1. Open Postman.
2. Set the method to `POST`.
3. Set the URL to `http://localhost:8000/api/auth/register/`.
4. In the body, provide the `username`, `password`, `email`, and `role`.
5. Send the request and verify the user is registered successfully.

### **Test 2: Login User**
1. Open Postman.
2. Set the method to `POST`.
3. Set the URL to `http://localhost:8000/api/auth/login/`.
4. In the body, provide the `username` and `password`.
5. Send the request and check that the `access` and `refresh` tokens are returned.

### **Test 3: View Profile**
1. Open Postman.
2. Set the method to `GET`.
3. Set the URL to `http://localhost:8000/api/auth/profile/`.
4. Add the `Authorization` header with the `access` token.
5. Send the request and verify the profile details are returned correctly.

### **Test 4: Create Event**
1. Open Postman.
2. Set the method to `POST`.
3. Set the URL to `http://localhost:8000/api/events/`.
4. In the body, provide event details like `title`, `description`, `date`, `time`, `location`, and `created_by` (use the logged-in user's ID).
5. Send the request and verify that the event is created successfully.

### **Test 5: Make Donation**
1. Open Postman.
2. Set the method to `POST`.
3. Set the URL to `http://localhost:8000/api/donations/`.
4. In the body, provide the `donation_type`, `amount`, and `user` (use the logged-in user's ID).
5. Send the request and verify that the donation is processed correctly.

---
