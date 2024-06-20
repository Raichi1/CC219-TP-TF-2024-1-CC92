// This file is used to handle the recommendation model using the RBM model
const dataForm = document.getElementById('container-options');
const containerMovies = document.getElementsByClassName('movies-options');
const containerRatings = document.getElementsByClassName('movies-ratings');

// Function to update the movies in the form
const containerCardTitle = document.getElementsByClassName('card-title');
const containerCardDate = document.getElementsByClassName('card-date');
const containerCardMovies = document.getElementsByClassName('card-movie');

// Function to update the movies in the form
const modelOption = document.getElementById('model-options');

const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZTg4YjMzYjRiMTNlMTNiZmJiYTg0MjgyYmE3ZWFjZCIsInN1YiI6IjY2MjZlZjQ4NjJmMzM1MDEzMWQ3ODkwOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.y0c6NjIay8Byza_Tl1BKAaAcjtVdFrBu9NQrxfWBN2g'
    }
  };

async function getImage(movie_id) {
    try {
        const response = await fetch('https://api.themoviedb.org/3/movie/' + movie_id + '/images', options);
        const data = await response.json();
        const backdrops = data['backdrops'];
        
        // Buscar el primer diccionario con iso_639_1 === 'en'
        const englishBackdrop = backdrops.find(backdrop => backdrop.iso_639_1 === 'en');

        if (englishBackdrop){
            console.log(englishBackdrop.file_path);
            return englishBackdrop.file_path;
        }
        return '';
    } catch (err) {
        console.error(err);
        return '';
    }
}


// Function to update the movies in the form
async function updateCardMovies(data){
    for (let i = 0; i < containerCardMovies.length; i++){
        const file_path = await getImage(data[i].movie_id);
        console.log(data[i].movie_id);
        containerCardTitle[i].innerHTML = data[i].title;
        containerCardDate[i].innerHTML = data[i].date;
        containerCardMovies[i].src = 'https://image.tmdb.org/t/p/w500' + file_path;
        console.log(containerCardMovies[i].src);
        containerCardMovies[i].alt = data[i].title;
    }
}

dataForm.addEventListener('submit', function(event){
    event.preventDefault();

    const formData = event.target;

    const divs = formData.getElementsByTagName('select');
    const ratings = formData.getElementsByTagName('input');

    const data = {};

    for (let i = 0; i < divs.length; i++){
        data[Number(divs[i].value)] = Number(ratings[i].value);
    }
    if (modelOption.value == "rbm"){
        fetch('/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            updateCardMovies(result);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    else if (modelOption.value == "embeddings"){
        fetch('/embeddings', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            updateCardMovies(result);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    else{
        
    }
});