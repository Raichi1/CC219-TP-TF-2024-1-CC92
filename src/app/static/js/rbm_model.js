const dataForm = document.getElementById('container-options');
const containerMovies = document.getElementsByClassName('movies-options');
const containerRatings = document.getElementsByClassName('movies-ratings');


dataForm.addEventListener('submit', function(event){
    event.preventDefault();

    const formData = event.target;

    const divs = formData.getElementsByTagName('select');
    const ratings = formData.getElementsByTagName('input');

    const data = {};

    for (let i = 0; i < divs.length; i++){
        data[Number(divs[i].value)] = Number(ratings[i].value);
    }

    console.log(data);
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log('Success:', result);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});