from fastapi import FastAPI

app = FastAPI(docs_url='/')


@app.get("/")
async def home():
    return {"Hello": "World"}


@app.get('/users', tags=['This method for users'], description='This method for get all users')
async def users():
    return {'User': 'John'}


@app.get('/продукты', tags=['This method for products'])
async def users():
    return {'products': 'test'}


@app.post('/products', tags=['This method for products'])
async def users(title: str, price: int, description: str):
    return {'products': f'Название: {title} Цена: ${price}, Описание: {description}'}


# Параметры для запроса
@app.get('/param-example')
async def param(user_id: int, user_answer: str):
    return {'message': f'У этого пользователя {user_id} ID, 10 ответов и этот ответ: {user_answer}'}


@app.put('/products', tags=['This method for products'])
async def product_change(title: str, price: int, description: str):
    return {'Update info': f'Новые данные: {title}, новая цена: {price}, новое описание: {description}'}


@app.delete('/products', tags=['This method for products'])
async def delete(title: str):
    return {'Ответ': f'Этот продукт: {title} удалён из базы!'}

