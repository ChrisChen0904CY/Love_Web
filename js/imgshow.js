// JavaScript Document
window.addEventListener('load', function(){
	// 加载完延时2.5秒关闭动画
	var disp_div = document.querySelector('.cssload-main');
	var load_page = document.querySelector('.loading_page');
	var load_timer = setInterval(function() {
		// 关闭加载动画
		load_page.style.display = 'none';
	}, 2500);
	// 获取左右箭头元素
	var arrow_l = document.querySelector('.prev');
	var arrow_r = document.querySelector('.next');
	var focus = document.querySelector('.img_show');
	// 宽度获取
	var img_width = focus.offsetWidth;
	// 小圆圈index
	var circle = 0;
	var num = 0;
	// 鼠标经过显示左右按钮
	focus.addEventListener('mouseenter', function(){
		arrow_l.style.display = 'block';
		arrow_r.style.display = 'block';
		// 停止定时器并清除该变量
		clearInterval(timer);
		timer = null;
	});
	// 鼠标离开隐藏左右按钮
	focus.addEventListener('mouseleave', function(){
		arrow_l.style.display = 'none';
		arrow_r.style.display = 'none';
		// 打开定时器
		timer = setInterval(function() {
		arrow_r.click();
	}, 2000);
	});
	// 动态生成小圆圈
	var ul = focus.querySelector('ul');
	// 获取ol
	var ol = focus.querySelector('.img_navigation');
	// 插入小圆圈
	for(var i = 0; i < ul.children.length; i++){
		// 创建一个li
		var li = document.createElement('li');
		// 记录索引号
		li.setAttribute('index', i);
		// 插入
		ol.appendChild(li);
		// 一边生成一边绑定点击事件
		li.addEventListener('click', function() {
			// 干掉所有人
			for(var i = 0; i < ol.children.length; i++){
				ol.children[i].className = 'none';
			}
			// 留下我自己
			this.className = 'selected';
			// 点击小圆圈移动图片
			// 索引号获取
			var index = this.getAttribute('index');
			animate(ul, -index*img_width);
			// num与circle更新为index
			num = circle = index;
		});
	}
	// 设置第一个为选中
	ol.children[0].className = 'selected';
	// 克隆第一张图放到ul最后面
	var first_img = ul.children[0].cloneNode(true);
	ul.appendChild(first_img);
	// 节流阀
	var flag = true;
	// 点击左侧按钮
	arrow_l.addEventListener('click', function() {
		if(flag) {
			// 关闭节流阀
			flag = false;
			// 走到最后一张则复制第一张并不做动画的展示
			if(num == 0){
				num = ul.children.length - 1;
				ul.style.left = -num * img_width + 'px';
			}
			num--;
			animate(ul, -num*img_width, function() {
				// 打开节流阀
				flag = true;
			});
			circle--;
			// 到头了 切到尾
			circle = circle<0 ? ol.children.length - 1 : circle;
			// 设置小圆圈
			circle_change();
		}
	});
	// 点击右侧按钮
	arrow_r.addEventListener('click', function() {
		if(flag) {
			// 关闭节流阀
			flag = false;
			// 走到最后一张则复制第一张并不做动画的展示
			if(num == ul.children.length-1){
				ul.style.left = 0;
				num = 0;
			}
			num++;
			animate(ul, -num*img_width, function() {
				// 开启节流阀
				flag = true;
			});
			circle++;
			if(circle == ol.children.length) {
				circle = 0;
			}
			// 设置小圆圈
			circle_change();
		}
	});
	// 小圆圈设置
	function circle_change() {
		for(var i = 0; i < ol.children.length; i++){
			ol.children[i].className = '';
		}
		ol.children[circle].className = 'selected';
	};
	// 自动播放设置
	var timer = setInterval(function() {
		// 手动调用右侧点击
		arrow_r.click();
	}, 1500);
});