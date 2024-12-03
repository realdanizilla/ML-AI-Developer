import requests

api_url = 'http://127.0.0.1:8000/api/tasks'

# obter tarefas
# response = requests.get(api_url)
# if response.status_code == 200:
#     print("tarefas atuais:")
#     print(response.json())
# else:
#     print(f"erro ao obter tarefas: {response.status_code}")


# criar nova tarefa
# new_task = {
#     'title': 'escrever código de exemplo',
#     'description': 'criar uma api restful usando fast api'
# }
# response = requests.post(api_url, json=new_task)
# if response.status_code == 201:
#     print("nova tarefa criada")
#     print(response.json())
# else:
#     print(f"Erro ao criar tarefa: {response.status_code}")


# atualizar tarefa existente
# task_id = 1
# update_data = {
#     'title': 'Comprar mantimentos e bebidas',
#     'done': True
# }
# response = requests.put(f'{api_url}/{task_id}', json=update_data)
# if response.status_code == 200:
#     print(f"Tarefa {task_id} atualizada com sucesso")
#     print(response.json())
# else:
#     print(f"erro ao atualizar tarefa {task_id}: {response.status_code}")


# deletar tarefa
task_id_to_delete = 2
response = requests.delete(f"{api_url}/{task_id_to_delete}")
if response.status_code == 200:
    print(f"tarefa {task_id_to_delete} deletada com sucesso")
    print(response.json())
else:
    print(f"Erro ao deletar tarefa {task_id_to_delete}: {response.status_code}")

# obter tarefas novamente
response = requests.get(api_url)
if response.status_code == 200:
    print("tarefas atuais:")
    print(response.json())
else:
    print(f"erro ao obter tarefas: {response.status_code}")