from src.data.dao import DataDAO
from fastapi import HTTPException, status


async def add_data_logic(**values):
    check_email = await DataDAO.get_all_data(email = values.get('email'))
    check_phone = await DataDAO.get_all_data(phone_number = values.get('phone_number'))
    if check_email or check_phone:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Данные данные уже были добавлены')
    data = await DataDAO.add_data(**values)
    return data