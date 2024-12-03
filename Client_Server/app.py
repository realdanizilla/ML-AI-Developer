from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str = ""
    done: bool = False


tasks = [
    Task(id=1, title='Comprar mantimentos', description='Leite, Queijo, Pão', done=False),
    Task(id=2, title='Estudar Python', description='Ler sobre APIs Restful', done=False)
]

@app.get('/api/tasks', response_model=List[Task])
def get_tasks():
    return tasks

@app.get('/api/tasks/{task_id}', response_model=Task)
def get_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada')
    return task

@app.post('/api/tasks', response_model=Task, status_code=201)
async def create_task(request: Request):
    json_body = await request.json()
    if 'title' not in json_body:
        raise HTTPException(status_code=400, detail='Dados inválidos')
    task = Task(
        id = tasks[-1].id + 1 if tasks else 1,
        title = json_body['title'],
        description = json_body.get('description',''),
        done=False
    )
    tasks.append(task)
    return task

@app.put('/api/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, request: Request):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada')
    json_body = await request.json()
    task.title = json_body.get('title', task.title)
    task.description = json_body.get('description', task.description)
    task.done = json_body.get('done', task.done)
    return task

@app.delete('/api/tasks/{task_id}', response_model=dict)
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {'result': 'tarefa deletada com sucesso'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)