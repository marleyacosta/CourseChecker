var client = new elasticsearch.Client({
  host: 'http://localhost:9200',
  log: 'trace'
});

client.search({index: term, body: queryBuilder()
}).then(function (resp) {
  var hits = resp.hits.hits;

    var total_found = "<center><h4>" + hits.length + " class section(s) found </h4></center>";
    var course_div = '';
    for (course_id in hits) {

      course_div +=  "<div id = " +  "'" + course_id + "' >" +
        "<table align='center' border='1' cellpadding='5' cellspacing='2'>" +

        "<tr>" +
            "<th colspan='9'>" + hits[course_id]._source.courseInfo + "</th>" +
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

        "<td>" + hits[course_id]._source.classNum + "</td>" +
        "<td>" + hits[course_id]._source.section + "</td>" +
        "<td>" + hits[course_id]._source.daysAndTimes + "</td>" +
        "<td>" + hits[course_id]._source.room + "</td>" +
        "<td>" + hits[course_id]._source.instructor + "</td>" +
        "<td>" + hits[course_id]._source.meetingDates + "</td>" +
        "<td>" + hits[course_id]._source.location + "</td>" +


        "</tr>" +

        "</table>" +

         "</div>";

    }
    //document.getElementById("#courses_div").innerHTML = total_found + course_div;

document.write(total_found + course_div);
}, function (err) {
    document.write("failure </br>");
    document.write(err.message);
});
