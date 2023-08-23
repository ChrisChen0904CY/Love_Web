// JavaScript Document
// 动画函数的封装
function animate(obj, target, callback) {
	// 不同元素绑定不同定时器
	clearInterval(obj.timer);
	obj.timer = setInterval(function() {
		// 获得缓动步长并取整
		var step = (target - obj.offsetLeft) / 10;
		step = step > 0 ? Math.ceil(step) : Math.floor(step);
		if(obj.offsetLeft == target) {
			// 关闭定时器停止动画
			clearInterval(obj.timer);
			// 执行回调函数
			callback && callback();
		}
		obj.style.left = obj.offsetLeft + step + 'px';
	}, 15)
}