$(function () {

  $(".delete-applet").each(
        function () {
            var currentEle = $(this);

                var id = currentEle[0].dataset.id

            currentEle.click(function () {

                deleteApplet(id)
            })


        }
    )

  $("#sub").click(function () {
    subit()
  })


$("#image1").click(function () {
  upImage(0)
})


  $("#image2").click(function () {
  upImage(1)
})
$(".item-symptom-button").each(
    function () {
     var currentEle = $(this);



      $(this).click(function () {
        if(currentEle.hasClass("item-symptom-button-selectd"))
        {
          currentEle.removeClass("item-symptom-button-selectd")
        }
        else
        {currentEle.addClass("item-symptom-button-selectd")}

        zhungkuang()
      })

    }

)


})

function up() {


    var formData = new FormData();

    $.ajax({
        type: "POST",
        url: "/imageupapi/",

        data: formData,


        mimeType: "multipart/form-data",
        success: function (returndata) {
          console.log(returndata.toString());
        }
        ,

        error: function (returndata) {
            console.log(returndata.toString());
        }
    });


}
function subit() {


  var form=$("#subform")[0]
  var data=new FormData($("#subform")[0])
  var image1id=$("#image1")[0].dataset.id
  var image2id=$("#image2")[0].dataset.id

    if(image1id==undefined || image2id==undefined)
    {
        alert("请上传两张舌苔图")
        return
    }

  var sick=$(".item-symptom-button")
 var i=0;
    sick.each(
     function () {
       var cur=$(this)
       if(cur.hasClass("item-symptom-button-selectd"))
       {   var id=cur[0].dataset.id
           data.append("symptom["+i+"]",id)
           i++;
       }

     }
 )
    if(i<=4)
    {
        alert("至少选择六项症状")
        return
    }

    if($("#name").val()=="" || $("#name").val()==undefined)
    {
         alert("请输入姓名")
        return
    }
     if($("#tel").val()=="" ||$("#tel").val()==undefined)
    {
         alert("请输入联系电话")
        return
    }

  data.append("image1",image1id)
  data.append("image2",image2id)
     data.append("physicalCondition",$("#sickspan").text())





  data.append("session_key",getQueryString("session_key"))
 $.ajax({
        type: "POST",
        url: "/api/casehistory/",

        data: data,

        cache: false,
        contentType: false,
        processData: false,
        mimeType: "multipart/form-data",
        success: function (returndata) {
            console.log(returndata.toString());
            alert("提交成功")
            window.location="/index/";





        },
        error: function (returndata) {
            console.log(returndata.toString());
            alert("提交失败")
        }
    });


}

function upImage(index) {
  wx.chooseImage({
    count: 1, // 默认9
    sizeType: ['compressed'], // 可以指定是原图还是压缩图，默认二者都有
    sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
    success: function (res) {
        var localIds = res.localIds;


        // 返回选定照片的本地ID列表，localId可以作为img标签的src属性显示图片

   wx.uploadImage({
    localId: localIds, // 需要上传的图片的本地ID，由chooseImage接口获得
    isShowProgressTips: 1, // 默认为1，显示进度提示
    success: function (res) {
        $.ajax(
            {
                url:"/upimage/",
                type:"POST",
                data:{
                    session_key:getQueryString("session_key"),
                    localIds:localIds

                },
                success: function (returndata) {
            console.log(returndata.toString());
          mjson=JSON.parse(returndata)
          if(index==0)
          {

            $("#image1").attr("src",mjson[0].image)
            $("#image1").attr("data-id",mjson[0].id)

          }
           if(index==1)
          {

            $("#image2").attr("src",mjson[0].image)
            $("#image2").attr("data-id",mjson[0].id)


          }


        },
        error: function (returndata) {
            console.log(returndata.toString());
        }




            }
        )




        // 返回图片的服务器端ID
    }
});











    }
});





}
function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]);
    return null;
}
function zhungkuang() {
var i=0;
  $(".item-symptom-button").each(function () {
    var currentEle = $(this);
     var sick =parseInt(currentEle[0].dataset.sick)

    if(currentEle.hasClass("item-symptom-button-selectd"))
    {i=i+sick}

  })
  var p="胃中性"
  if(i>0)
  {

p="胃热"
  }


  if(i<0)
  {p="胃寒"

  }
$("#sickspan").text(p);
}