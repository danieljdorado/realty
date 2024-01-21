"""
Dataclasses for Zillow API.
"""


from typing import Dict, List, Optional
from marshmallow_dataclass import dataclass

import marshmallow

# Schema for the Search API. This returns a list of properties and essential data
# that can be used for refining results.
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
class SearchProperty:
    class Meta:
        """Allow unknown fields since this is an undocumented API."""

        unknown = marshmallow.EXCLUDE

    dateSold: Optional[str]
    "Date this property was last sold. Only if property isn't listed for sale" ""
    propertyType: str
    "What kind of property this is. Detached house, condo, etc."
    lotAreaValue: float
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
class ZillowSearchResponse:
    """
    Zillow Search Response.
    """

    class Meta:
        """Allow unknown fields since this is an undocumented API."""

        unknown = marshmallow.EXCLUDE

    props: List[SearchProperty]
    resultsPerPage: int
    totalPages: int
    totalResultCount: int
    schools: Dict
    currentPage: int


# Schema for Individual Properties.

@dataclass
class Address:
    """Property Address"""
    community: Optional[str]
    city: str
    neighborhood: Optional[str]
    subdivision: Optional[str]
    streetAddress: str
    zipcode: int

@dataclass
class MortgageRates:
    "Mortgage Rate Data."
    thirtyYearFixedRate: float

@dataclass
class ZillowPropertyResponse:
    """Class representing the Returned Response Object for a Specific Property."""
    zpid: int
    "Zillow Property ID"
    propertyTaxRate: float
    address: Address
    timeOnZillow: str
    zestimate: int
    description: str
    price: int
    livingAreaValue: int
    rentZestimate: int
    bathrooms: int
    annualHomeownersInsurance: int
    yearBuilt: int
    pageViewCount: int
    "How many times this page as been viewed on Zillow."
    mortgageRates: MortgageRates
    monthlyHoaFee: Optional[int]
    homeStatus: str
    "Listing status. For sale, sold, etc."
    homeFacts: Optional[str]
    latitude: float
    # TODO: Set this as datetime.
    datePosted: str
    bedrooms: int
    livingArea: int
    favoriteCount: int
    "How many users have favorited this property."
