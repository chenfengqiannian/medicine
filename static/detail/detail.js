// detail.js
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
  
  },

  

  onLoad: function (options) {
    if(options.type==1)
    {
      wx.setNavigationBarTitle({
        title: '关于我们'
      })

    }
    this.setData({
      url: options.url,
      type: options.type
    })



  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  var that=this;
    
  var url = that.data.url.replace("http", "https");
    if(!this.data.type==1){
  app.showModal({
    content: '是否要保存到本地？',
    showCancel: true,
    confirmText: '确定',
    cancelText: '取消',
   
    confirm: function () {
     
      wx.downloadFile({
        url: url,
        success: function (e) {
          wx.saveImageToPhotosAlbum({
            filePath: e.tempFilePath,
            success: function (e) {

              app.showModal({
                content: "成功到本地相册"
              });
            },
            fail:function(e)
            {
              app.showModal({
                content: "保存失败" + e.errMsg
              });
              
            }

          })

        },
      fail:function(e)
      {
        app.showModal({
          content: "下载失败" + e.errMsg + that.data.url
        });

      }

      })


    }
  })
    }
  

  
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

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})