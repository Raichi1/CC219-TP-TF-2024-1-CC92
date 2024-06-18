
fetch('http://127.0.0.1:5000/api')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => { console.error('Error:', error); });