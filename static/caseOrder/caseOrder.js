// pages/caseOrder/caseOrder.js
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {


  },

  /**
   * 生命周期函数--监听页面加载
   */
  getCurrentPage:function()
{},
  onLoad: function (options) {
    let type=options.type;
    let url;
    var that = this;
    app.checkLogin()
    this.setData(
      {
        type: type
        })
    if(type)
    {
      url ="/api/messages/"
    }else
    {
      url = "/api/casehistory/"

    }
    
    app.sendRequest({
      url: url,
      success: function (res) {
        for (var i=0;i<=res.length-1;i++)
        {
          res[i].modDateTime = String(res[i].modDateTime).split(".")[0]


        }
        that.setData({
          message:res})
      }
     
    })

   



  },
  dataInitial:function()
  {}
  ,
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },
orderDetail:function(e)
{let id = e.currentTarget.dataset.id;
let router= e.currentTarget.dataset.router;
if(!this.data.type)
{
 app.turnToPage('/pages/' + router + '/' + router +'?id='+id);

}





}
  
 
})