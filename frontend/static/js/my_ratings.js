
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

function createDeleteForm(ratingWrap, element){
    const formDeleteRateButton = document.createElement('form');
    formDeleteRateButton.value = element.id;
    formDeleteRateButton.action = `/raitings`;
    formDeleteRateButton.method = 'POST';
    ratingWrap.appendChild(formDeleteRateButton);

    const ratingDeleteIdInput = document.createElement('input');
    ratingDeleteIdInput.type = 'hidden';
    ratingDeleteIdInput.name = 'rating_id';
    ratingDeleteIdInput.value = element.id; 
    formDeleteRateButton.appendChild(ratingDeleteIdInput);

    const deleteActionInput = document.createElement('input');
    deleteActionInput.type = 'hidden';
    deleteActionInput.name = 'action';
    deleteActionInput.value = 'delete';
    formDeleteRateButton.appendChild(deleteActionInput);
    
    const deleteRateButton = document.createElement('button');
    deleteRateButton.innerText = "Usuń ocenę";
    deleteRateButton.classList.add('rate-delete-button');
    deleteRateButton.dataset.rateId = element.id;
    deleteRateButton.type = 'submit';
    formDeleteRateButton.appendChild(deleteRateButton);
}


function createChangeForm(ratingWrap, element){
    const formChangeRateButton = document.createElement('form');
    formChangeRateButton.method = 'POST';
    ratingWrap.appendChild(formChangeRateButton);
    
    const ratingChangeIdInput = document.createElement('input');
    ratingChangeIdInput.type = 'hidden';
    ratingChangeIdInput.name = 'rating_id';
    ratingChangeIdInput.value = element.id;
    formChangeRateButton.appendChild(ratingChangeIdInput);


    const editActionInput = document.createElement('input');
    editActionInput.type = 'hidden';
    editActionInput.name = 'action';
    editActionInput.value = 'edit';
    formChangeRateButton.appendChild(editActionInput);
    
    
    const changeRateButton = document.createElement('button');
    changeRateButton.innerText = "Zmień ocenę";
    changeRateButton.classList.add('rate-change-button');
    changeRateButton.dataset.rateId = element.id;
    changeRateButton.type = 'submit';
    formChangeRateButton.appendChild(changeRateButton);
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
            

            createChangeForm(ratingWrap, element);
            createDeleteForm(ratingWrap, element);

            
            
            
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

        const changeRatingButtons = document.querySelectorAll(".rate-change-button");
        const deleteRatingButtons = document.querySelectorAll(".rate-delete-button");

    }
    catch(error){
        console.error(error);
    }
    
}

mainFunc();