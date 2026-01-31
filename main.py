from typing import Any
from fastapi import FastAPI, HTTPException
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

shipments: dict[int, dict[str, Any]] = {
    1234567890: {
        "tracking_number": 1234567890,
        "content": "wooden table",
        "status": "in transit",
        "carrier": "UPS",
        "estimated_delivery": "2026-01-31",
        "current_location": "New York, NY",
        "destination": "Los Angeles, CA",
        "shipment_date": "2026-01-29",
        "delivery_date": "2026-02-01",
        "tracking_url": "https://www.ups.com/track?tracking_number=1234567890",
        "tracking_status": "in transit",
        "tracking_history": [
            {
                "date": "2026-01-29",
                "location": "New York, NY",
                "status": "in transit",
            },
        ],
    },
    2345678901: {
        "tracking_number": 2345678901,
        "content": "electronics package",
        "status": "delivered",
        "carrier": "FedEx",
        "estimated_delivery": "2026-02-05",
        "current_location": "San Francisco, CA",
        "destination": "Seattle, WA",
        "shipment_date": "2026-02-01",
        "delivery_date": "2026-02-04",
        "tracking_url": "https://www.fedex.com/track?tracking_number=2345678901",
        "tracking_status": "delivered",
        "tracking_history": [
            {
                "date": "2026-02-01",
                "location": "San Francisco, CA",
                "status": "in transit",
            },
            {
                "date": "2026-02-03",
                "location": "Portland, OR",
                "status": "in transit",
            },
            {
                "date": "2026-02-04",
                "location": "Seattle, WA",
                "status": "delivered",
            },
        ],
    },
    3456789012: {
        "tracking_number": 3456789012,
        "content": "furniture set",
        "status": "pending",
        "carrier": "DHL",
        "estimated_delivery": "2026-02-10",
        "current_location": "Miami, FL",
        "destination": "Atlanta, GA",
        "shipment_date": "2026-02-05",
        "delivery_date": None,
        "tracking_url": "https://www.dhl.com/track?tracking_number=3456789012",
        "tracking_status": "pending",
        "tracking_history": [
            {
                "date": "2026-02-05",
                "location": "Miami, FL",
                "status": "pending",
            },
        ],
    },
    4567890123: {
        "tracking_number": 4567890123,
        "content": "clothing order",
        "status": "in transit",
        "carrier": "USPS",
        "estimated_delivery": "2026-02-08",
        "current_location": "Chicago, IL",
        "destination": "Boston, MA",
        "shipment_date": "2026-02-03",
        "delivery_date": None,
        "tracking_url": "https://www.usps.com/track?tracking_number=4567890123",
        "tracking_status": "in transit",
        "tracking_history": [
            {
                "date": "2026-02-03",
                "location": "Chicago, IL",
                "status": "in transit",
            },
            {
                "date": "2026-02-06",
                "location": "Cleveland, OH",
                "status": "in transit",
            },
        ],
    },
    5678901234: {
        "tracking_number": 5678901234,
        "content": "books collection",
        "status": "delivered",
        "carrier": "UPS",
        "estimated_delivery": "2026-01-28",
        "current_location": "Denver, CO",
        "destination": "Phoenix, AZ",
        "shipment_date": "2026-01-25",
        "delivery_date": "2026-01-27",
        "tracking_url": "https://www.ups.com/track?tracking_number=5678901234",
        "tracking_status": "delivered",
        "tracking_history": [
            {
                "date": "2026-01-25",
                "location": "Denver, CO",
                "status": "in transit",
            },
            {
                "date": "2026-01-26",
                "location": "Albuquerque, NM",
                "status": "in transit",
            },
            {
                "date": "2026-01-27",
                "location": "Phoenix, AZ",
                "status": "delivered",
            },
        ],
    },
    6789012345: {
        "tracking_number": 6789012345,
        "content": "appliance delivery",
        "status": "in transit",
        "carrier": "FedEx",
        "estimated_delivery": "2026-02-12",
        "current_location": "Dallas, TX",
        "destination": "Houston, TX",
        "shipment_date": "2026-02-07",
        "delivery_date": None,
        "tracking_url": "https://www.fedex.com/track?tracking_number=6789012345",
        "tracking_status": "in transit",
        "tracking_history": [
            {
                "date": "2026-02-07",
                "location": "Dallas, TX",
                "status": "in transit",
            },
        ],
    },
    7890123456: {
        "tracking_number": 7890123456,
        "content": "sports equipment",
        "status": "delivered",
        "carrier": "DHL",
        "estimated_delivery": "2026-02-02",
        "current_location": "Las Vegas, NV",
        "destination": "San Diego, CA",
        "shipment_date": "2026-01-30",
        "delivery_date": "2026-02-01",
        "tracking_url": "https://www.dhl.com/track?tracking_number=7890123456",
        "tracking_status": "delivered",
        "tracking_history": [
            {
                "date": "2026-01-30",
                "location": "Las Vegas, NV",
                "status": "in transit",
            },
            {
                "date": "2026-02-01",
                "location": "San Diego, CA",
                "status": "delivered",
            },
        ],
    },
}


@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    return shipments[max(shipments.keys())]


@app.get("/shipment/{tracking_number}")
def get_shipment(tracking_number: int) -> dict[str, Any]:
    if tracking_number not in shipments:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipments[tracking_number]


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        # Your OpenAPI document
        openapi_url=app.openapi_url,
        title="Scalar API",
        # Avoid CORS issues (optional)
        scalar_proxy_url="https://proxy.scalar.com",
        dark_mode=True,
    )
