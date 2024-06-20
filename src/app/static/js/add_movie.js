const containerOptions = document.getElementsByClassName('container-movies-options');
const moviesOptions = document.getElementsByClassName('movies-options');
const addMovieButton = document.getElementById('add-movie');

let moviesArray = [];

fetch('/api')
    .then(response => response.json())
    .then(movies => {
        moviesArray = movies; 
        console.log(moviesArray);
        movies.forEach(movie => {
            const option = document.createElement('option');
            option.value = movie.id;
            option.text = movie.title;
            for (let i = 0; i < moviesOptions.length; i++) {
                moviesOptions[i].appendChild(option);
            }
        });
    });


function createSelectMovies(){
    const div = document.createElement('div');
    const select = document.createElement('select');
    const input = document.createElement('input');
    
    input.type = 'text';
    input.placeholder = 'Rating';
    input.className = 'movies-ratings';
    select.className = 'movies-options';

    for (let i = 0 ; i < moviesArray.length; i++){
        const option = document.createElement('option');
        option.value = moviesArray[i].id;
        option.text = moviesArray[i].title;
        select.appendChild(option);
    }

    div.appendChild(select);
    div.appendChild(input);
    containerOptions[0].appendChild(div);
}

addMovieButton.addEventListener('click', createSelectMovies);