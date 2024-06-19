document.addEventListener('DOMContentLoaded', function () {
    // Seleccionar el contenedor padre de la lista de películas en lugar de una colección de elementos
    const moviesContainer = document.querySelector('.list-movies');

    document.getElementById('refresh-button').addEventListener('click', function () {
        fetch('/api/movies')
            .then(response => response.json())
            .then(movies => {
                console.log(movies);
                // Limpiar el contenedor de películas antes de agregar nuevos elementos
                moviesContainer.innerHTML = '';
  
                if (movies.length === 0) {
                    moviesContainer.innerHTML = 'No hay películas populares';
                }
                movies.forEach(movie => {
                    const template = document.getElementById('movie-template').content.cloneNode(true);

                    // Rellenar los datos en el template
                    template.querySelector('.title').textContent = movie.title;
                    template.querySelector('.release-date').textContent = movie.release_date;
                    template.querySelector('img').src = movie.image;
                    template.querySelector('img').alt = movie.title;

                    // Crear un div contenedor para la película y agregar el template rellenado
                    const movieElement = document.createElement('div');
                    //movieElement.classList.add('card');
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