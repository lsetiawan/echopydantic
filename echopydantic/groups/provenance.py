from pydantic import Field, validator
from typing import Optional, List, Union, Tuple

from ..base_models import (
    BaseAttributes,
    BaseDimensions,
    BaseGroup,
    BaseDataVariables,
    BaseVariable,
)


class SourceFileNameAttrs(BaseAttributes):
    long_name: str = Field(default="Source filenames", description="")

    @validator('long_name')
    def long_name_default(cls, v):
        if v != "Source filenames":
            raise ValueError("must be 'Source filenames'")
        return v


class SourceFileName(BaseVariable):
    attributes: SourceFileNameAttrs = Field(...)
    data_type: str = "string"
    dimensions: Union[List[str], Tuple[str]] = ['filenames']

    @validator('dimensions')
    def dimesions_default(cls, v):
        if v != ['filenames']:
            raise ValueError("must be '['filenames']'")
        return v

    @validator('data_type')
    def data_type_default(cls, v):
        if v != 'string':
            raise ValueError("must be 'string'")
        return v


class GroupAttributes(BaseAttributes):
    conversion_software_name: Optional[str] = Field(
        default='echopype',
        description="""Name of the software used to do the conversion.""",
    )
    conversion_software_version: Optional[str] = Field(
        ...,
        description="""Version of the software used to do the conversion.""",
    )
    conversion_time: Optional[str] = Field(
        ...,
        description="""Date and time of the start of the conversion process in extended ISO8601:2005 extended format, including time zone (e.g. 2017-05-06T20:21:35Z).""",
    )

    @validator('conversion_software_name')
    def conversion_software_name_default(cls, v):
        if v != 'echopype':
            raise ValueError("must be 'echopype'")
        return v


class Dimensions(BaseDimensions):
    filenames: int = Field(
        default=0,
        description="""Can be of fixed or unlimited length, as appropriate.""",
    )


class DataVariables(BaseDataVariables):
    source_filenames: SourceFileName = Field(...)


class Provenance(BaseGroup):
    attributes: GroupAttributes = Field(...)
    dimensions: Dimensions = Field(...)
    variables: DataVariables = Field(...)
