from pydantic import BaseModel, Field
from .toplevel import Toplevel
from .groups.provenance import Provenance


class EchoData(BaseModel):
    toplevel: Toplevel = Field(...)
    provenance: Provenance = Field(...)
