let host = 'http://127.0.0.1:8000';

function backToMainPage() {
    fetch(host)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(() => {
            window.location.href = host;
        })
        .catch(e => console.log('There was an error: ' + e.message));
}

function goToAddOrderPage() {
    fetch(host + '/add_order/')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(() => {
            window.location.href = host + '/add_order/';
        })
        .catch(e => console.log('There was an error: ' + e.message));
}


