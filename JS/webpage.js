///////////////////////////////////////////////////////////////
// Search animation functions
///////////////////////////////////////////////////////////////

// This function changes the search option in the search box.
$(document).ready(function(e) {
    $('.search-panel .dropdown-menu').find('a').click(function(e) {
        e.preventDefault();
        var param = $(this).attr("href").replace("#", "");
        var concept = $(this).text();
        $('.search-panel span#search_concept').text(concept);
        $('.input-group #search_param').val(param);
    });
});

// This function shows the buffering when loading the homepage
document.onreadystatechange = function() {
    var state = document.readyState
    if (state == 'complete') {
        document.getElementById('interactive');
        document.getElementById('load').style.visibility = "hidden";
    }
}

///////////////////////////////////////////////////////////////
// Logic for displaying the courses on the web page
///////////////////////////////////////////////////////////////

// TODO: Instead of a table make each class it's own div, programmatically add divs, at most 6.
// Make AJAX Call to Populate HTML Table with JSON Data
$.ajax({
    url: 'sample.json',
    dataType: 'json',
    success: function(data) {
        for (var i = 0; i < data.length; i++) {
            var table = $("<tr class = 'course_description'><th colspan='8'>" + data[i].course_name + "</th></tr>" +
                "<tr><th>Class</th><th>Section</th><th>Times</th><th>Room</th><th>Instructor</th><th>Location</th></tr>" +
                "<tr><td>" + data[i].course_id + "</td><td>" + data[i].course_section + "</td><td>" + data[i].time +
                "</td><td>" + data[i].room + "</td><td>" + data[i].instructor + "</td><td>" + data[i].location + "</td><tr>"
            );

            $('#tabl').append(table);
        }


    },
    error: function(jqXHR, textStatus, errorThrown) {
        alert('Error: ' + textStatus + ' - ' + errorThrown);
    }
});
///////////////////////////////////////////////////////////////
// Scrolling Functions
///////////////////////////////////////////////////////////////


// This function create a smooth scrolling effect to the course results when the user clicks on the search button
$("#search-button").click(function() {
    $('html,body').animate({
            scrollTop: $("#course_results_div").offset().top
        },
        400, );
});


// This function create a smooth scrolling effect back to the search homepage when the user clicks on the 'Back to search' link
$("#back_to_search").click(function() {
    $('html,body').animate({
            scrollTop: $("#homepage").offset().top
        },
        400, );
});

///////////////////////////////////////////////////////////////
// This function selects all the locations in the selectpicker
///////////////////////////////////////////////////////////////

function toggleSelectAll(control) {
    var allOptionIsSelected = (control.val() || []).indexOf("All") > -1;
    function valuesOf(elements) {
        return $.map(elements, function(element) {
            return element.value;
        });
    }

    if (control.data('allOptionIsSelected') != allOptionIsSelected) {
        // User clicked 'All' option
        if (allOptionIsSelected) {
            // Can't use .selectpicker('selectAll') because multiple "change" events will be triggered
            control.selectpicker('val', valuesOf(control.find('option')));
        } else {
            control.selectpicker('val', []);
        }
    } else {
        // User clicked other option
        if (allOptionIsSelected && control.val().length != control.find('option').length) {
            // All options were selected, user deselected one option
            // => unselect 'All' option
            control.selectpicker('val', valuesOf(control.find('option:selected[value!=All]')));
            allOptionIsSelected = false;
        } else if (!allOptionIsSelected && control.val().length == control.find('option').length - 1) {
            // Not all options were selected, user selected all options except 'All' option
            // => select 'All' option too
            control.selectpicker('val', valuesOf(control.find('option')));
            allOptionIsSelected = true;
        }
    }
    control.data('allOptionIsSelected', allOptionIsSelected);
}

$('#campus_locations').selectpicker().change(function(){toggleSelectAll($(this));}).trigger('change');

$('#days_of_the_week').selectpicker().change(function(){toggleSelectAll($(this));}).trigger('change');

$('#times_of_day').selectpicker().change(function(){toggleSelectAll($(this));}).trigger('change');


///////////////////////////////////////////////////////////////
// This function selects up to 6 courses in the flowchart
///////////////////////////////////////////////////////////////

var counter = 0;

// if a square and some counter is less than 6 squares selected is clicked on, then add the selected class.

if(){
  counter++;
}

// if clicked again while having selected class, remove the selected class
if(){
  counter--;
}
