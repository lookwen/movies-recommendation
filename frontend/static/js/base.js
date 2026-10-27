
export async function getJsonData(){
    try {
        const response = await fetch('api/movies');
    
        if(!response.ok){
            throw new Error("/api/movies response error");
        }

        const jsonData = await response.json();

        return jsonData;

    }
    catch(error){
        console.log(error);
    }

}

export function createMoviesDetails(jsonElement, moviesWrapper){
    const movieDetails = document.createElement('div');
    movieDetails.classList.add('movies-details-wrapper');
    movieDetails.classList.add('non-visible');
    moviesWrapper.appendChild(movieDetails);

    const genresDetails = document.createElement('p');
    genresDetails.innerText = jsonElement.genre;
    movieDetails.appendChild(genresDetails);

    const yearDetails = document.createElement('p');
    yearDetails.innerText = jsonElement.release_date;
    movieDetails.appendChild(yearDetails);

    const runtimeDetails = document.createElement('p');
    runtimeDetails.innerText = jsonElement.runtime;
    movieDetails.appendChild(runtimeDetails);

    const plotDetails = document.createElement('p');
    plotDetails.innerText = jsonElement.plot;
    movieDetails.appendChild(plotDetails);

    const rateDetails = document.createElement('a');
    rateDetails.href = `/rate/${jsonElement.id}`;
    rateDetails.classList.add("rate-details");
    rateDetails.innerText = "Oceń Film";
    movieDetails.appendChild(rateDetails);

}


export function createMoviesElements(jsonData, moviesWrapper){
    
    try{
        jsonData.forEach(element => {
            const movieWrap = document.createElement('div');
            movieWrap.classList.add('movie-wrap');
            moviesWrapper.appendChild(movieWrap);

            
            const titleElem = document.createElement('p');
            titleElem.innerText = element.title;
            titleElem.classList.add('movie-title');
            movieWrap.appendChild(titleElem);

            const ratingElem = document.createElement('p');
            ratingElem.innerText = element.average_rating
            ratingElem.classList.add('movie-rating');
            movieWrap.appendChild(ratingElem);

            const imageWrap = document.createElement('div');
            imageWrap.classList.add("image-wrap");
            movieWrap.appendChild(imageWrap);

            const imageElem = document.createElement('img');
            imageElem.classList.add('movie-image')
            imageElem.src = element.poster;
            
            imageElem.addEventListener('error', () => {
                movieWrap.style.display = 'none';
            });
            
            imageWrap.appendChild(imageElem);
            
            createMoviesDetails(element, movieWrap);
        });
    }
    catch(error){
        console.error(error);
    }
}




async function mainFunc(){
    try{
        const moviesJsonData = await getJsonData();
        //console.log(moviesJsonData)
        
        const moviesWrapper = document.querySelector(".movies-wrapper");

        createMoviesElements(moviesJsonData, moviesWrapper);

        const moviesWraps = document.querySelectorAll('.movie-wrap');

        moviesWraps.forEach((element) => {
            element.addEventListener('click', (event) => {
                const currentElement = event.currentTarget;
                const detailsElement = currentElement.querySelector(
                    '.movies-details-wrapper'
                );

                if (detailsElement) {
                    detailsElement.classList.toggle('non-visible');
                }
            });
        });


    }
    catch(error){
        console.error(error);
    }
}

mainFunc();