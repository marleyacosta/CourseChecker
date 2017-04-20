import scraperFall

def main():
    classObject = scraperFall.TestFIUSearchPage()

    if classObject.fallSemester:
        scrape = classObject.scrape()
    else:
        scrape = "Semester is not available"

main()
