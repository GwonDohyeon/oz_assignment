import pymysql
import pymysql.cursors

connection=pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    #문제1:새로운 제품 추가
    sql="INSERT INTO Products(productName,price,stockQuantity) VALUES (%s, %s, %s)"
    cursor.execute(sql,('Python Book',10000,10))
    connection.commit()
    
    """여러 데이터를 삽입할 경우 
    product_data=[("product1",199,19),("priduct2",121,10)]
    for product in product_data:
	cursor.execute(sql, product)
    """
    #문제2:제품 목록 조회
    cursor.execute("SELECT * FROM Products")
    for book in cursor.fetchall():
        print(book)
        
    #문제3:제품 재고 업데이트   
    sql="UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    cursor.execute(sql,(1,1))
    connection.commit()#update, insert, delete는 데이터를 변화시키는 쿼리이기 때문에 commit을 해주어야 db에 변경사항이 저장된다.
    
    #문제4:고객별 총 주문 금액
    sql="select customerID, sum(totalAmount) from Orders group by customerID"
    cursor.execute(sql)
    data=cursor.fetchall()#list 형식으로 데이터를 받아온다. ex)[{"칼럼명1":"value1", "칼럼명2":"value2"},{"칼럼명1":"value1", "칼럼명2":"value2"}]
    for row in data:#각 row는 dictionary 형식 ex) {"칼럼명1":"value1", "칼럼명2":"value2"}
        print(row)
        
    #문제5:고객 이메일 업데이트
    sql="update Customers set email=%s WHERE customerID =%s"
    cursor.execute(sql,("update1@update.com",1))
    connection.commit()
    
    #문제6:주문 취소
    sql="delete from Orders where orderID=%s"
    cursor.execute(sql,(15))
    connection.commit()
    
    #문제7:특정 제품 검색
    sql="select * from Products where productName like %s"
    cursor.execute(sql,('%Book%'))
    data=cursor.fetchall()
    for row in data:
        print(row['productName'])
    
    #문제8:특정 고객 주문 데이터 조회
    sql="select * from Orders where customerID=%s"
    cursor.execute(sql,(1))
    data=cursor.fetchall()
    for row in data:
        print(row)
    #문제9:가장 많이 주문한 고객
    sql="select customerID,count(*) as orderCount from Orders group by customerID order by orderCount DESC limit 1"
    cursor.execute(sql)
    data=cursor.fetchone()
    print(data)
    
cursor.close()#db connection 종료