from fastapi import FastAPI
import json

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'world!'}

@app.get('/items/{item_id}')
def read_item(item_id: int):
    return (item_id * 2)

@app.post('/items/')
def update_item(item: dict):

    if len(item) < 3:
        FIELD_THE_USER_FORGOT_HERE = "salary" if ('salary' not in item.keys()) else "bonus" if ('bonus' not in item.keys()) else "taxes"
        return f"3 fields expected (salary, bonus, taxes). You forgot: {FIELD_THE_USER_FORGOT_HERE}."
    elif (str(item['salary']).isdigit() & 
          str(item['bonus']).isdigit() &
          str(item['taxes']).isdigit()) == False:
        return 'expected numbers, got strings.'
  
    return (item['salary'] + item['bonus'] - item['taxes']) # salary + bonus - taxes