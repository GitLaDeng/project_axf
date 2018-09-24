/**DOM树加载完毕后执行的操作
 */
$(document).ready(function () {
    //延迟100毫秒
    setTimeout(function () {
        swiper1();
    },100);

});

function swiper1(){
    //加载 #topSwiper
    var mySwiper1 = new Swiper('#topSwiper',{
        //方向 横
        direction:'horizontal',
        //自动轮播
        loop:true,
        //速度
        speeds:500,
        //间隔时间
        autoplay:2000,
        //小圆点
        pagination:'.swpier-pagination',
        //控制左右
        control:true,
    });
}









