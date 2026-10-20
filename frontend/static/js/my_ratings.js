
async function getRatingsData(){
    try{
        const response = await fetch('api/ratings');

        if(!response.ok){
            throw new Error("/api/ratings response error")
        }

        const jsonData = await response.json();

        return jsonData;
    }
    catch(error){
        console.log(error);
    }
}

function createRatings(jsonData){
    const ratingsWrapper = document.querySelector(".ratings-wrapper");
    const maxRating = 5;


    try{
        jsonData.forEach(element => {
            const ratingWrap = document.createElement('div');
            ratingWrap.classList.add('rating-wrap');
            ratingsWrapper.appendChild(ratingWrap);

            const movieTitle = document.createElement('p');
            movieTitle.innerText = element.title;
            movieTitle.classList.add('movie-title');
            ratingWrap.appendChild(movieTitle);

            const img = document.createElement('img');
            img.classList.add('image-rating');
            img.src = element.poster;
            ratingWrap.appendChild(img);

            const rateValue = element.value;
            const stars ='★'.repeat(rateValue) + '☆'.repeat(maxRating - rateValue);

            const starsElem = document.createElement('p');
            starsElem.classList.add('stars-elem');
            starsElem.innerText = stars;
            ratingWrap.appendChild(starsElem);

            const changeRateButton = document.createElement('button');
            changeRateButton.innerText = "Zmień ocenę";
            changeRateButton.classList.add('rate-button');
            ratingWrap.appendChild(changeRateButton);

            const deleteRateButton = document.createElement('button');
            deleteRateButton.innerText = "Usuń ocenę";
            deleteRateButton.classList.add('rate-button');
            ratingWrap.appendChild(deleteRateButton);
            
            
        });
    }
    catch(error){
        console.error(error);
    }
}


async function mainFunc(){
    try{
        const jsonRatings = await getRatingsData();
        createRatings(jsonRatings);

    }
    catch(error){
        console.error(error);
    }
    
}

mainFunc();