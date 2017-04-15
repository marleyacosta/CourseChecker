import scraperSummer
import json

def main():
    classObject = scraperSummer.TestFIUSearchPage()

    if classObject.summerSemester:
        availability_list = classObject.scrape()
        #print (json.dumps(availability_list))
    else:
        print ("Semester is not available")

main()
