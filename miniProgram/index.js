Page({
    data: {
      message: ""
    },
  
    sayHello: function() {
      wx.request({
        url: 'https://your-api-url.com/endpoint', // Replace with your API endpoint
        method: 'GET',  // You can also use 'POST' if needed
        success: (res) => {
          if (res.statusCode === 200) {
            // Assuming the API returns a response like { message: 'Hello World' }
            this.setData({
              message: res.data.message || 'No message returned from API'
            });
          } else {
            this.setData({
              message: 'API call failed!'
            });
          }
        },
        fail: (err) => {
          this.setData({
            message: 'Error in calling API'
          });
        }
      });
    }
  });
  