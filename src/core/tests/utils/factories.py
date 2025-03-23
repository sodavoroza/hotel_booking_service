import random
import string
from datetime import date, timedelta
from typing import Any, Dict, Union


def random_string(length: int = 5) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


def get_id(obj_or_dict: Union[Dict[str, Any], Any]) -> Any:
    return obj_or_dict.id if hasattr(obj_or_dict, "id") else obj_or_dict["id"]


def hotel_payload(strict: bool = False, **overrides: Any) -> Dict[str, Any]:
    if strict:
        payload = {
            "name": "Test Hotel",
            "address": "Test Address",
            "city": "Test City",
            "location": "Test Location",
        }
    else:
        payload = {
            "name": overrides.get("name", f"Hotel {random_string()}"),
            "address": overrides.get("address", f"{random.randint(1, 999)} Main St"),
            "city": overrides.get("city", "Cityville"),
            "location": overrides.get("location", "Downtown"),
        }
    return {**payload, **overrides}


def room_payload_api(
    hotel: Any, strict: bool = False, **overrides: Any
) -> Dict[str, Any]:
    hotel_id = get_id(hotel)
    if strict:
        payload = {
            "hotel": hotel_id,
            "number": "101",
            "capacity": 2,
            "price_per_night": 100.00,
            "address": "Standard Room",
        }
    else:
        payload = {
            "hotel": hotel_id,
            "number": overrides.get("number", str(random.randint(100, 999))),
            "capacity": overrides.get("capacity", random.choice([1, 2, 3, 4])),
            "price_per_night": overrides.get(
                "price_per_night", round(random.uniform(50.0, 300.0), 2)
            ),
            "address": overrides.get("address", f"Floor {random.randint(1, 10)}"),
        }
    return {**payload, **overrides}


def room_payload_model(hotel: Any, **overrides: Any) -> Dict[str, Any]:
    payload = room_payload_api(hotel, **overrides)
    payload["hotel"] = hotel
    return payload


def booking_payload_api(
    room: Any, strict: bool = False, **overrides: Any
) -> Dict[str, Any]:
    room_id = get_id(room)
    today = date.today()
    if strict:
        payload = {
            "room": room_id,
            "guest_name": "John Doe",
            "check_in": today.isoformat(),
            "check_out": (today + timedelta(days=3)).isoformat(),
        }
    else:
        payload = {
            "room": room_id,
            "guest_name": overrides.get("guest_name", f"Guest {random_string()}"),
            "check_in": overrides.get(
                "check_in", (today + timedelta(days=1)).isoformat()
            ),
            "check_out": overrides.get(
                "check_out", (today + timedelta(days=5)).isoformat()
            ),
        }
    return {**payload, **overrides}
