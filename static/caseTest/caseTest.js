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


$("#upload").change(function () {
  upImage(0)
})


  $("#upload2").change(function () {
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



        },
        error: function (returndata) {
            console.log(returndata.toString());
        }
    });


}

function upImage(index) {
  if(index==0)
  {
    var files = $("#upload")[0].files

  }
  else
  {var files = $("#upload2")[0].files


  }

    var formData = new FormData();

         formData.append((new Date()).valueOf()
        , files[0])

    $.ajax({
        type: "POST",
        url: "/imageupapi/",

        data: formData,

        cache: false,
        contentType: false,
        processData: false,
        mimeType: "multipart/form-data",
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