from typing import List, Tuple, Union, Optional
from pydantic import BaseModel, Field


class BaseAttributes(BaseModel):
    # TODO: Need date format validator for attributes
    # ISO8601:2004 extended format
    pass


class BaseDataVariables(BaseModel):
    pass


class BaseVariable(BaseModel):
    data_type: str = Field(default="", description="Variable data type.")
    dimensions: Union[List[str], Tuple[str]] = Field(
        default=[], description="Variable associated dimensions"
    )
    attributes: Optional[BaseAttributes]


class BaseDimensions(BaseModel):
    pass


class BaseCoordinates(BaseModel):
    pass


class BaseGroup(BaseModel):
    attributes: Optional[BaseAttributes]
    dimensions: Optional[BaseDimensions]
    variables: Optional[BaseDataVariables]
    coordinates: Optional[BaseCoordinates]
