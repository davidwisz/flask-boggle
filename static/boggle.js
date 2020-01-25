$(function(){
    //CREATE FORM SUBMIT HANDLER
    async function formSubmitHandler(searchWord) {
        let response = await axios.post('/word-check', {"word": searchWord});
        return response.data
    }
    
    //CREATE FORM SUBMIT LISTENER
    $('#word-entry-form').on('submit', async function(e){
        e.preventDefault();
        let searchWord = $('#word_entry').val();
        let responseData = await formSubmitHandler(searchWord);
        displayMessage(responseData);
    })

    // DISPLAY USER MESSAGE
    function displayMessage(responseData) {
        $message = $('#message');
        $message.removeClass('success failure');
        $score = $('.score');

        if (responseData.result === 'ok') {
            $message.addClass('success');
            $message.text(`Added: ${responseData.word}`);
            $score.text(responseData.score)
        } else if (responseData.result === 'not-a-word') {
            $message.addClass('failure');
            $message.text(`${responseData.word} is not a valid English word`);
        } else {
            $message.addClass('failure');
            $message.text(`${responseData.word} is not a valid word on the board`)
        }
    }

})