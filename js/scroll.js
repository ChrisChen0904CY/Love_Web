// JavaScript Document
// 获取元素
var slider = document.querySelector('.slider-bar');
// 获取文字内容二
var paragraphs = document.querySelector('.paragraph');
var context = paragraphs[0];
var con_top = context.offsetTop;
// 页面滚动事件
document.addEventListener('scroll', function() {
	if (window.pageYOffset >= con_top){
		slider.style.position = 'fixed';
	}
	else{
		slider.style.position = 'absolute';
	}
})