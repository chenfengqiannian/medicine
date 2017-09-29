
  var canvas = document.createElement("canvas");
  var ctx = canvas.getContext('2d');
  //    瓦片canvas
  var tCanvas = document.createElement("canvas");
  var tctx = tCanvas.getContext("2d");

$(function () {





    $(".close").click(function () {
        $(".deatil-div").hide()
    })

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

    $('#upload').change(function () {
        com(0,this)
        $(this).attr("disabled","disabled")


$(this).hide()

    })

     $("#image1").click(function () {
            $(".deatil-div").show()
            var src=$(this).attr("src")
         if(src=="../static/images/upimage_03.png")
             return
         $(".detail").attr("src",src)
           $(".deatil-div").show()
        })
    $("#image2").click(function () {
if(src=="../static/images/upimage_03.png")
             return
            var src=$(this).attr("src")
            $(".detail").attr("src",src)

        $(".deatil-div").show()
        })

    $('#upload2').change(function () {
        com(1,this)
        $(this).attr("disabled","disabled")
        $(this).hide()


    })


    $(".item-symptom-button").each(
        function () {
            var currentEle = $(this);


            $(this).click(function () {
                if (currentEle.hasClass("item-symptom-button-selectd")) {
                    currentEle.removeClass("item-symptom-button-selectd")
                }
                else {
                    currentEle.addClass("item-symptom-button-selectd")
                }

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

function  androidroapple() {
    var u = navigator.userAgent;
    var isAndroid = u.indexOf('Android') > -1 || u.indexOf('Adr') > -1;
    var isiOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/);


    return isAndroid



}


function subit() {


    var form = $("#subform")[0]
    var data = new FormData($("#subform")[0])
    var image1id = $("#image1")[0].dataset.id
    var image2id = $("#image2")[0].dataset.id

    if (image1id == undefined || image2id == undefined) {
        alert("请上传两张舌苔图")
        return
    }

    var sick = $(".item-symptom-button")
    var i = 0;
    sick.each(
        function () {
            var cur = $(this)
            if (cur.hasClass("item-symptom-button-selectd")) {
                var id = cur[0].dataset.id
                data.append("symptom[" + i + "]", id)
                i++;
            }

        }
    )
    if (i <= 4) {
        alert("至少选择六项症状")
        return
    }

    if ($("#name").val() == "" || $("#name").val() == undefined) {
        alert("请输入姓名")
        return
    }
    if ($("#tel").val() == "" || $("#tel").val() == undefined) {
        alert("请输入联系电话")
        return
    }

    data.append("image1", image1id)
    data.append("image2", image2id)
    data.append("physicalCondition", $("#sickspan").text())


    data.append("session_key", getQueryString("session_key"))
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
            window.history.back();


        },
        error: function (returndata) {
            console.log(returndata.toString());
            alert("提交失败")
        }
    });


}
function upImagef(data,type,index) {

    var text = window.atob(data.split(",")[1]);
        var buffer = new ArrayBuffer(text.length);
        var ubuffer = new Uint8Array(buffer);
        var pecent = 0 , loop = null;

        for (var i = 0; i < text.length; i++) {
            ubuffer[i] = text.charCodeAt(i);
        }

        var Builder = window.WebKitBlobBuilder || window.MozBlobBuilder;
        var blob;

        if (Builder) {
            var builder = new Builder();
            builder.append(buffer);
            blob = builder.getBlob(type);
        } else {
            blob = new window.Blob([buffer], {type: type});
        }







    var formData = new FormData();

         formData.append((new Date()).valueOf()+".jpeg"
        , blob)

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
            mjson = JSON.parse(returndata)
            if (index == 0) {

                $("#image1").attr("src", mjson[0].image)
                $("#image1").attr("data-id", mjson[0].id)

            }
            if (index == 1) {

                $("#image2").attr("src", mjson[0].image)
                $("#image2").attr("data-id", mjson[0].id)


            }
if (androidroapple())
            {

                $(".upimage").css("transform","")


                $(".deatil-div img").css("transform","rotate(0deg)")
                   }



        },
        error: function (returndata) {
            console.log(returndata.toString());
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
                            url: "/upimage/",
                            type: "POST",
                            data: {
                                session_key: getQueryString("session_key"),
                                localIds: localIds

                            },
                            success: function (returndata) {
                                console.log(returndata.toString());
                                mjson = JSON.parse(returndata)
                                if (index == 0) {

                                    $("#image1").attr("src", mjson[0].image)
                                    $("#image1").attr("data-id", mjson[0].id)

                                }
                                if (index == 1) {

                                    $("#image2").attr("src", mjson[0].image)
                                    $("#image2").attr("data-id", mjson[0].id)


                                }


                            },
                            error: function (returndata) {
                                console.log(returndata.toString());
                            }


                        }
                    )


                    // 返回图片的服务器端ID
                },
                error: function (returndata) {
                    console.log(returndata.toString());

                }
            });


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
    var i = 0;
    $(".item-symptom-button").each(function () {
        var currentEle = $(this);
        var sick = parseInt(currentEle[0].dataset.sick)

        if (currentEle.hasClass("item-symptom-button-selectd")) {
            i = i + sick
        }

    })
    var p = "胃中性"
    if (i > 0) {

        p = "胃热"
    }


    if (i < 0) {
        p = "胃寒"

    }
    $("#sickspan").text(p);
}


