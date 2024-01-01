function goToAddOrderPage() {
    fetch("http://127.0.0.1:8000/add_order/")
    .then((response) => response.json())
    .then((json) => console.log(json));
}
