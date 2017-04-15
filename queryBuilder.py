import subprocess
from subprocess import call

### NEED TO GET THESE GLOBAL VARIABLES FROM USER INPUT ###
# Term and file_ID are required inputs
term = "summer"
file_ID = "2"

course_list = ["CNT 4713", "COP 2210"]
location = None
instructor = "Downey"
days = ["Tu", "Th", "Sa", "Su"]     # user searched Mo We Fr  (reverse logic)
                                    # if user didn't specify days then [] is returned
times = ["morning", "afternoon"]
section = None
##########################################################

def main():
    query = 'curl -XPOST "localhost:9200/' + term + '/_search?pretty" -d \'{"from": 0, "size": 1000, "query": {"bool": {'

    if must() is not None and must_not() is None and filter_courses() is None and filter_times() is None:
        query = query + must() + '}}}\''
    elif must() is None and must_not() is not None and filter_courses() is None and filter_times() is None:
        query = query + must_not() + '}}}\''
    elif must() is None and must_not() is None and filter_courses() is not None and filter_times() is None:
        query = query + filter_courses() + '}}}\''
    elif must() is None and must_not() is None and filter_courses() is None and filter_times() is not None:
        query = query + filter_times() + '}}}\''
    elif must() is not None and must_not() is not None and filter_courses() is None and filter_times() is None:
        query = query + must() + ', ' + must_not() + '}}}\''
    elif must() is not None and must_not() is None and filter_courses() is not None and filter_times() is None:
        query = query + must() + ', ' + filter_courses() + '}}}\''
    elif must() is not None and must_not() is None and filter_courses() is None and filter_times() is not None:
        query = query + must() + ', ' + filter_times() + '}}}\''
    elif must() is None and must_not() is not None and filter_courses() is not None and filter_times() is None:
        query = query + must_not() + ', ' + filter_courses() + '}}}\''
    elif must() is None and must_not() is not None and filter_courses() is None and filter_times() is not None:
        query = query + must_not() + ', ' + filter_times() + '}}}\''
    elif must() is None and must_not() is None and filter_courses() is not None and filter_times() is not None:
        query = query + filter_courses() + ', ' + filter_times() + '}}}\''
    elif must() is not None and must_not() is not None and filter_courses() is not None and filter_times() is None:
        query = query + must() + ', ' + must_not() + ', ' + filter_courses() + '}}}\''
    elif must() is not None and must_not() is not None and filter_courses() is None and filter_times() is not None:
        query = query + must() + ', ' + must_not() + ', ' + filter_times() + '}}}\''
    elif must() is not None and must_not() is None and filter_courses() is not None and filter_times() is not None:
        query = query + must() + ', ' + filter_courses() + ', ' + filter_times() + '}}}\''
    elif must() is None and must_not() is not None and filter_courses() is not None and filter_times() is not None:
        query = query + must_not() + ', ' + filter_courses() + ', ' + filter_times() + '}}}\''
    elif must() is not None and must_not() is not None and filter_courses() is not None and filter_times() is not None:
        query = query + must() + ', ' + must_not() + ', ' + filter_courses() + ', ' + filter_times() + '}}}\''
    else:
        print ("ERROR: Input is needed!")
        return

    #with open(file_ID + ".txt", "w") as output:
    #    subprocess.call(query, stdout = output)
    print(query)
    call(query)


def must():
    str_must = None

    if location is not None:
        str_location = '{"match_phrase": {"location": "' + location + '"}}'
    if instructor is not None:
        str_instructor = '{"match_phrase": {"instructor": "' + instructor + '"}}'
    if section is not None:
        str_section = '{"match_phrase": {"section": "' + section + '"}}'

    if location is not None and instructor is None and section is None:
        str_must = '"must": [' + str_location + ']'
    elif location is None and instructor is not None and section is None:
        str_must = '"must": [' + str_instructor + ']'
    elif location is None and instructor is None and section is not None:
        str_must = '"must": [' + str_section + ']'
    elif location is not None and instructor is not None and section is None:
        str_must = '"must": [' + str_location + ', ' + str_instructor + ']'
    elif location is not None and instructor is None and section is not None:
        str_must = '"must": [' + str_location + ', ' + str_section + ']'
    elif location is None and instructor is not None and section is not None:
        str_must = '"must": [' + str_instructor + ', ' + str_section + ']'
    elif location is not None and instructor is not None and section is not None:
        str_must = '"must": [' + str_location + ', ' + str_instructor + ', ' + str_section + ']'

    return str_must


def must_not():
    str_not = None
    i = 0

    if len(days) is not 0:
        str_not = '"must_not": ['
        while(i < len(days)):
            str_not = str_not + '{"match_phrase": {"days": "' + days[i] + '"}}'
            i = i + 1

            if (len(days) - i is 0):
                continue
            else:
                str_not = str_not + ', '
        str_not = str_not + ']'

    return str_not


def filter_courses():
    str_courses = None
    i = 0

    if len(course_list) is not 0:
        str_courses = '"filter": {"bool": {"should": ['
        while(i < len(course_list)):
            str_courses = str_courses + '{"match_phrase": {"courseInfo": "' + course_list[i] + '"}}'
            i = i + 1

            if (len(course_list) - i is 0):
                continue
            else:
                str_courses = str_courses + ', '
        str_courses = str_courses + ']}}'

    return str_courses


def filter_times():
    str_times = None
    i = 0

    if len(times) is not 0:
        str_times = '"filter": {"bool": {"should": ['
        while(i < len(times)):
            str_times = str_times + '{"match_phrase": {"time": "' + times[i] + '"}}'
            i = i + 1

            if (len(times) - i is 0):
                continue
            else:
                str_times = str_times + ', '
        str_times = str_times + ']}}'

    return str_times


main()
