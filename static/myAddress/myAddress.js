$(function () {


    $("#addresssave").click(function () {
        save()
    })
    $(".myAddress-bottom-nav").click(function () {
        $("#formaddressa").show()
         $(".myAddress-bottom-nav").hide()

    })
    
})

function save()
{
    try {

        var mdata = {}
        mdata.session_key = getQueryString("session_key")
        mdata.name = $("[name|='name']").val()
        mdata.contact = $("[name|='contact']").val()
        mdata.detailAddress = $("[name|='detailAddress']").val()
        mdata.province = $("[name|='province]").val()
        mdata.city = $("[name|='city']").val()
        mdata.district = $("[name|='district']").val()

    }
    catch(err)
        {alert(err.name+err.message)
        }

    $.ajax({
        type: "POST",
        url: "/api/address/",
        data:mdata,




        mimeType: "multipart/form-data",
        success: function (returndata) {
          console.log(returndata.toString());
             location.reload(true)

        }
        ,

        error: function (returndata) {
            alert(returndata.toString())
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