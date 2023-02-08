from aiohttp import ClientSession
import asyncio
from more_itertools import chunked
from models import engine, Session, Character, Base
from typing import Optional, List

MAX_SIZE = 15


async def get_field_name(url: str, client: ClientSession, field_name: str = 'name') -> str:

    async with client.get(url) as response:
        json_data = await response.json()
    return json_data[field_name]


async def get_plurality_list(url_list: list, client: ClientSession, field_name: str = 'name') -> str:

    result = ','.join([await get_field_name(url, client, field_name) for url in url_list])
    return result


async def get_character(character_id: int, client: ClientSession) -> Optional[dict]:

    url = f'https://swapi.dev/api/people/{character_id}'
    async with client.get(url) as response:
        json_data = await response.json()

    if json_data.get('detail') == 'Not found':
        return None

    json_data['id'] = character_id

    del(json_data['created'], json_data['edited'], json_data['url'])

    try:
        json_data['mass'] = float(json_data['mass'].replace(',', '.'))
    except ValueError:
        json_data['mass'] = None
    try:
        json_data['height'] = int(json_data['height'])
    except ValueError:
        json_data['height'] = None

    json_data['films'] = await get_plurality_list(json_data['films'], client, 'title')
    json_data['homeworld'] = await get_field_name(json_data['homeworld'], client)
    json_data['species'] = await get_plurality_list(json_data['species'], client)
    json_data['starships'] = await get_plurality_list(json_data['starships'], client)
    json_data['vehicles'] = await get_plurality_list(json_data['vehicles'], client)

    return json_data


async def paste_to_db(character_list: List[Optional[dict]]) -> None:

    async with Session() as session:
        character_list = [Character(**item) for item in character_list if item]
        session.add_all(character_list)
        await session.commit()


async def main() -> None:

    tasks = []
    async with ClientSession() as client:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        for id_chunk in chunked(range(1, 100), MAX_SIZE):
            coros = [get_character(character_id, client) for character_id in id_chunk]
            character_list = await asyncio.gather(*coros)
            """
            проверка на пустые запросы, работает только если в базе элементы идут подряд 
            и если есть пустая последовательность, то дальше функция не работает
            """
            # try:
            #     if set(character_list) == {None}:
            #         return print('All Done!')
            # except TypeError:
            #     pass
            db_coro = paste_to_db(list(character_list))
            paste_to_db_task = asyncio.create_task(db_coro)
            tasks.append(paste_to_db_task)
    tasks = asyncio.all_tasks() - {asyncio.current_task()}
    for task in tasks:
        await task
    return print('All Done!')

asyncio.get_event_loop().run_until_complete(main())
