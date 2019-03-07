# coding=utf-8
from flask import Flask, jsonify, render_template
from py2neo import Graph,Node,Relationship

app = Flask(__name__)
graph = Graph("http://localhost:7474/db/data/",username='neo4j',password='123456')
graph.delete_all()

make_node_1 = Node("Person",name = "tom")
make_node_2 = Node("Person",name = "jerry")
graph.create(make_node_1)
graph.create(make_node_2)
node_1_make_node_2 = Relationship(make_node_1,'play',make_node_2)
node_1_make_node_2['count'] = 1
node_2_make_node_1 = Relationship(make_node_2,'play',make_node_1)
node_2_make_node_1['count'] = 2
graph.create(node_1_make_node_2)
graph.create(node_2_make_node_1)

node_1_make_node_2['count']+=1
find_code_1=graph.find_one(
    label="Person",
    property_key="name",
    property_value="tom"
)
find_code_2=graph.find_one(
    label="Person",
    property_key="name",
    property_value="jerry"
)




@app.route('/')
def index():
    return render_template('index.html')
 

if __name__ == '__main__':
    app.run(debug = True)