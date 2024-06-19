
document.addEventListener('DOMContentLoaded', function () {
    const moviesPopularList = document.getElementsByClassName('list-movies')

    document.getElementById('refresh-button').addEventListener('click', function () {
        fetch('/test')
            .then(response => response.json())
            .then(movies => {
                console.log(movies);
                moviesPopularList.innerHTML = '';
                if (movies.length === 0) {
                    moviesPopularList.innerHTML = 'No hay películas populares';
                }
                movies.forEach(movie => {
                    const template = document.getElementById('movie-template').content.cloneNode(true);
                    const moviesContainer = document.querySelector('.list-movies');

                    // Rellenar los datos en el template
                    template.querySelector('.title').textContent = movie.title;
                    template.querySelector('.release-date').textContent = movie.release_date;
                    template.querySelector('img').src = movie.image;
                    template.querySelector('img').alt = movie.title;

                    // Crear un div contenedor para la película y agregar el template rellenado
                    const movieElement = document.createElement('div');
                    movieElement.classList.add('card');
                    movieElement.id = movie.id;
                    movieElement.appendChild(template);

                    // Agregar el nuevo elemento de película al contenedor de películas
                    moviesContainer.appendChild(movieElement);
                });
            })
            .catch(error => {
                console.error('Error fetching movies:', error);
            });
    });
});