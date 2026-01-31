# Shipment Tracking API - Learning Project

A FastAPI-based shipment tracking API built as part of a Python learning course. This project demonstrates building RESTful APIs with FastAPI, handling HTTP requests, and managing data structures.

## Project Overview

This is a learning project focused on:
- Building REST APIs with FastAPI
- Working with Python dictionaries and data structures
- Handling HTTP requests and responses
- Error handling with HTTP exceptions
- API documentation with Scalar

## Features

### Current Implementation

- **Shipment Data Storage**: In-memory dictionary storing shipment information with tracking numbers as keys
- **API Endpoints**:
  - `GET /shipment/latest` - Returns the most recent shipment (by tracking number)
  - `GET /shipment/{tracking_number}` - Returns a specific shipment by tracking number
  - `GET /scalar` - Interactive API documentation (Scalar UI)

### Shipment Data Structure

Each shipment contains:
- `tracking_number`: Unique identifier (integer)
- `content`: Description of the shipment
- `status`: Current status (e.g., "in transit", "delivered", "pending")
- `carrier`: Shipping carrier (UPS, FedEx, DHL, USPS)
- `estimated_delivery`: Expected delivery date
- `current_location`: Current location of the shipment
- `destination`: Final destination
- `shipment_date`: Date the shipment was created
- `delivery_date`: Actual delivery date (null if not delivered)
- `tracking_url`: URL to carrier's tracking page
- `tracking_status`: Current tracking status
- `tracking_history`: Array of tracking events with date, location, and status

## Getting Started

### Prerequisites

- Python 3.14+
- `uv` package manager (or pip)

### Installation

1. Install dependencies:
```bash
uv sync
# or
pip install -r requirements.txt
```

2. Run the development server:
```bash
uvicorn main:app --reload
# or
fastapi dev main.py
```

3. Access the API:
- API: http://localhost:8000
- Interactive Docs: http://localhost:8000/scalar
- OpenAPI Schema: http://localhost:8000/openapi.json

## API Endpoints

### Get Latest Shipment

```http
GET /shipment/latest
```

Returns the shipment with the highest tracking number.

**Response:**
```json
{
  "tracking_number": 7890123456,
  "content": "sports equipment",
  "status": "delivered",
  ...
}
```

### Get Shipment by Tracking Number

```http
GET /shipment/{tracking_number}
```

Returns a specific shipment by its tracking number.

**Parameters:**
- `tracking_number` (path, integer): The tracking number to look up

**Response (200 OK):**
```json
{
  "tracking_number": 1234567890,
  "content": "wooden table",
  "status": "in transit",
  ...
}
```

**Response (404 Not Found):**
```json
{
  "detail": "Shipment not found"
}
```

## Learning Notes

### What We've Learned So Far

1. **FastAPI Basics**
   - Creating a FastAPI application instance
   - Defining route handlers with decorators
   - Type hints for request/response validation

2. **Data Structures**
   - Working with nested dictionaries
   - Dictionary keys as tracking numbers (integers)
   - Complex nested data (tracking history arrays)

3. **Error Handling**
   - Using `HTTPException` for proper error responses
   - 404 status codes for not found resources

4. **API Design**
   - RESTful endpoint design
   - Path parameters
   - Response type annotations

### Sample Shipments

The project includes 7 sample shipments with various:
- Carriers (UPS, FedEx, DHL, USPS)
- Statuses (in transit, delivered, pending)
- Locations across the United States
- Different tracking histories

## Project Structure

```
app/
├── main.py              # FastAPI application and routes
├── pyproject.toml       # Project dependencies and metadata
├── uv.lock             # Dependency lock file
└── README.md           # This file
```

## Next Steps (Learning Goals)

Potential features to add as we continue learning:
- [ ] POST endpoint to create new shipments
- [ ] PUT/PATCH endpoints to update shipments
- [ ] DELETE endpoint to remove shipments
- [ ] Query parameters for filtering/searching
- [ ] Database integration (SQLite, PostgreSQL)
- [ ] Data validation with Pydantic models
- [ ] Authentication and authorization
- [ ] Testing with pytest
- [ ] Docker containerization

## Development Notes

This is a learning project, so the code structure and patterns may evolve as we learn new concepts and best practices.
