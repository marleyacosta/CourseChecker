var client = new elasticsearch.Client({
    host: 'http://localhost:9200',
    log: 'trace'
});

client.search({
    index: term,
    body: queryBuilder()
}).then(function(resp) {
    var hits = resp.hits.hits;

    var total_found = "<center><h4>" + hits.length + " class section(s) found </h4></center>";
    var course_div = '';
    for (course_id in hits) {

        course_name = hits[course_id]._source.courseInfo
        class_number = hits[course_id]._source.classNum
        class_section = hits[course_id]._source.section
        class_times = hits[course_id]._source.daysAndTimes
        class_room = hits[course_id]._source.room
        class_instructor = hits[course_id]._source.instructor
        class_meeting_dates = hits[course_id]._source.meetingDates
        class_location = hits[course_id]._source.location

        if (course_id != 0) {


            if (hits[course_id - 1]._source.courseInfo === hits[course_id]._source.courseInfo) {


                course_div += "<tr>" +

                    "<td>" + class_number + "</td>" +
                    "<td>" + class_section + "</td>" +
                    "<td>" + class_times + "</td>" +
                    "<td>" + class_room + "</td>" +
                    "<td>" + class_instructor + "</td>" +
                    "<td>" + class_meeting_dates + "</td>" +
                    "<td>" + class_location + "</td>" +

                    "</tr>" ;
            }
            else{

              course_div += "</table>" + "</div>";

              course_div += "<div id = " + "'" + course_id + "'  >" +

                  "<table align='center' border='1' cellpadding='5' cellspacing='2'>" +

                  "<tr>" +
                  "<th colspan='9'>" + course_name + "</th>" +
                  "</tr>" +

                  "<tr>" +
                  "<th>Class</th>" +
                  "<th>Section</th>" +
                  "<th>Days & Times</th>" +
                  "<th>Room</th>" +
                  "<th>Instructor</th>" +
                  "<th>Meeting Dates</th>" +
                  "<th>Location</th>" +
                  "</tr>" +

                  "<tr>" +

                  "<td>" + class_number + "</td>" +
                  "<td>" + class_section + "</td>" +
                  "<td>" + class_times + "</td>" +
                  "<td>" + class_room + "</td>" +
                  "<td>" + class_instructor + "</td>" +
                  "<td>" + class_meeting_dates + "</td>" +
                  "<td>" + class_location + "</td>" +

                  "</tr>";

            }
        }
        else{

          course_div += "<div id = " + "'" + course_id + "'  >" +

              "<table align='center' border='1' cellpadding='5' cellspacing='2'>" +

              "<tr>" +
              "<th colspan='9'>" + course_name + "</th>" +
              "</tr>" +

              "<tr>" +
              "<th>Class</th>" +
              "<th>Section</th>" +
              "<th>Days & Times</th>" +
              "<th>Room</th>" +
              "<th>Instructor</th>" +
              "<th>Meeting Dates</th>" +
              "<th>Location</th>" +
              "</tr>" +

              "<tr>" +

              "<td>" + class_number + "</td>" +
              "<td>" + class_section + "</td>" +
              "<td>" + class_times + "</td>" +
              "<td>" + class_room + "</td>" +
              "<td>" + class_instructor + "</td>" +
              "<td>" + class_meeting_dates + "</td>" +
              "<td>" + class_location + "</td>" +

              "</tr>";
        }
    }
    document.getElementById("courses_div").innerHTML = total_found + course_div ;
}, function(err) {
    document.write("failure </br>");
    document.write(err.message);
});
