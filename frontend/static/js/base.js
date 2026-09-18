
async function getJsonData(){
    try{
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


function createMoviesElements(jsonData){
    const moviesWrapper = document.querySelector(".movies-wrapper");

    try{
        jsonData.movies.forEach(element => {
            const movieWrap = document.createElement('div');
            movieWrap.classList.add('movie-wrap');
            moviesWrapper.appendChild(movieWrap);

            const titleElem = document.createElement('p');
            titleElem.innerText = element.Title;
            titleElem.classList.add('movie-title');
            movieWrap.appendChild(titleElem);

            const ratingElem = document.createElement('p');
            ratingElem.innerText = element.Ratings[0].Value;
            ratingElem.classList.add('movie-rating');
            movieWrap.appendChild(ratingElem);

            const imageWrap = document.createElement('div');
            imageWrap.classList.add("image-wrap");
            movieWrap.appendChild(imageWrap);

            const imageElem = document.createElement('img');
            imageElem.classList.add('movie-image')
            imageElem.src = element.Poster;
            imageWrap.appendChild(imageElem);

        });
    }
    catch(error){
        console.error(error);
    }
}


async function mainFunc(){
    try{
        const moviesJsonData = await getJsonData();

        createMoviesElements(moviesJsonData);


    }
    catch(error){
        console.error(error);
    }
}

mainFunc();