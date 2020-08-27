$(function(){
    
        $('.btn_white').on('click',function changeCss(){
            document.getElementById("cs").href = "../static/css/white_css/base.css"; 
            document.getElementById("top_css").href = "../static/css/white_css/top_white.css";
            document.getElementById("content_css").href = "../static/css/white_css/content1.css";   
        });
        $('.btn_white').on('click',function(){
            document.getElementById('img').src= "../static/image/top/kikyu.jpg";
         });
         

});