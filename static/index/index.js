$(function () {
    //因为使用了document，所以js需要放在需要执行的代码下面生效才能生效
    var a=$(".slide-a")
    var num=0;
    var len=a.length;

    setInterval(function(){
        a[num].style.display="none";
        num=++num==len?0:num;
        a[num].style.display="inline-block";

    },3000);//切换时间


})