"""
Internal Realty Domain model.
"""

import re
from dataclasses import dataclass
from typing import Dict, Optional


us_address_regex = re.compile(
    r"""
    ^                           # Start of string
    (?P<street_number>\d+)      # Named Group: Match one or more digits (street number)
    \s+                         # Match one or more whitespace characters
    (?P<street_name>[\w\s.#-]+)
    # Named Group: Match street name (alphanumeric, spaces, dots, hyphens)
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
class SearchPropertyRow:
    """
    Dataclass representing a brief summary of a Property from searching.
    Corresponds to a single row in a tsv from a search query.
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


def build_property_search_row(prop: Dict) -> SearchPropertyRow:
    """
    Build a normalized dataclass representing a property. Each Property is a high level
    summary of essential details.
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

    return SearchPropertyRow(
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


@dataclass
class RealtyProperty:
    """Dataclass representing land and buildings on it and natural resources."""

    zpid: int
    price: int
    "Asking price, sold for or rent price."
    property_tax_rate: float
    time_on_zillow: str
    zestimate: int
    rent_zestimate: str
    lot_size: Optional[int]
    "Lot size in square feet."
    annual_homeowners_insurance: int
    beds: int
    baths: int
    description: str
    living_area_value: int
    year_built: int
    page_view_count: int
    home_status: str
    monthly_hoa_fee: Optional[int]


def get_lot_size(lot_string) -> Optional[int]:
    """Get lot size
    Assume that this will always be sqft.
    """

    if lot_string:
        lot = lot_string.split()
        return int(lot[0].replace(",", ""))
    return None


def build_realty_property(prop: Dict) -> RealtyProperty:
    """Build Realty Property"""

    return RealtyProperty(
        zpid=prop["zpid"],
        price=prop["price"],
        property_tax_rate=prop["propertyTaxRate"],
        time_on_zillow=prop["timeOnZillow"],
        zestimate=prop["zestimate"],
        rent_zestimate=prop["rentZestimate"],
        lot_size=get_lot_size(prop["resoFacts"]["lotSize"]),
        annual_homeowners_insurance=prop["annualHomeownersInsurance"],
        beds=prop["bedrooms"],
        baths=prop["bathrooms"],
        description=prop["description"],
        living_area_value=prop["livingAreaValue"],
        year_built=prop["yearBuilt"],
        page_view_count=prop["pageViewCount"],
        home_status=prop["homeStatus"],
        monthly_hoa_fee=prop["monthlyHoaFee"],
    )
