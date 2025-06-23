from flask import request,Flask,jsonify

app = Flask(__name__)

items =[
    {"id":1,"name":"Item 1","description":"This item belongs to Baveet"},
    {"id":2,"name":"Item 2","description":"This is the second item that doesnt belongs to Baveet"}
]
@app.route('/')
def sample():
    return "Welcome to the home page of the sample TODO app"
##display itels
@app.route('/items')
def getitems():
    return jsonify(items)

@app.route('/retrieve/<int:id>')
def retrieve(id):
    for ids in items:
        if id == ids["id"]:
            return jsonify(ids)
    return jsonify({"error":"requested item is not in the database"})
## Post request, used Postman to post with json request!
@app.route('/additems',methods=['GET','POST'])
def add():
    if not request.json or not 'id' in request.json:
        return jsonify({"error":"requested item is not in the database"})
    
    new_item = {
        "id" : items[-1]["id"] + 1 if items else 1,
        "name" : request.json["name"],
        "description" : request.json["description"]
    }
    items.append(new_item)
    return jsonify({"success":"Item added to the database!"})
## in put, we update an existing item
## using postman send a put request to the url and it works!
@app.route('/update/<int:id>',methods=['PUT'])
def update(id):
    ### retrieve item
    old_item = {}
    for ids in items:
        if id == ids["id"]:
            old_item = ids
            break
    if not old_item:
        return jsonify({"error":"requested item is not in the database"})
    
    old_item['name'] = request.json.get('name', old_item['name'])
    old_item['description'] = request.json.get('name',old_item['name'])
    return jsonify(old_item)

    
             
@app.route('/delete/<int:id>',methods=['DELETE'])
def delete(id):
    items = [item for item in items if item["id"]!=id]
    return jsonify({"result":"Item Deleted!"})


if __name__=='__main__':
    app.run(debug=True)
