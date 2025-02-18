// 크롤링한 데이터를 아래와 같은 형태의 객체 배열로 가정합니다.
// 추후 데이터베이스에 있는 데이터를 쿼리문으로 불러 올 수 있게 쿼리를 작성해 볼 수 있음

// 제품 데이터
const product_data = [
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' ,sex: '남성'},
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000',sex: '남성' },
    { category: "신발", brand: 'Nike', product: '에어포스 1', price: '137,000',sex: '남성' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' ,sex: '남성'},
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티2', price: '390,000' ,sex: '남성'},
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠2', price: '188,000' ,sex: '남성'},
    { category: "신발", brand: 'Nike', product: '에어포스 2', price: '137,000' ,sex: '여성'},
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링2', price: '29,000',sex: '남성' },
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티3', price: '390,000' ,sex: '남성'},
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠3', price: '188,000' ,sex: '여성'},
    { category: "신발", brand: 'Nike', product: '에어포스 3', price: '137,000' ,sex: '남성'},
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링3', price: '29,000' ,sex: '남성'},
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티4', price: '390,000',sex: '남성' },
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠4', price: '188,000',sex: '여성' },
    { category: "신발", brand: 'Nike', product: '에어포스 4', price: '137,000' ,sex: '남성'},
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링4', price: '29,000',sex: '남성' },
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티5', price: '390,000' ,sex: '남성'},
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠5', price: '188,000' ,sex: '여성'},
    { category: "신발", brand: 'Nike', product: '에어포스 5', price: '137,000',sex: '여성' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링5', price: '29,000' ,sex: '남성'},
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티6', price: '390,000' ,sex: '남성'},
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠6', price: '188,000' ,sex: '남성'},
    { category: "신발", brand: 'Nike', product: '에어포스 6', price: '137,000',sex: '남성' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링6', price: '29,000' ,sex: '여성'},
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티7', price: '390,000',sex: '여성' },
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠7', price: '188,000' ,sex: '남성'},
    { category: "신발", brand: 'Nike', product: '에어포스 7', price: '137,000',sex: '남성' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링7', price: '29,000',sex: '여성' },
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티8', price: '390,000' ,sex: '남성'},
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠8', price: '188,000',sex: '남성' },
    { category: "신발", brand: 'Nike', product: '에어포스 8', price: '137,000' ,sex: '남성'},
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링8', price: '29,000' ,sex: '남성'},
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티9', price: '390,000' ,sex: '남성'},
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠9', price: '188,000',sex: '남성' },
    { category: "신발", brand: 'Nike', product: '에어포스 9', price: '137,000' ,sex: '남성'},
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링9', price: '29,000' ,sex: '남성'},
    // ...
];

const itemsPerPage = 4; // 한 페이지당 표시할 제품 개수
let currentPage = getCurrentPageFromURL();
let searchQuery = "";
let selectedCategory = "카테고리";
let selectedSex = "전체";

// URL에서 페이지 번호 가져오기 (query parameter 방식)
function getCurrentPageFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const page = parseInt(urlParams.get("page"));
    return isNaN(page) ? 1 : page;
}

// URL에서 검색어 가져오기
function getSearchQueryFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get("search") || "";
}

// URL에서 카테고리 가져오기
function getCategoryFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get("category") || "카테고리";
}

// URL에서 성별 가져오기
function getSexFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get("sex") || "전체";
}

// URL 변경 (query parameter 사용)
function updateURL() {
    const newURL = `?page=${currentPage}&search=${searchQuery}&category=${selectedCategory}&sex=${selectedSex}`;
    console.log("Updating URL to:", newURL);  // 로그 추가로 URL이 업데이트되는지 확인
    window.history.pushState({}, '', newURL);
}

// 페이지 로드 시 URL에 따른 필터 및 페이지 정보 가져오기
function loadFiltersFromURL() {
    selectedCategory = getCategoryFromURL();  // URL에서 카테고리 가져오기
    searchQuery = getSearchQueryFromURL();  // URL에서 검색어 가져오기
    currentPage = getCurrentPageFromURL();  // URL에서 페이지 번호 가져오기
    selectedSex = getSexFromURL(); // URL에서 성별 가져오기
}

// 검색 및 카테고리에 맞는 제품 필터링
function getFilteredProducts() {
    return product_data.filter((item) => {
        const matchesCategory = selectedCategory === "카테고리" || item.category === selectedCategory;
        const matchesSearch = item.product.includes(searchQuery);
        const matchesSex = item.sex === selectedSex || selectedSex === "전체";
        return matchesCategory && matchesSearch && matchesSex;
    });
}

// 제품 목록 출력
function displayProducts() {
    const filteredProducts = getFilteredProducts();
    const totalPages = Math.ceil(filteredProducts.length / itemsPerPage);

    // 현재 페이지가 범위를 벗어나면 조정
    if (currentPage > totalPages) currentPage = totalPages;
    if (currentPage < 1) currentPage = 1;

    const start = (currentPage - 1) * itemsPerPage;
    const end = currentPage * itemsPerPage;
    const paginatedProducts = filteredProducts.slice(start, end);

    const productTable = document.getElementById('product_data_Table');
    productTable.innerHTML = ""; // 기존 데이터 초기화

    paginatedProducts.forEach((item) => {
        const row = productTable.insertRow();
        row.insertCell(0).innerHTML = item.category;
        row.insertCell(1).innerHTML = item.brand;
        row.insertCell(2).innerHTML = item.product;
        row.insertCell(3).innerHTML = item.price;
        row.insertCell(4).innerHTML = item.sex;
    });
    renderPagination(totalPages);
}

