$(function () {
  $(".detail").click(function () {

    $(this).hide()
    
  })

  $("div.line").click(function () {
    $(".detail").show()
  })
})