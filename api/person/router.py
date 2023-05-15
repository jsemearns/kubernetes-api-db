from typing import Optional

from fastapi import Depends, HTTPException, Request, status
from fastapi.routing import APIRouter

from .models import Person

person_router = APIRouter(prefix='/person')

@person_router.get('/list', tags=['Person'])
async def list():
    persons = await Person.all().to_list()
    return persons

@person_router.get('/{person_id}', response_model=Optional[Person])
async def get(person_id: str) -> Person:
    person = await Person.get(person_id)
    return person

@person_router.post('/create', tags=['Person'])
async def post(person: Person) -> dict:
    response = {
        'success': True
    }
    try:
        await person.save()
    except Exception as e:
        response['success'] = False
        response['message'] = 'Failed to create person. Try again.'
    return response
