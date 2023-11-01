$(document).ready(function () {
    var $slider = $("nav .slider"),
      width = $("nav ul li").width;
    $slider.width(width);
  });
  
  var isactivated = get("x");
  console.log(isactivated);
  
  if (!isactivated) {
    isactivated = "ra";
  }
  
  $(`.${isactivated}`).addClass("isactive isactivated");
  console.log("here");
  
  $(window)
    .resize(function () {
      var $slider = $("nav .slider"),
        width = $("nav ul li").width,
        $isActive = $("nav ul li.isactivated"),
        isX = $isActive.position().left,
        isW = $isActive.width();
      $slider.css({ left: isX, width: isW });
  
      $slider.width(width);
      $("nav ul li").each(function () {
        var x = $(this).position().left,
          w = $(this).width();
        $(this).on({
          mouseenter: function () {
            $slider.css({ left: x, width: w });
            $("nav ul li").removeClass("isactive");
            $(this).addClass("isactive");
          },
          mouseleave: function () {
            $slider.css({ left: isX, width: isW });
            $("nav ul li").removeClass("isactive");
          },
        });
      });
    })
    .resize();
  
  $("nav ul li").on("click", function () {
    $("nav ul li").removeClass("isactivated");
    $(this).addClass("isactivated");
  });
  
  $(".counter").each(function () {
    var $this = $(this),
      countTo = $this.attr("data-count");
  
    $({ countNum: $this.text() }).animate(
      {
        countNum: countTo,
      },
  
      {
        duration: countTo * 100,
        easing: "linear",
        step: function () {
          $this.text(Math.floor(this.countNum));
        },
        complete: function () {
          $this.text(this.countNum);
          //alert('finished');
        },
      }
    );
  });
  
  $(".trigger").on("click", function () {
    if ($(this).hasClass("show")) {
      $(".leftmc .pageinfo").css("transform", "translateX(300px)");
      $(this).removeClass("show");
      $(this).addClass("hide");
      $(this).children("i").removeClass("fa-bars");
      $(this).children("i").addClass("fa-times");
    } else {
      $(".leftmc .pageinfo").css("transform", "translateX(-300px)");
      $(this).removeClass("hide");
      $(this).addClass("show");
      $(this).children("i").removeClass("fa-times");
      $(this).children("i").addClass("fa-bars");
    }
  });
  
  let theEditor;
  
  // EditorClass.create({
  //   toolbar: ["bold", "italic"],
  //   mediaEmbed: {
  //     previewsInData: true,
  //   },
  // })
  //   .then("hgmgh")
  //   .catch("...");
  
  ClassicEditor.create(document.querySelector("#contentDetails"), {
    ckfinder: {
      uploadUrl:
        "/ckfinder/core/connector/php/connector.php?command=QuickUpload&type=Files&responseType=json",
    },
    mediaEmbed: {
      previewsInData: true,
    },
  })
    .then((editor) => {
      theEditor = editor;
    })
    .catch((error) => {
      console.error(error);
    });
  
  function get(name) {
    if (
      (name = new RegExp("[?&]" + encodeURIComponent(name) + "=([^&]*)").exec(
        location.search
      ))
    )
      return decodeURIComponent(name[1]);
  }
  
  function ani(op0, trd, curr) {
    $(`.${op0}`).addClass("op0");
    $(`.${trd}`).addClass("trd");
    $('#' + curr).html("Open All Questions");
    document.getElementById(curr).onclick = function () {
      remove_ani(op0, trd, curr);
    };
  }
  
  function remove_ani(op0, trd, curr) {
    $(`.${op0}`).removeClass("op0");
    $(`.${trd}`).removeClass("trd");
    $('#' + curr).html("ASK A QUESTION");
  
    document.getElementById(curr).onclick = function () {
      ani(op0, trd, curr);
    };
  }

// $(document).ready(function() {
//   $.ajax({
//       type: "GET",
//       url: "http://127.0.0.1:8000/api/user/all-answers",  // Replace with your API endpoint
//       headers: {
//         'Authorization': 'Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiY2Q0YjI5NmEtZGY4Yy00ZGUwLTlmODUtNWVkMjY5MjUwZDkwIiwiZXhwIjoxNjk4ODA1ODczLCJpYXQiOjE2OTg3NzU4NzN9.62B8Lx1Las1w1b4z7jKzKoY_EFxjCJB29EspLOlf0tA',  // Replace with your JWT token
//       },
//       success: function(data) {
//           // Data retrieval was successful
//           var dataContainer = $("#data-container");
//           // dataContainer.empty();  // Clear previous data
          
//           // Iterate through the data and display it
//           data.forEach(function(item) {
//               dataContainer.append("<p>" + item.field_name + "</p>");
//           });
//       },
//       error: function() {
//           // Handle errors
//           console.error("Error fetching data from the API");
//       }
//   });
// });