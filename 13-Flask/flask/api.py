## PUT and DELETE methods in Flask
## Working with API's -- JSON

from flask import Flask, request, jsonify

app = Flask(__name__)

## Initial Data In TO-Do List
todo_list = [
    {'id': 1, 'task': 'Learn Flask', 'Description': 'Study Flask framework for web development'},
    {'id': 2, 'task': 'Build a REST API', 'Description': 'Create endpoints for CRUD operations'},
    {'id': 3, 'task': 'Deploy to Heroku', 'Description': 'Deploy the application to Heroku'}
]

@app.route('/')
def index():
    return "Welcome to the To-Do List API!"

## Get: Retrieve all tasks
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todo_list)

## Get: Retrieve a specific task by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todo_list if item['id'] == todo_id), None)
    if todo:
        return jsonify(todo)
    else:
        return jsonify({'error': 'Task not found'}), 404  
    
## Post: Create a new task
@app.route('/todos', methods=['POST'])
def create_todo():
    new_todo = request.get_json()
    new_todo['id'] = len(todo_list) + 1
    todo_list.append(new_todo)
    return jsonify(new_todo), 201

## Put: Update an existing task
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((item for item in todo_list if item['id'] == todo_id), None)
    if todo:
        updated_todo = request.get_json()
        todo.update(updated_todo)
        return jsonify(todo)
    else:
        return jsonify({'error': 'Task not found'}), 404
    
## Delete: Remove a task
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todo_list
    todo_list = [item for item in todo_list if item['id'] != todo_id]
    return jsonify({'message': 'Task deleted successfully'}), 204

## Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

## Example JSON Data for Testing
 
