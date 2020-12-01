var settings = {
  "url": "http://192.168.1.55:9001/module_info",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({"product":"17","module":""}),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
