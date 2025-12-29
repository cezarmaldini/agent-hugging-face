from pydantic import BaseModel, Field

def get_temperature(city: str):
    """
    Get the current weather in a given city.
    """
    if city.lower() == "san francisco":
        return "72"
    if city.lower() == "paris":
        return "75"
    if city.lower() == "tokyo":
        return "73"
    return "70"


class GetTemperatureArgs(BaseModel):
    city: str = Field(description="A cidade para onde se deve obter a temperatura.")
    
schema_tools = {
    "type": "function",
    "function": {
        "name": "get_temperature",
        "description": "Obtenha a temperatura atual em uma determinada cidade.",
        "parameters": GetTemperatureArgs.model_json_schema()
    }
}