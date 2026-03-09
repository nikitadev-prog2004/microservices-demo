import httpx
from app.config import get_settings


def team_exists(team_id: int) -> bool:
    url = get_settings().team_service_url
    response = httpx.get(f"{url}{team_id}")
    return response.status_code == 200
