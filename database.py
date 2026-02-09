import random
import sqlite3
from typing import Any

from schemas import Shipment, ShipmentCreate

# Column order for SELECT * FROM shipments
_SHIPMENT_ROW_KEYS = (
    "id",
    "tracking_number",
    "content",
    "status",
    "carrier",
    "estimated_delivery",
    "current_location",
    "destination",
    "shipment_date",
    "delivery_date",
    "tracking_url",
    "tracking_status",
)


def _row_to_shipment_dict(row: tuple[Any, ...]) -> dict[str, Any]:
    """Convert a shipments row tuple to a dict suitable for Shipment(**kwargs)."""
    d = dict(zip(_SHIPMENT_ROW_KEYS, row))
    d["id"] = row[0]  # ensure int
    d["tracking_number"] = int(d["tracking_number"]) if d.get("tracking_number") is not None else None
    d["tracking_history"] = []
    return d


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('shipments.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_shipments_table()
        # self.create_tracking_history_table()
        # self.create_tracking_events_table()

    def create_shipments_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS shipments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tracking_number TEXT,
                content TEXT,
                status TEXT,
                carrier TEXT,
                estimated_delivery TEXT,
                current_location TEXT,
                destination TEXT,
                shipment_date TEXT,
                delivery_date TEXT,
                tracking_url TEXT,
                tracking_status TEXT
            )
        """)

    def close(self):
        self.conn.close()

    def add_shipment(self, shipment: ShipmentCreate) -> dict[str, Any]:
        """Insert a new shipment from create payload; DB generates id, we generate tracking_number and defaults."""
        tracking_number = random.randint(1000000000, 9999999999)
        content = shipment.content or "No content"
        status = "in transit"
        carrier = shipment.carrier
        estimated_delivery = "2026-01-31"
        current_location = "New York, NY"
        destination = shipment.destination
        shipment_date = "2026-01-29"
        delivery_date = None
        tracking_url = f"https://www.ups.com/track?tracking_number={tracking_number}"
        tracking_status = "in transit"
        self.cursor.execute('''
            INSERT INTO shipments (tracking_number, content, status, carrier, estimated_delivery, current_location, destination, shipment_date, delivery_date, tracking_url, tracking_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (tracking_number, content, status, carrier, estimated_delivery, current_location, destination, shipment_date, delivery_date, tracking_url, tracking_status))
        self.conn.commit()
        result = self.get_shipment(self.cursor.lastrowid)
        assert result is not None, "inserted row should exist"
        return result

    def get_shipment(self, id: int) -> dict[str, Any] | None:
        self.cursor.execute('''
            SELECT * FROM shipments WHERE id = ?
        ''', (id,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        return _row_to_shipment_dict(row)

    def get_all_shipments(self) -> list[dict[str, Any]]:
        self.cursor.execute("""
            SELECT * FROM shipments
        """)
        return [_row_to_shipment_dict(row) for row in self.cursor.fetchall()]

    def update_shipment(self, id: int, shipment: Shipment):
        self.cursor.execute('''
            UPDATE shipments SET content = ?, status = ?, carrier = ?, estimated_delivery = ?, current_location = ?, destination = ?, shipment_date = ?, delivery_date = ?
            WHERE id = ?
        ''', (shipment.content, shipment.status, shipment.carrier, shipment.estimated_delivery, shipment.current_location, shipment.destination, shipment.shipment_date, shipment.delivery_date, id))
        self.conn.commit()
        return self.get_shipment(id)

    def delete_shipment(self, id: int):
        self.cursor.execute('''
            DELETE FROM shipments WHERE id = ?
        ''', (id,))
        self.conn.commit()