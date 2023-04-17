from fastapi import APIRouter

from src.models.models import NodalCalcRequest, NodalCalcResponse

main_router = APIRouter(prefix="/nodal", tags=["NodalAnalysis"])


@main_router.post("/calc", response_model=NodalCalcResponse)
async def my_profile(data: NodalCalcRequest):
    """
    Эндпоинт для выполнения Узлового Анализа
    """
    # Функция для выполнения узлового анализа
    from src.calculations.nodal import calc_nodal

    return calc_nodal(data.vlp.dict(), data.ipr.dict())
