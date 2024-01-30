/*
    JavaScript code for handling default country selection in user profile form.
    The code does the following:
    1. Initially sets the color of the default country dropdown to a muted color if no country is selected.
    2. Listens for changes in the default country dropdown.
    3. Updates the color of the dropdown based on whether a country is selected or not.
*/

// Initial check and styling for default country
let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}

// Event listener for changes in default country dropdown
$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});