// 페이지네이션 렌더링
function renderPagination(totalPages) {
    const paginationContainer = document.querySelector(".pagination");
    paginationContainer.innerHTML = "";

    if (totalPages <= 1) return;

    let startPage = Math.max(1, currentPage - 1);
    let endPage = Math.min(totalPages, startPage + 2);
    if (endPage - startPage < 2) startPage = Math.max(1, endPage - 2);

    // 이전 버튼
    paginationContainer.innerHTML += `<li class="page-item ${currentPage === 1 ? "disabled" : ""}">
        <a class="page-link" href="" onclick="changePage(${currentPage - 1},event)">Previous</a>
    </li>`;

    if (startPage > 1) paginationContainer.innerHTML += `<li class="page-item">
        <a class="page-link" href="" onclick="changePage(${startPage - 1},event)">...</a>
    </li>`;

    for (let i = startPage; i <= endPage; i++) {
        paginationContainer.innerHTML += `<li class="page-item ${i === currentPage ? "active" : ""}">
            <a class="page-link" href="" onclick="changePage(${i},event)">${i}</a>
        </li>`;
    }

    if (endPage < totalPages) paginationContainer.innerHTML += `<li class="page-item">
        <a class="page-link" href="" onclick="changePage(${endPage + 1},event)">...</a>
    </li>`;

    paginationContainer.innerHTML += `<li class="page-item ${currentPage === totalPages ? "disabled" : ""}">
        <a class="page-link" href="" onclick="changePage(${currentPage + 1},event)">Next</a>
    </li>`;
}

// 페이지 변경 함수
function changePage(page,event) {
    event.preventDefault(); // 클릭 시 페이지 새로고침 방지
    const totalPages = Math.ceil(getFilteredProducts().length / itemsPerPage);
    if (page < 1 || page > totalPages) return;
    currentPage = page;
    updateURL();
    displayProducts();
}

// 검색 및 필터 적용 버튼 이벤트
document.querySelector(".btn-primary").addEventListener("click", function () {
    selectedCategory = document.getElementById("inlineFormSelectPref").value;
    searchQuery = document.querySelector("input.form-control").value;
    selectedSex = document.getElementById("inlineFormSelectSex").value;
    currentPage = 1; // 필터를 변경하면 1페이지로 초기화
    updateURL();
    displayProducts();
});

// 뒤로가기/앞으로 가기 이벤트 발생 시
window.addEventListener('popstate', function () {
    currentPage = getCurrentPageFromURL();
    searchQuery = getSearchQueryFromURL();
    selectedCategory = getCategoryFromURL();
    selectedSex = getSexFromURL();
    displayProducts();
});

// 페이지 로드 시 필터 및 페이지 초기화
window.addEventListener('load', function () {
    loadFiltersFromURL();  // URL에서 필터 값 및 페이지 번호 로드
    displayProducts();      // 필터 및 페이지에 맞는 제품 표시
});

// 현재 시간을 표시하는 함수
function updateCurrentTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    const day = now.getDate().toString().padStart(2, '0');
    const month = (now.getMonth() + 1).toString().padStart(2, '0');  // 1부터 시작하는 월
    const year = now.getFullYear();

    const timeString = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;  // 날짜와 시간을 결합
    document.getElementById('current-time').textContent = timeString;  // 시간 및 날짜 업데이트
}

// 페이지 로드 시 현재 시간 갱신
setInterval(updateCurrentTime, 1000);  // 1초마다 시간을 갱신

// 다크 모드 토글 함수
function toggleDarkMode() {
    const body = document.body;
    const table = document.querySelectorAll('.table');
    const btn = document.querySelectorAll('.btn');
    const pagination = document.querySelector('.pagination');
    body.classList.toggle('dark-mode');
    table.forEach(table => table.classList.toggle('dark-mode'));
    btn.forEach(button => button.classList.toggle('dark-mode'));
    pagination.classList.toggle('dark-mode');
    // 버튼 텍스트 변경
    if (body.classList.contains('dark-mode')) {
        darkModeBtn.innerHTML = '라이트 모드';
    } else {
        darkModeBtn.innerHTML = '다크 모드';
    }
}

// 다크 모드 버튼 클릭 이벤트
document.getElementById('darkModeBtn').addEventListener('click', toggleDarkMode);

// 폼 요소를 선택
const form = document.querySelector('form');
function getUserInfo(
  name,
  ssn_front,
  ssn_back,
  username,
  password,
  emailId,
  mailbox,
  address,
  gender,
  agree
) {
  const userInfo = {
    name: name,
    ssn: ssn_front + '-' + ssn_back,
    username: username,
    password: password,
    email: emailId + '@' + mailbox,
    address: address,
    gender: gender,
    agree: agree,
  };
  return userInfo;
}
// 폼 제출 이벤트 리스너 추가
form.addEventListener('submit', function (event) {
  event.preventDefault();
  const name = document.querySelector('#name').value;
  const ssn_front = document.querySelector('#ssn_front').value;
  const ssn_back = document.querySelector('#ssn_back').value;
  const username = document.querySelector('#username').value;
  const password = document.querySelector('#password').value;
  const passwordRetype = document.querySelector('#password-retype').value;
  const emailId = document.querySelector('#email').value;
  const mailbox = document.querySelector('#mailbox').value;
  const address = document.querySelector('#address').value;
  const gender = document.querySelector('input[name="gender"]:checked').value;
  const agree = document.querySelector('#agree').checked;
  if (username.length < 4 || username.length > 8) {
    alert('아이디는 4자 이상, 8자 이하로 입력하세요.');
  } else if (password !== passwordRetype) {
    alert('비밀번호가 일치하지 않습니다.');
  } else {
    const result = getUserInfo(
      name,
      ssn_front,
      ssn_back,
      username,
      password,
      emailId,
      mailbox,
      address,
      gender,
      agree
    );
    console.log(result);
  }
});
