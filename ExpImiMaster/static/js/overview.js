  var rf_percentage;
  var rf_percentage_total=0;
  var count = 1;
$("#btn1").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression1',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '0'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression1score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn2").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression2',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '1'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression2score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn3").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression3',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '2'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression3score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn4").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression4',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '3'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression4score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn5").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression5',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '4'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression5score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn6").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression6',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '5'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression6score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn7").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression7',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '6'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression7score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn8").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression8',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '7'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression8score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn9").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression9',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '8'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression9score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn10").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression10',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '9'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression10score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn11").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression11',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '10'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression11score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });

 $("#btn12").click(function () {
     count = count +1;
     if (count % 2 )
    {
          $.ajax({
              url: '/expression12',
              method: 'POST',
              dataType: 'JSON',
              data: {'picture': '11'},
              success: function (data) {
                if (data.success) {
                    window.location.href = '/expression12score';
                } else {
                    alert('Error');
                }
            },
            error: function () {

            }
          });
     }
 });


