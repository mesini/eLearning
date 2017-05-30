var tour_template = `<div style="background-color: black;color: grey;" class='popover tour'>
                        <div class='arrow'></div>
                        <h3 class='popover-title'></h3>
                        <div class='popover-content'></div>
                        <div class='popover-navigation'>
                            <button class='btn btn-default' data-role='prev'>« Prev</button>
                            <span data-role='separator'>|</span>
                            <button class='btn btn-default' data-role='next'>Next »</button>
                        </div>
                        <button class='btn btn-default' data-role='end'>End tour</button>
                      </div>`

var createTour = function(){

    var tour = new Tour({
        storage : false,
        template: tour_template,
        onEnd: function (tour) {$('#myModal').modal('show');},
    });

    tour.addSteps([
      {
        element: "#toladata",
        placement: "bottom",
        title: "Welcome to our landing page!",
        content: "This tour will guide you through some of the features we'd like to point out."
      },
      {
        element: "#contact",
        placement: "bottom",
        title: function(){ return "<code>hello world</code>"},
        content: "Here are the sections of this page, easily laid out."
      },
      {
        element: "#contact",
        placement: "top",
        backdrop: true,
        title: "Main section",
        content: "This is a section that you can read. It has valuable information."
      },
    ]);
    // Initialize and start the tour
    tour.init();
    tour.start();
}

