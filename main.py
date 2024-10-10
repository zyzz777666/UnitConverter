from fastapi import FastAPI, HTTPException

from models.length import LengthConversionRequest, WeightConversionRequest, TemperatureConversionRequest
from conversion.conversion_factors import conversion_factors_length, conversion_factors_wight, \
    conversion_factors_temperature

app = FastAPI()


@app.post("/convert-length/")
async def convert_length(conversion_request: LengthConversionRequest):
    from_unit = conversion_request.from_unit.lower()
    to_unit = conversion_request.to_unit.lower()

    # Проверяем, существуют ли указанные единицы измерения
    if from_unit not in conversion_factors_length or to_unit not in conversion_factors_length:
        raise HTTPException(status_code=400, detail="Invalid unit of measurement")

    # Конвертируем значение в метры
    value_in_meters = conversion_request.value / conversion_factors_length[from_unit]

    # Конвертируем метры в целевую единицу измерения
    converted_value = value_in_meters * conversion_factors_length[to_unit]

    return {
        "original_value": conversion_request.value,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "converted_value": converted_value
    }


@app.post("/convert-weight/")
async def convert_weight(conversion_request: WeightConversionRequest):
    from_unit = conversion_request.from_unit.lower()
    to_unit = conversion_request.to_unit.lower()

    # Проверяем, существует ли указанные единицы веса
    if from_unit not in conversion_factors_wight or to_unit not in conversion_factors_wight:
        raise HTTPException(status_code=400, detail="Invalid unit of measurement")

    # Конвертируем значение в килограммы
    value_in_kilogram = conversion_request.value / conversion_factors_wight[from_unit]

    # Конвертируем килограммы в целивую единицу веса
    converted_value = value_in_kilogram * conversion_factors_wight[to_unit]

    return {
        "original_value": conversion_request.value,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "converted_value": converted_value
    }


@app.post("/convert-temperature/")
async def convert_temperature(conversion_request: TemperatureConversionRequest):
    from_unit = conversion_request.from_unit.lower()
    to_unit = conversion_request.to_unit.lower()

    # Проверяем, существует ли указанные единицы температуры
    if from_unit not in conversion_factors_temperature or to_unit not in conversion_factors_temperature:
        raise HTTPException(status_code=400, detail="Invalid unit of measurement")

    # Конвертируем значение в цельсии
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            converted_value = (conversion_request.value * 9 / 5) + 32
        elif to_unit == "kelvin":
            converted_value = conversion_request.value + 273.15
        else:
            converted_value = conversion_request.value

    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            converted_value = (conversion_request.value - 32) * 5 / 9
        elif to_unit == "kelvin":
            converted_value = (conversion_request.value - 32) * 5 / 9 + 273.15
        else:
            converted_value = conversion_request.value

    elif from_unit == "kelvin":
        if to_unit == "celsius":
            converted_value = conversion_request.value - 273.15
        elif to_unit == "fahrenheit":
            converted_value = (conversion_request.value - 273.15) * 9 / 5 + 32
        else:
            converted_value = conversion_request.value

    return {
        "original_value": conversion_request.value,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "converted_value": converted_value
    }
