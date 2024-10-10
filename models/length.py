from pydantic import BaseModel


class LengthConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str


class WeightConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str


class TemperatureConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str
