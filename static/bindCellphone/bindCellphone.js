
var app = getApp()
var util = require('../../utils/util.js')

Page({
  data: {
    hideVerifyPhone: true,
    
    oldCode: '',
    oldCodeBtnDisabled: false,
    oldCodeStatus: '获取验证码',
    nextStepDisabled: false,
    newPhone: '',
    newCode: '',
    newCodeBtnDisabled: false,
    newCodeStatus: '获取验证码',
    bindNewPhoneBtnDisabled: false,
    codeInterval: 60
  },
  onLoad: function(){
    app.checkLogin()
    var userInfo = app.getUserInfo();
   

   
  },
  dataInitial:function()
  {},
  sendCodeToNewPhone: function(){
    if (this.data.newCodeBtnDisabled)
    {return;}
    var that = this;
    
    
    this.setData({
      oldCodeStatus: '正在发送...',
      oldCodeBtnDisabled: true
    })
    app.sendRequest({
      url: '/code/',
      data:{
        phone:that.data.newPhone

      } ,
      success: function(){
        var second = that.data.codeInterval,
            interval;

        app.showToast({
          title: '已发送',
          icon: 'success'
        })
        interval = setInterval(function(){
          if(second < 0) {
            clearInterval(interval);
            that.setData({
              newCodeStatus: '获取验证码',
              newCodeBtnDisabled: false
            })
          } else {
            that.setData({
              newCodeStatus: second+'s',
              newCodeBtnDisabled:true
            })
            second--;
          }
        }, 1000);
      },
      complete: function(){
        that.setData({
          newCodeStatus: '获取验证码',
          newCodeBtnDisabled: false
        })
      }
    })

  },
  inputOldCode: function(e){
    this.setData({
      oldCode: e.detail.value
    })
  },
  bindNewPhone: function(){
    var that = this;
    if (!this.data.newCode){
      app.showModal({
        content: '请输入验证码'
      })
      return;
    }
   
    this.setData({
      nextStepDisabled: true
    })
    app.sendRequest({
      url: '/code/',
      method: 'post',
      data: {
        code: this.data.newCode,
        phone: this.data.newPhone
      },
      success: function(){
       
        app.showToast({
          title: '绑定成功',
          icon: 'success'
        })
        app.globalData.userInfo.phone = this.data.newPhone;

        setTimeout(function () {
          app.turnBack()
        }.bind(this), 2000)
      },
      fail:function()
      {
        app.showToast({
          title: '验证码错误',
          icon: 'fail'
        })

      }
      ,
      complete: function(){
        that.setData({
          nextStepDisabled: false
        })
      }
    })
  },
  inputPhone: function(e){
    this.setData({
      newPhone: e.detail.value
    })
  },
  inputNewCode: function (e) {
    this.setData({
      newCode: e.detail.value
    })
  },
  
 

})
