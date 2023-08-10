from typing import TypeVar, Generic, Optional

from pydantic import BaseModel, Field

T = TypeVar('T')


class ApiResponse(BaseModel, Generic[T]):
    content: T
    status_code: int = Field(..., alias="statusCode")
    message: Optional[str]
    pass
