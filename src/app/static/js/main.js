//const $moviesPopularList = $('#movies_popular .list-movies')
//
//$refreshButton.addEventListener('click', () => {
//    // Mostrar el icono de cargando
//    $loadingIcon.style.display = 'flex'
//    $refreshButton.style.display = 'none'
//    fetch('/api/movies')
//        .then(response => response.json())
//        .then(movies => {
//            // Limpiar las películas existentes
//            $moviesPopularList.innerHTML = ''
//
//            // Añadir las nuevas películas
//            movies.forEach(movie => {
//                const movieCard = document.importNode($movieTemplate, true)
//
//                // Añadimos el id
//                movieCard.querySelector('.card').id = movie.id
//
//                // Añadimos la imagen
//                const movieImage = movieCard.querySelector('img')
//                movieImage.src = movie.image
//                movieImage.alt = movie.title
//
//                // Añadimos el titulo
//                const movieTitle = movieCard.querySelector('.title')
//                movieTitle.textContent = movie.title
//
//                // Añadimos la fecha
//                const movieDate = movieCard.querySelector('.release-date')
//                movieDate.textContent = movie.release_date
//
//                // Add event OnClick
//                movieCard.querySelector('.card').addEventListener('click', addMovie)
//
//                $moviesPopularList.appendChild(movieCard)
//            })
//
//            // Ocultar el icono de cargando
//            $loadingIcon.style.display = 'none'
//            $refreshButton.style.display = 'block'
//        })
//        .catch(error => {
//            console.error('Error fetching movies:', error)
//            // Ocultar el icono de cargando en caso de error
//            $loadingIcon.style.display = 'none'
//        })
//})



fetch('http://127.0.0.1:5000/api')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => { console.error('Error:', error); });