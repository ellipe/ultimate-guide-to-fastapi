from typing import List
from fastapi import FastAPI, HTTPException
from scalar_fastapi import get_scalar_api_reference
from schemas import Shipment, ShipmentCreate, ShipmentUpdate, MessageResponse
from database import Database

app = FastAPI()
db = Database()


@app.get("/shipments/{id}", response_model=Shipment)
def get_shipment(id: int) -> Shipment:
    shipment = db.get_shipment(id)
    if shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return Shipment(**shipment)

@app.get("/shipments", response_model=List[Shipment])
def get_all_shipments() -> List[Shipment]:
    return [Shipment(**shipment) for shipment in db.get_all_shipments()]

@app.post("/shipments", response_model=Shipment)
def create_shipment(shipment: ShipmentCreate) -> Shipment:
    created = db.add_shipment(shipment)
    return Shipment(**created)

@app.put("/shipments/{id}", response_model=Shipment)
def update_shipment(id: int, shipment: ShipmentUpdate) -> Shipment:
    updated_shipment = db.update_shipment(id, shipment)
    return Shipment(**updated_shipment)

@app.patch("/shipments/{id}", response_model=Shipment)
def patch_shipment(id: int, shipment: ShipmentUpdate) -> Shipment:
    updated_shipment = db.update_shipment(id, shipment)
    return Shipment(**updated_shipment)

@app.delete("/shipments/{id}", response_model=MessageResponse)
def delete_shipment(id: int) -> MessageResponse:
    db.delete_shipment(id)
    return MessageResponse(message="Shipment deleted successfully")

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
