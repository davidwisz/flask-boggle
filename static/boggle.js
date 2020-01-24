$(function(){
    //CREATE FORM SUBMIT HANDLER
    async function formSubmitHandler(searchWord) {
        let response = await axios.post('/word-check', {"word": searchWord});
        console.log('here it is ' + response);
    }
    //CREATE FORM SUBMIT LISTENER
    $('#word-entry-form').on('submit',  function(e){
        e.preventDefault();
        let searchWord = $('#word_entry').val();
        formSubmitHandler(searchWord);
    })
})