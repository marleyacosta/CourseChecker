import scraperSpring

def main():
    classObject = scraperSpring.TestFIUSearchPage()

    if classObject.springSemester:
        scrape = classObject.scrape()
    else:
        scrape = "Semester is not available"

main()
