// JavaScript Document
window.addEventListener('load', function(){
	var bgm_audio = document.querySelector("#BGM");
	var cont = document.querySelector(".bgm_control");
	var cont_img = document.querySelector(".bgm_img");
	var bgm_src = bgm_audio.getAttribute('src');
	var bgm_name = bgm_src.slice(bgm_src.lastIndexOf('/')+1, bgm_src.indexOf('.'));
	var bgm_info = document.querySelector(".info");
	// 点击事件绑定
	cont.addEventListener('click', function(){
		if(bgm_audio.paused){
			bgm_audio.play();
			cont_img.src = "img/music_play.png";
			bgm_info.innerHTML = "正在播放: "+bgm_name+"♪";
		}
		else{
			bgm_audio.pause();
			cont_img.src = "img/music_pause.png";
			bgm_info.innerHTML = "暂停中▶";
		}
	});
})