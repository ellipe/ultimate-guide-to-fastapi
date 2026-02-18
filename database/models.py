from datetime import datetime
from enum import Enum
import uuid
from sqlmodel import SQLModel, Field

class ShipmentStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    IN_TRANSIT = "in transit"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    RETURNED = "returned"
    LOST = "lost"
    DAMAGED = "damaged"
    OTHER = "other" 

class Shipment(SQLModel, table=True):
    __tablename__ = "shipments"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    content: str
    weight: float = Field(le=25, ge=0)
    destination: str
    tracking_number: str = Field(index=True)
    status: ShipmentStatus = Field(default=ShipmentStatus.PENDING)
    carrier: str = Field(default="unknown")
    estimated_delivery: datetime
    current_location: str = Field(default="unknown")