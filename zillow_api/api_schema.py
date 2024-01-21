"""
Dataclasses for Zillow API.
"""


import marshmallow
from marshmallow_dataclass import dataclass
from typing import Dict, List, Optional


@dataclass
class VariableData:
    text: Optional[str]
    type: Optional[str]


@dataclass
class listingSubType:
    class Meta:
        """Allow unknown fields since this is an undocumented API."""

        unknown = marshmallow.EXCLUDE

    is_FSBA: Optional[bool]
    "Property is for sale by owner"
    is_openHouse: Optional[bool]
    "There is an upcoming open house for this property. Details are not provided by API."


@dataclass
class Property:
    class Meta:
        """Allow unknown fields since this is an undocumented API."""

        unknown = marshmallow.EXCLUDE

    dateSold: Optional[str]
    "Date this property was last sold. Only if property isn't listed for sale" ""
    propertyType: str
    "What kind of property this is. Detached house, condo, etc."
    lotAreaValue: int
    "Lot size"
    address: str
    "Full address of property."
    variableData: VariableData
    "Miscellaneous data"
    zestimate: int
    "Zillow's estimate of property value."
    rentZestimate: int
    "Zillows estimate of for how much property could rent."
    price: int
    "Current List price of property."
    detailUrl: str
    "Page URL after zillow.com"
    bedrooms: int
    "Number of bedrooms property has"
    bathrooms: int
    "Number of bathrooms property has."
    contingentListingType: Optional[str]
    "Unsure, only have seen foreclosure"

    latitute: float
    "Latitude of property"
    longitude: float
    "longitude of property"
    listingStatus: str
    zpid: int
    "Zillow ID Number"
    daysOnZillow: int
    "Number of days property has been listed on Zillow."
    lotAreaUnit: str
    "Unit e.g. acre, sqft, which lot area is expressed."
    priceChange: Optional[int]
    "Difference of earlier for-sale price."


@dataclass
class ZillowResponse:
    """
    Zillow Search Response.
    """

    class Meta:
        """Allow unknown fields since this is an undocumented API."""

        unknown = marshmallow.EXCLUDE

    props: List[Property]
    resultsPerPage: int
    totalPages: int
    totalResultCount: int
    schools: Dict
    currentPage: int
