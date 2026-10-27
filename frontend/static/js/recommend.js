import { getJsonData, createMoviesElements, createMoviesDetails } from './base.js'

function getJsonElemByIdList(jsonElem, id_list){
    try{
        const finalJsonElem = [];
        id_list.forEach(element => {
            finalJsonElem.push(jsonElem.find(u => u.id == element));
        });
        
        return finalJsonElem;
    }
    catch(error){
        console.error(error);
    }
}

async function getTopIdMoviesList(){
    try{
        const response = await fetch('/api/top_movies_id');

        if(!response.ok){
            throw new Error("/api/movies_d error");

        }

        const jsonData = await response.json();

        return jsonData;
    }
    catch(error){
        console.error(error);
    }


}

async function getForYouMoviesIdList(){
    try{
        const response = await fetch('/api/for_you');

        if(!response.ok){
            throw new Error("/api/for_you error");

        }

        const jsonData = await response.json();

        return jsonData;
    }
    catch(error){
        console.error(error);
    }
}



async function mainFunc(){
    try{
        const jsonData = await getJsonData();
        const topMoviesIdList = await getTopIdMoviesList();
        const recommendedMoviesIdList = await getForYouMoviesIdList();
        //console.log(jsonData);

        const bestMoviesWrapper = document.querySelector(".best-movies");
        const recommendedMoviesWrapper = document.querySelector(".for-you-movies");
        
        const topMovies = getJsonElemByIdList(jsonData, topMoviesIdList);
        const recommendedMovies = getJsonElemByIdList(jsonData, recommendedMoviesIdList);
        
        createMoviesElements(topMovies, bestMoviesWrapper);
        createMoviesElements(recommendedMovies, recommendedMoviesWrapper);
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