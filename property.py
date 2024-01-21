"""
Internal property model.
"""

import re
from dataclasses import dataclass
from typing import Dict, Optional


us_address_regex = re.compile(
    r"""
    ^                           # Start of string
    (?P<street_number>\d+)      # Named Group: Match one or more digits (street number)
    \s+                         # Match one or more whitespace characters
    (?P<street_name>[\w\s.#-]+)  # Named Group: Match street name (alphanumeric, spaces, dots, hyphens)
    ,\s*                        # Match comma and optional whitespace
    (?P<city>[\w\s.-]+)         # Named Group: Match city (alphanumeric, spaces, dots, hyphens)
    ,\s*                        # Match comma and optional whitespace
    (?P<state>\w{2})            # Named Group: Match state abbreviation (two letters)
    \s*                         # Match optional whitespace
    (?P<zip_code>\d{5}(?:-\d{4})?)?  # Named Group: Match ZIP code (optional +4 extension)
    $                           # End of string
""",
    re.VERBOSE,
)


@dataclass
class Property:
    """
    Dataclass representing a Property.
    """

    zpid: int
    property_type: str
    beds: int
    baths: int
    listing_status: str
    price: int
    price_zestimate: int
    rent_zestimate: int
    street_number: Optional[int]
    street_name: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[int]


def build_property(prop: Dict) -> Property:
    """
    Build a normalized dataclass representing a property.
    :param prop: Property data.
    :return: Property dataclass.
    """

    # Parse Address
    match = us_address_regex.match(prop["address"])
    if match:
        street_number: Optional[int] = int(match.group("street_number"))
        street_name: Optional[str] = match.group("street_name")
        city: Optional[str] = match.group("city")
        state: Optional[str] = match.group("state")
        zip_code: Optional[int] = int(match.group("zip_code"))
    else:
        street_number = None
        street_name = None
        city = None
        state = None
        zip_code = None

    return Property(
        zpid=prop["zpid"],
        property_type=prop["propertyType"],
        beds=prop["bedrooms"],
        baths=prop["bathrooms"],
        listing_status=prop["listingStatus"],
        price=prop["price"],
        price_zestimate=prop["zestimate"],
        rent_zestimate=prop["rentZestimate"],
        # Address
        street_number=street_number,
        street_name=street_name,
        city=city,
        state=state,
        zip_code=zip_code,
    )
