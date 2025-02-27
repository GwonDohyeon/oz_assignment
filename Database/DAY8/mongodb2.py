from pymongo import MongoClient
from datetime import datetime

def insert_data(db):
    # 책 데이터 삽입
    books = [
        {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002, "genre": "fiction"},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987, "genre": "fiction"},
        {"title": "1Q84", "author": "Haruki Murakami", "year": 2009, "genre": "fiction"}
    ]
    db.books.insert_many(books)

    # 영화 데이터 삽입
    movies = [
        {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
        {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
        {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0}
    ]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = [
        {"user_id": 1, "action": "click", "timestamp": datetime(2023, 4, 12, 8, 0)},
        {"user_id": 1, "action": "view", "timestamp": datetime(2023, 4, 12, 9, 0)},
        {"user_id": 2, "action": "purchase", "timestamp": datetime(2023, 4, 12, 10, 0)},
    ]
    db.user_actions.insert_many(user_actions)

    print("Data inserted successfully")

#특정 장르의 책 찾기
def find_books_by_genre(db,genre):
    print(f"find {genre} books")
    books_collection=db['books']
    query={"genre":genre}
    projection={"_id":0,"title":1,"author":1}
    books=books_collection.find(query,projection)
    for book in books:
        print(book)
#감독별 평균 영화 평점 계산
def calculate_avg_rating(db):
    print("average rating group by director")
    movie_collection=db['movies']
    pipeline=[{"$group":{"_id":"$director","avg_rating":{"$avg":"$rating"}}},{"$project":{"director":"$_id","_id":0,"avg_rating":1}},{"$sort":{"avg_rating":-1}}]#내림차순($sort:{"avg_rating":-1})
    avg_ratings=movie_collection.aggregate(pipeline)
    for avg_rating in avg_ratings:
        print(avg_rating)
#특정 사용자의 최근 행동 조회
def find_recent_actions_by_user(db,user_id,limit=1):
    print(f"{user_id}'s recent actions")
    user_actions_collection=db["user_actions"]
    pipline=[{"$match":{"user_id":user_id}},
             {"$sort":{"timestamp":-1}},
             {"$limit":limit}]
    recent_actions=user_actions_collection.aggregate(pipline)
    for recent_action in recent_actions:
        print(recent_action)
#출판 연도별 책의 수 계산
def count_books_by_year(db):
    print("count books by year")
    books_collection=db['books']
    pipeline=[{"$group":{"_id":"$year","count":{"$sum":1}}},{"$project":{"_id": 0,"year":"$_id","count": 1}},{"$sort":{"year":-1}}]
    count_books=books_collection.aggregate(pipeline)
    for count_book in count_books:
        print(count_book)
#특정 사용자의 행동 유형 업데이트
def update_user_actions(db,user_id,date,old_action,new_action):
    user_actions_collection=db["user_actions"]
    query={"user_id":user_id,"action":old_action,"timestamp":{"$lt":date}}
    update={"$set":{"action":new_action}}
    result=user_actions_collection.update_many(query,update)
    print(f"Updated {result.modified_count}document(s).")
    for i,doc in enumerate(user_actions_collection.find()):
        print(i+1,doc,sep=".\n")
def drop_all_collections(db):
    # 데이터베이스 내 모든 컬렉션 삭제
    collections = db.list_collection_names()  # 데이터베이스의 모든 컬렉션 이름을 가져옵니다.
    for collection in collections:
        db.drop_collection(collection)  # 각 컬렉션을 삭제합니다.
    print("All collections dropped successfully.")
if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local  # 'local' 데이터베이스 사용
    insert_data(db)
    find_books_by_genre(db,"fiction")
    calculate_avg_rating(db)
    find_recent_actions_by_user(db,1,2)
    count_books_by_year(db)
    update_user_actions(db, 1, datetime(2023, 4, 13), "view", "seen")
    drop_all_collections(db)
    client.close()