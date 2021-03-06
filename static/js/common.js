$(function(){


    function changeLightCss(){
        var css_id   = document.getElementById("top_css")
        var sp_css_id= document.getElementById("top_sp_css")
        var cs_id    = document.getElementById("cs")
        var sp_cs_id = document.getElementById("sp_cs")
        var img      = document.getElementById('img')
        var contents = document.getElementById("content_css")
        var sp_contents = document.getElementById("sp_content_css")
        var genre    = document.getElementById("genre")
        var sp_genre = document.getElementById("sp_genre")
        console.log(sp_css_id)

        if(css_id !== null){
            css_id.href = "../static/css/white_css/top_white.css";
        }
        if(sp_css_id !== null){
            sp_css_id.href = "../static/css/white_css/top_sp_white.css";
            console.log("dd")
        }
        if(cs_id !== null){
            cs_id.href = "../static/css/white_css/base.css"; 
        }
        if(sp_cs_id !== null){
            sp_cs_id.href= "../static/css/white_css/base_sp.css";    
        }
        if(img !== null){
            img.src= "../static/image/top/kikyu.jpg";
        }
        if(contents !== null){
            contents.href = "../static/css/white_css/content1.css";
        }
        if(sp_contents !== null){
            sp_contents.href = "../static/css/white_css/content1_sp.css";
        }
        if(genre !== null){
            genre.href = "/static/css/white_css/style.contents.css";
        }
        if(sp_genre !== null){
            sp_genre.href = "/static/css/white_css/style.sp.contents.css";
        }

    }

    function changeDarkCss(){
        console.log("aaaaaaaaaaaaaaaaaa")
        var css_id   = document.getElementById("top_css")
        var sp_css_id= document.getElementById("top_sp_css")
        var cs_id    = document.getElementById("cs")
        var sp_cs_id = document.getElementById("sp_cs")
        var img      = document.getElementById('img')
        var contents = document.getElementById("content_css")
        var sp_contents = document.getElementById("sp_content_css")
        var genre    = document.getElementById("genre")
        var sp_genre = document.getElementById("sp_genre")
        
        if(css_id !== null){
            css_id.href = "../static/css/black_css/top_black.css";
        }
        if(sp_css_id !== null){
            sp_css_id.href = "../static/css/black_css/top_sp_black.css";
            console.log("dd")
        }
        if(cs_id !== null){
            cs_id.href = "../static/css/black_css/base.css"; 
        }
        if(sp_cs_id !== null){
            sp_cs_id.href= "../static/css/black_css/base_sp.css";    
        }
        if(img !== null){
            img.src= "../static/image/top/earth.jpg";
        }
        if(contents !== null){
            contents.href = "../static/css/black_css/content1.css";
        }
        if(sp_contents !== null){
            sp_contents.href = "../static/css/black_css/content1_sp.css";
        }
        if(genre !== null){
            genre.href = "/static/css/black_css/style.contents.css";
        }
        if(sp_genre !== null){
            sp_genre.href = "/static/css/black_css/style.sp.contents.css";
        }

    }

    var css_mode = sessionStorage.getItem("css_mode")
    console.log(css_mode)

    if(css_mode === "light"){
        changeLightCss();
    }
    
    if(css_mode === "dark"){
        changeDarkCss();
    }

        $('.btn_white').on('click',function changeCss(){
            sessionStorage.setItem("css_mode", "light");
            console.log(sessionStorage.getItem("css_mode"))
            changeLightCss(); 
        });

        $('.btn_black').on('click',function changeCss(){
            sessionStorage.setItem("css_mode", "dark");
            console.log(sessionStorage.getItem("css_mode"))
            changeDarkCss();
        });


});