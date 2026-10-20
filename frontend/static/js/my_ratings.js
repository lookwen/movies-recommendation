
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

    try{
        jsonData.forEach(element => {
            console.log(element.title);
            
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