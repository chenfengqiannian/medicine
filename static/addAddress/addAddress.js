
var app = getApp()

Page({
  data: {
    addressId: '',
    orderId: '',
    provinces: [],
    provinceIds: [],
    provinceIndex: 0,
    cities: [],
    cityIds: [],
    cityIndex: 0,
    districts: [],
    districtIds: [],
    districtIndex: 0,
    name: '',
    contact: '',
    detail: '',
    isDefault: 0,
    provincePara: {
      text: '',
      id: ''
    },
    cityPara: {
      text: '',
      id: ''
    },
    districtPara: {
      text: '',
      id: ''
    }
  },
  onLoad: function(options){
    var id = options.id;    
    var orderId = options.oid; 
    if(id){
      this.getAddressDetail(id);
      this.setData({
        addressId: id
      })
    }
    if(orderId) {
      this.setData({
        orderId: orderId
      })
    }
   
  },
  getAddressDetail: function(id){
    var that = this;

    app.sendRequest({
      url: '/api/address/'+id,
    
      success: function(res){
        
        that.setData({
          name: res.name,
          contact: res.contact,
          detail: res.detailAddress,
         
          provincePara: res.province,
          cityPara: res.city,
          districtPara: res.district,
          region: res.province + "," + res.city + "," + res.district
        })
     }
      
    });
  },
  bindPickerChange:function(e)
  {
    this.setData({
      region: e.detail.value,
      province : e.detail.value[0],
      city: e.detail.value[1],
      district: e.detail.value[2],
    
    })

  },
  
 
  nameInput: function(e){
    this.setData({
      name: e.detail.value
    })
  },
  contactInput: function(e){
    this.setData({
      contact: e.detail.value
    })
  },
  detailInput: function(e){
    this.setData({
      detail: e.detail.value
    })
  },
  formSubmit: function(){
    var para = {};
    var that = this;
    let url = '/api/address/';
    let method='post';
    if(!this.completeAddressInfo()){
      return;
    }

    if (that.data.addressId)
    {
method='put';
url = url + that.data.addressId;      
    }

    app.sendRequest({
      method: method,
      url: url,
      data: {
        province : this.data.provincePara,
        city : this.data.cityPara,
        district : this.data.districtPara,

        name : this.data.name,
        contact : this.data.contact,
        detailAddress : this.data.detail,
      },
      success: function(res){
       
          app.turnBack();
        
      },
      fail:function(res)
      {
     let re=res;
      }
    })
  },
  
  setAddress: function(addressId){
    var orderId = this.data.orderId;

    app.sendRequest({
      url: '/index.php?r=AppShop/setAddress',
      data: {
        order_id: orderId,
        address_id: addressId
      },
      success: function(res){
        app.turnBack();
      }
    });
  },
  completeAddressInfo: function(){
    var data = this.data,
        tip = '';

    if(!tip && !data.name.trim()){
      tip = '请填写名字';
    }
    if(!tip && !data.contact){
      tip = '请填写联系方式';
    }
    if (!tip && !data.region){
      tip = '请选择地区';
    }
   
    if(!tip && !data.detail){
      tip = '请填写详细地址';
    }

    if(tip){
      app.showModal({
        content: tip
      });
      return false;
    }
    return true;
  },
  setDefaultAddress: function(e){
    var checked = e.detail.value;
    if(checked){
      this.setData({
        isDefault: 1
      })
    } else {
      this.setData({
        isDefault: 0
      })
    }
  }
})
