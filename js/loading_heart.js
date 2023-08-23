window.addEventListener('load', function(){
	// 加载完延时2.5秒关闭动画
	var disp_div = document.querySelector('.cssload-main');
	var load_timer = setInterval(function() {
		// 手动调用右侧点击
		disp_div.style.display = 'none';
	}, 2500);
})