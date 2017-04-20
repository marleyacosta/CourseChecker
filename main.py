import scraperSpring
import scraperSummer
import scraperFall
from multiprocessing import Process

def springTerm():
    spring = scraperSpring.TestFIUSearchPage()
    if spring.springSemester:
        spring_list = spring.scrape()
    else:
        print ("Spring semester is not available")

def summerTerm():
    summer = scraperSummer.TestFIUSearchPage()
    if summer.summerSemester:
        summer_list = summer.scrape()
    else:
        print ("Summer semester is not available")

def fallTerm():
    fall = scraperFall.TestFIUSearchPage()
    if fall.fallSemester:
        fall_list = fall.scrape()
    else:
        print ("Fall semester is not available")

if __name__ == '__main__':
    while (True):
        p1 = Process(target=springTerm)
        p1.start()
        p2 = Process(target=summerTerm)
        p2.start()
        p3 = Process(target=fallTerm)
        p3.start()
        p1.join()
        p2.join()
        p3.join()
