import datetime
import httpx
import json
from typing import List
from wbnotifierbot import config



class Wildberries:
    def __init__(self):
        pass
        
        
        
async def stocks() -> List[dict]:
    '''Остатки товаров на складах WB
    Данная функция возвращает данные по остаткам на складах для всех артикулов на вчерашних день
    :quantity в ответе - остаток на всех складах'''
    
    date_yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    headers = {"Authorization": config.WBAPISTATISTIC, "content-Type": "application/json"}
    api_url = config.WBURLGETSTOCKS+"?dateFrom="+date_yesterday
    async with httpx.AsyncClient() as client:
...     response = await client.get(api_url, headers=headers, json=request_body)
    return response.json()



async def detail(nmID: int) -> dict:
    '''Получение статистики КТ за выбранный период, по nmID'''
    
    date_time_from = (datetime.datetime.today() - datetime.timedelta(days=8)).strftime("%Y-%m-%d 00:00:00")
    date_time_to = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d 00:00:00")
    request_body = {
        "nmIDs": [nmID],
        "timezone": "Europe/Moscow",
        "period": {
            "begin": date_time_from,
            "end": date_time_to
        },
        "orderBy": {
            "field": "ordersSumRub",
            "mode": "asc"
        },
        "page": 1
    }
    headers = {"Authorization": config.WBAPISTANDART, "content-Type": "application/json"}
    async with httpx.AsyncClient() as client:
        await response = client.post(config.WBURLGETDETAIL, headers=headers, json=request_body)
    return response.json()


