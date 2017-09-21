$(function () {
  $(".get-code-btn").click(function () {
    code()
  })

})
function code() {
  var phone=$(".code-tel").val()

  $.ajax({
    url:"/code/",
    data:{"phone":phone,"session_key":getQueryString("session_key")},
    type:"GET",
    success: function (returndata) {
          console.log(returndata.toString());
      var second=60;
      interval = setInterval(function(){
          if(second < 0) {
            clearInterval(interval);
            $(".code-tel").attr('disabled',false);



          } else {
              $(".code-tel").attr('disabled',true);
            $(".code-tel").text(second)
            second--;
          }
        }, 1000);
      },
    error: function (returndata) {
            console.log(returndata.toString());
        }




  })


}

function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]);
    return null;
}

function sub() {
  $.ajax({
        url: '/code/',
        type: 'POST',
        data: {
          code: $(".codeinupt").val(),
          phone:$(".code-tel").val()
        },
        success: function () {



         alert("绑定成功")
          window.history.back();
        },
        fail: function () {
          alert("验证码错误")


        }
      }
  )

}