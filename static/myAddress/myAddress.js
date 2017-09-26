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
        mdata.name = $("#name").val()
        mdata.contact = $("#contact").val()
        mdata.detailAddress = $("#detailAddress").val()
        mdata.province = $("#province").val()
        mdata.city = $("#city").val()
        mdata.district = $("#district").val()

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