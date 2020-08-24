$(function(){
    $('.linkbtn').each(function(){
        $(this).on('click',function(){
            $("+.btn_item",this).slideToggle();
            return false;
        });
    });
});