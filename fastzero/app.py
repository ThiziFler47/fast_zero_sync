from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fastzero.schemas import (
    MessageSchema,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {'message': 'Hello World'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    print(user)

    user_with_id = UserDB(id=len(database), **user.model_dump())

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_user_all():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id < 0 or user_id + 1 > len(database):
        raise HTTPException(status_code=404, detail='User Not Found')
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    database[user_id] = user_with_id
    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=MessageSchema
)
def delete_user(user_id: int):
    if user_id < 0 or user_id + 1 > len(database):
        raise HTTPException(status_code=404, detail='User Not Found')
    del database[user_id]
    return {'message': 'User Deleted!'}


@app.get(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def read_user(user_id: int):
    if user_id < 0 or user_id + 1 > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User Not Found'
        )

    user_with_id = database[user_id]

    return user_with_id
