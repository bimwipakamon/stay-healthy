
	// < !--Call Showcase - change 4 from min: 4 and max: 4 to the number of items you want visible-- >

    $(window).load(function () {
        $('#recent-projects').carouFredSel({
            responsive: true,
            width: '100%',
            auto: true,
            circular: true,
            infinite: false,
            prev: {
                button: "#car_prev",
                key: "left",
            },
            next: {
                button: "#car_next",
                key: "right",
            },
            swipe: {
                onMouse: true,
                onTouch: true
            },
            scroll: 2000,
            items: {
                visible: {
                    min: 4,
                    max: 4
                }
            }
        });
    });	