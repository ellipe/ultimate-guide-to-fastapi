from pydantic import BaseModel, create_model
from typing import Optional, get_origin, get_args


class TrackingHistoryItem(BaseModel):
    date: str
    location: str
    status: str


class Shipment(BaseModel):
    id: int
    tracking_number: int
    content: str
    status: str
    carrier: str
    estimated_delivery: str
    current_location: str
    destination: str
    shipment_date: str
    delivery_date: Optional[str]
    tracking_url: str
    tracking_status: str
    tracking_history: list[TrackingHistoryItem]


class ShipmentCreate(BaseModel):
    content: str
    carrier: str
    destination: str


class MessageResponse(BaseModel):
    message: str


# Create a partial model where all fields from Shipment are optional
# This is cleaner than manually listing all Optional fields
# Using Pydantic's model creation to automatically generate optional fields
def create_optional_model(base_model: type[BaseModel], name_suffix: str = "Update") -> type[BaseModel]:
    """Dynamically create a model with all fields optional from a base model."""
    field_definitions = {}
    for field_name, field_info in base_model.model_fields.items():
        annotation = field_info.annotation
        # Check if the type is already Optional (Union[Type, None])
        # get_origin(Optional[str]) returns Union, get_args gives us (str, type(None))
        origin = get_origin(annotation)
        if origin is not None and type(None) in get_args(annotation):
            # Already Optional, keep it as is
            field_type = annotation
        else:
            # Not Optional yet, wrap it
            field_type = Optional[annotation]
        field_definitions[field_name] = (field_type, None)
    
    return create_model(
        f"{base_model.__name__}{name_suffix}",
        __base__=BaseModel,
        **field_definitions
    )


ShipmentUpdate = create_optional_model(Shipment)