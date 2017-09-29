$(function () {
$(".delete-button").each(function () {
   var id=this.dataset.id
  $(this).click(function (event) {

     var r=confirm("确认删除吗");
     if (r==true)
     {
     detele(id)
     }


    detele(id)
    event.preventDefault();

  })
  
})

})
  function detele(id) {
      $.ajax({
          url:"/api/casehistory/"+id+"/",
          type:"DELETE",
          success: function (returndata) {

            location.reload(true)
          }






  })
}