function com(index,upload) {


        var files = Array.prototype.slice.call(upload.files);

        if (files.length > 9) {
            alert("最多同时只可上传9张图片");
            return;
        }

        files.forEach(function (file, i) {
            if (!/\/(?:jpeg|png|gif)/i.test(file.type)) return;

            var reader = new FileReader();

            reader.onload = function () {
                var result = this.result;
                var img = new Image();
                img.src = result;

                //如果图片大小小于100kb，则直接上传
                if (result.length <= 102400) {
                    img = null;
                    upImagef(data,file.type,index);
                    return;
                }

//                图片加载完毕之后进行压缩，然后上传
                if (img.complete) {
                    callback();
                } else {
                    img.onload = callback;
                }

                function callback() {
                    var data = compress(img);


                    upImagef(data,file.type,index);

                    img = null;
                }

            };

            reader.readAsDataURL(file);
        })
    };


    function compress(img) {
        var initSize = img.src.length;
        var width = img.width;
        var height = img.height;

        //如果图片大于四百万像素，计算压缩比并将大小压至400万以下
        var ratio;
        if ((ratio = width * height / 4000000)>1) {
            ratio = Math.sqrt(ratio);
            width /= ratio;
            height /= ratio;
        }else {
            ratio = 1;
        }

        canvas.width = width;
        canvas.height = height;

//        铺底色
        ctx.fillStyle = "#fff";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        //如果图片像素大于100万则使用瓦片绘制
        var count;
        if ((count = width * height / 1000000) > 1) {
            count = ~~(Math.sqrt(count)+1); //计算要分成多少块瓦片

//            计算每块瓦片的宽和高
            var nw = ~~(width / count);
            var nh = ~~(height / count);

            tCanvas.width = nw;
            tCanvas.height = nh;

            for (var i = 0; i < count; i++) {
                for (var j = 0; j < count; j++) {
                    tctx.drawImage(img, i * nw * ratio, j * nh * ratio, nw * ratio, nh * ratio, 0, 0, nw, nh);

                    ctx.drawImage(tCanvas, i * nw, j * nh, nw, nh);
                }
            }
        } else {
            ctx.drawImage(img, 0, 0, width, height);
        }


        //进行最小压缩
        var ndata = canvas.toDataURL('image/jpeg', 0.1);

        console.log('压缩前：' + initSize);
        console.log('压缩后：' + ndata.length);
        console.log('压缩率：' + ~~(100 * (initSize - ndata.length) / initSize) + "%");

        tCanvas.width = tCanvas.height = canvas.width = canvas.height = 0;

        return ndata;
    }
