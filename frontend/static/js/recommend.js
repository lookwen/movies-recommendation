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
        const response = await fetch('/api/movies_id');

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



async function mainFunc(){
    try{
        const jsonData = await getJsonData();
        const topMoviesIdList = await getTopIdMoviesList();
        //console.log(jsonData);

        const bestMoviesWrapper = document.querySelector(".best-movies");
        
        const movies = getJsonElemByIdList(jsonData, topMoviesIdList);
        
        createMoviesElements(movies, bestMoviesWrapper);
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