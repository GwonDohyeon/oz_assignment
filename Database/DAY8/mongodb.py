from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')#MongoDB연결
db=client['example_db']#데이터베이스 선택
collection=db['example_collection']#컬렉션 선택
#삽입
example_doc={"name":"John","age":30,"city":"New York"}
collection.insert_one(example_doc)#문서 삽입
#조회
for doc in collection.find():#모든 문서 조회
    print(doc)
query={"name":"John"}#조건
for doc in collection.find(query):#조건에 맞는 문서 조회
    print(doc)
#업데이트
collection.update_one({"name":"John"},{"$set":{"age":31}})#조건에 맞는 문서 1개 업데이트
collection.update_many({"name":"John"},{"$set":{"age":32}})#조건에 맞는 모든 문서 업데이트
#삭제
collection.delete_one({"name":"John"})#조건에 맞는 문서 1개 삭제
collection.delete_many({"name":"John"})#조건에 맞는 모든 문서 삭제
#컬렉션 삭제
db.drop_collection("example_collection")
#데이터베이스 삭제
client.drop_database("example_db")