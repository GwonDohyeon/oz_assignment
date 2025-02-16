use yes24;
CREATE TABLE Books (
    bookID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    publisher VARCHAR(255),
    publishing DATE,
    rating DECIMAL(3, 1),
    review INT,
    sales INT,
    price DECIMAL(10, 2),
    ranking INT,
    ranking_weeks INT
);
# 전체 조회
select * from books;
# 모든 책의 제목과 저자를 조회
select title, author from books;
# 평점이 8 이상인 책 조회
select * from books where rating>=8;
# 리뷰 수가 100개 이상인 책들의 제목과 리뷰 수 조회
select title,review from books where review>=100 order by review desc;
# 가격이 20000미만인 택의 가격과 제목 조회
select title,price from books where price<20000;
# 4주 이상 순위권에 머문 책들 조회
select * from books where ranking_weeks>=4 order by ranking_weeks desc;
# 특정 저자의 책 조회
select * from books where author='한강 저';
# 특정 출판사의 책 조회
select * from books where publisher = '창비';

# 저자별로 출판한 책의 수 조회
select author, count(*) as books_count from books group by author order by books_count desc;
# 가장 많은 책을 출판한 출판사
select publisher, count(*) as books_count from books group by publisher order by books_count desc limit 1;
# 평점 평균 순서로 저자 조회
select author, avg(rating) from books group by author order by avg(rating) desc;
# 랭킹이 1위인 도서의 제목과 저자 조회
select title,author from books where ranking=1;
# 판매 수와 리뷰수가 높은 상위 10개의 책 조회
select * from books order by sales desc, review desc limit 10; 
# 가장 최근에 출판된 책 5권 조회
select * from books order by publishing desc limit 5;

# 순위권에 드는 작품이 2개 이상이고 리뷰수가 100 이상인 작가의 평점 평균 조회
select author, avg(rating) as avg_rating from books b where b.author in(select author from books where review>=100 group by author having count(*)>=2) group by author order by avg_rating desc;
# 출판사별 출판된 책의 수 조회
select publishing, count(*) from books group by publishing order by count(*) desc;
# 리뷰수가 가장 많은 책 5개 조회
select * from books order by review desc limit 5;

# 평균 평점보다 높은 평점을 가진 책 조회
select * from books b where b.rating>(select avg(rating) from books);
# 평균 가격보다 비싼 책들의 제목과 가격을 조회
select title,price from books b where b.price > (select avg(price) from books);
# 평균 판매 수 보다 적게 팔린 책 조회
select * from books b where b.sales<(select avg(sales) from books);
# 가장 많은 책이 순위권에 있는 저자의 가장 최신작 조회
select author,title,publishing from books where author = (select author from books group by author order by count(*) desc limit 1) order by publishing desc limit 1;

# 특정 책 가격 업데이트
update books set price = 99999 where title like '%한국사%';
# 특정 저자의 책 제목 변경
update books set title = '제목' where author = '한강 저';
# 판매 수가 가장 낮은 책 삭제
delete from books where sales=(select min(sales) from books);
# 특정 출판사에서 출판된 모든 책의 평점 증가
update books set rating=rating+1 where publisher = '창비';

# 저자별 평균 평점 및 판매 수 조회
select author,avg(rating),sum(sales) from books group by author order by avg(sales) desc,avg(rating) desc;
# 출판일별 책 가격 조회
select publishing,price from books order by publishing asc;
# 출판사별 출판 책 수와 평균 리뷰 수 조회
select publisher, count(*) as books_count, avg(review) as review_avg from books group by publisher order by books_count desc;
# 순위별 평균 판매량 조회
select ranking, avg(sales) from books group by ranking;
# 가격별 리뷰 수 및 명점 평균 조회
select price,avg(review),avg(rating) from books group by price order by price;

# 출판사별 가장 많이 팔린 저자 조회
select publisher,author,sales_avg from (
select publisher,author,avg(sales) as sales_avg ,rank() over (
partition by publisher order by avg(sales) desc) as rnk from books group by publisher,author) sub
where rnk=1;
# 잘못된 쿼리로 출판사별 가장 많이 팔린 저자가 아니라 모든 저자를 조회
select publisher,author,avg(sales) as sales_avg from books group by publisher,author order by publisher, sales_avg desc;
# 리뷰 수가 평균보다 많고 가격은 평균보다 적은 책 조회
select * from books where review > (select avg(review) from books) and price<(select avg(price) from books);
# 가장 많은 책을 출간한 저자 조회
select author,count(distinct title) from books group by author order by count(distinct title) desc limit 1;
# 저자별로 가장 많이 팔린 책 조회1
select * from books b where b.sales=(select max(sales) from books b2 where b2.author=b.author);
# 저자별로 가장 많이 팔린 책 조회2
select * from (select * ,rank() over(partition by author order by sales desc) as rnk from books)sub where sub.rnk=1 order by bookID;
# 연도별 출간된 책의 수와 평균 가격
select year(publishing) as publishing_year,count(distinct title) as books_count,avg(price) as price_avg from books group by year(publishing) order by year(publishing);
# 출판사 중에 평점의 표준편차가 가장 큰 출판사 조회
select publisher,stddev(rating) from books group by publisher order by stddev(rating) desc limit 1;
# 특정 작가의 책들 중 판매량 대비 평점이 가장 높은 책 조회
select *,rating/sales as ratio from books where author='한강 저' order by ratio desc limit 1;


