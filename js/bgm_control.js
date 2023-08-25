// JavaScript Document
window.addEventListener('load', function(){
	var bgm_audio = document.querySelector("#BGM");
	var cont = document.querySelector(".bgm_control");
	var cont_img = document.querySelector(".bgm_img");
	var bgm_info = document.querySelector(".info");
	// 切歌按钮
	var prev = document.querySelector('.bgm_prev');
	var next = document.querySelector('.bgm_next');
	// 所有歌曲名称
	var bgms = ["喜欢一个人-陈奕迅", "陪你度过漫长岁月-陈奕迅"];
	var bgm_len = bgms.length;
	var cur_index = 0;
	// 播放点击事件绑定
	cont.addEventListener('click', function(){
		if(bgm_audio.paused){
			bgm_audio.play();
			cont_img.src = "img/music_play.png";
			bgm_info.innerHTML = "正在播放: "+bgms[cur_index]+"♪";
		}
		else{
			bgm_audio.pause();
			cont_img.src = "img/music_pause.png";
			bgm_info.innerHTML = "暂停中▶";
		}
	});
	// 前一首歌点击
	prev.addEventListener('click', function(){
		// 更新歌曲下标
		cur_index = cur_index==0?bgm_len-1:cur_index-1;
		// 更新歌曲源
		bgm_audio.pause();
		bgm_audio.src = "src/music/"+bgms[cur_index]+".mp3";
		bgm_audio.load();
		cont_img.src = "img/music_play.png";
		bgm_info.innerHTML = "正在播放: "+bgms[cur_index]+"♪";
	});
	// 后一首歌点击
	next.addEventListener('click', function(){
		// 更新歌曲下标
		cur_index = cur_index==bgm_len-1?0:cur_index+1;
		// 更新歌曲源
		bgm_audio.pause();
		bgm_audio.src = "src/music/"+bgms[cur_index]+".mp3";
		bgm_audio.load();
		cont_img.src = "img/music_play.png";
		bgm_info.innerHTML = "正在播放: "+bgms[cur_index]+"♪";
	});
})