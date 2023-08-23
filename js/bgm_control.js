// JavaScript Document
window.addEventListener('load', function(){
	var bgm_audio = document.querySelector("#BGM");
	var cont = document.querySelector(".bgm_control");
	var cont_img = document.querySelector(".bgm_img");
	// 点击事件绑定
	cont.addEventListener('click', function(){
		if(bgm_audio.paused){
			bgm_audio.play();
			cont_img.src = "img/music_play.png";
		}
		else{
			bgm_audio.pause();
			cont_img.src = "img/music_pause.png";
		}
	});
})