from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from elasticsearch import Elasticsearch
from datetime import time
from time import sleep
import os


class TestFIUSearchPage():

	def __init__(self):
		self.driver = webdriver.PhantomJS(executable_path=r'/Users/maurelyacosta/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
		self.driver.get("https://pslinks.fiu.edu/psc/cslinks/EMPLOYEE/CAMP/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL&FolderPath=PORTAL_ROOT_OBJECT.HC_CLASS_SEARCH_GBL&IsFolder=false&IgnoreParamTempl=FolderPath,IsFolder")

	def fallSemester(self):
		term = self.driver.find_element_by_xpath('//*[@id="win0divCLASS_SRCH_WRK2_STRM$35$"]').text
		if "Fall" in term:
			return True
		else:
			return False

	def search_request(self, num, pre):
		courseNumber = self.driver.find_element_by_id('SSR_CLSRCH_WRK_CATALOG_NBR$4')
		courseNumber.send_keys(num)
		prefix = self.driver.find_element_by_id('SSR_CLSRCH_WRK_SUBJECT$3')
		prefix.send_keys(pre)
		self.driver.find_element_by_id('CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH').click()

	def getCourses(self, courses, INDEX_N, TYPE_N):
		course = {}

		try:
			element_present = EC.presence_of_element_located((By.ID, 'win0divSSR_CLSRSLT_WRK_GROUPBOX1'))
			WebDriverWait(self.driver, 30).until(element_present)
		except TimeoutException:
			print ("Loading took too much time!")

		classSectionsFound = self.driver.find_element_by_xpath('//*[@id="win0divSSR_CLSRSLT_WRK_GROUPBOX1"]/table/tbody/tr[1]/td').text
		n = int(classSectionsFound.partition(' ')[0])
		i = 0
		while(i < n):
			outinfo = self.driver.find_element_by_xpath('//*[@id="win0divSSR_CLSRSLT_WRK_GROUPBOX2GP$0"]').text
			course['courseInfo'] = outinfo.replace('\n','<br>')
			classnuminfo = self.driver.find_element_by_xpath('//*[@id="MTG_CLASS_NBR$' + str(i) + '"]').text
			course['classNum'] = classnuminfo.replace('\n','<br>')
			outsection = self.driver.find_element_by_xpath('//*[@id="MTG_CLASSNAME$' + str(i) + '"]').text
			course['section'] = outsection.replace('\n','<br>')
			daysandtimesinfo = self.driver.find_element_by_xpath('//*[@id="MTG_DAYTIME$' + str(i) + '"]').text
			course['daysAndTimes'] = daysandtimesinfo.replace('\n','<br>')

			if daysandtimesinfo != 'TBA':
				course['days'] = self.getDays(daysandtimesinfo)
				course['time'] = self.getTime(daysandtimesinfo)

			roominfo = self.driver.find_element_by_xpath('//*[@id="MTG_ROOM$' + str(i) + '"]').text
			course['room'] = roominfo.replace('\n','<br>')
			instructorinfo = self.driver.find_element_by_xpath('//*[@id="MTG_INSTR$' + str(i) + '"]').text
			course['instructor'] = instructorinfo.replace('\n','<br>')
			meetingdatesinfo = self.driver.find_element_by_xpath('//*[@id="MTG_TOPIC$' + str(i) + '"]').text
			course['meetingDates'] = meetingdatesinfo.replace('\n','<br>')
			locationinfo = self.driver.find_element_by_xpath('//*[@id="DERIVED_CLSRCH_DESCR$' + str(i) + '"]').text
			course['location'] = locationinfo.replace('\n','<br>')

			#Unique identifier of each course created within loop. Each loop
			#will create a new identifier for each unique course within a set
			#of similar courses
			ID_FIELD = 'classNum'
			op_dict = {
				"index": {
					"_index": INDEX_N,
					"_type": TYPE_N,
					"_id": course[ID_FIELD]
				}
			}
			courses.append(op_dict) #added
			courses.append(course)
			i = i + 1
			course = {}

		return courses

	def getDays(self, info):
		dayStr = ""

		if "Mo" in info:
			dayStr = dayStr + "Mo "
		if "Tu" in info:
			dayStr = dayStr + "Tu "
		if "We" in info:
			dayStr = dayStr + "We "
		if "Th" in info:
			dayStr = dayStr + "Th "
		if "Fr" in info:
			dayStr = dayStr + "Fr "
		if "Sa" in info:
			dayStr = dayStr + "Sa "
		if "Su" in info:
			dayStr = dayStr + "Su"

		return dayStr

	def getTime(self, info):
		# morning = 6:00AM - 11:59AM
	    # afternoon = 12:00PM - 4:59PM
	    # evening = 5:00PM - 7:59PM
	    # night = 8:00PM - 5:59AM
		course_time = info.split(' ', 2)[1]
		hour = int(course_time.split(':')[0])

		if "PM" in course_time and hour is not 12:
			hour = hour + 12
			minute = int(course_time.split(':')[1].split('PM')[0])
		elif "PM" in course_time and hour is 12:
			minute = int(course_time.split(':')[1].split('PM')[0])
		elif "AM" in course_time and hour is not 12:
			minute = int(course_time.split(':')[1].split('AM')[0])
		else:
			hour = 0
			minute = int(course_time.split(':')[1].split('AM')[0])

		if time(6) <= time(hour, minute) <= time(11, 59):
			timeStr = "morning"
		elif time(12) <= time(hour, minute) <= time(16, 59):
			timeStr = "afternoon"
		elif time(17) <= time(hour, minute) <= time(19, 59):
			timeStr = "evening"
		else:
			timeStr = "night"

		return timeStr

	def modifySearch(self):
		self.driver.find_element_by_id('CLASS_SRCH_WRK2_SSR_PB_MODIFY').click()

	def clearSearch(self):
		try:
			element_present = EC.presence_of_element_located((By.ID, 'CLASS_SRCH_WRK2_SSR_PB_CLEAR'))
			WebDriverWait(self.driver, 30).until(element_present)
		except TimeoutException:
			print ("Loading took too much time!")

		self.driver.find_element_by_id('CLASS_SRCH_WRK2_SSR_PB_CLEAR').click()

	def checkSearch(self):
		if(len(self.driver.find_elements_by_id('DERIVED_CLSMSG_ERROR_TEXT')) > 0):
			return True

	def checkOverflow(self):
		if(len(self.driver.find_elements_by_id('win0divDERIVED_SSE_DSP_SSR_MSG_TEXT')) > 0):
			return True

	def clearAndSearch(self, num, pre):
		self.clearSearch()
		sleep(1.5)
		self.search_request(num, pre)
		sleep(1)

	#Added parameters needed to build dict objects
	def scrapeAndModifySearch(self, courses, esindex, estypename):
		self.getCourses(courses, esindex, estypename)
		self.modifySearch()

	def writeToCourseNumList(self):
		with open('courseNumList.txt') as f:
			courseNums = f.readlines()
		courseNums = [x.strip('\n') for x in courseNums]
		return courseNums

	def writeToCoursePrefixList(self):
		with open('coursePrefixList.txt') as f:
			coursePres = f.readlines()
		coursePres = [x.strip('\n') for x in coursePres]
		return coursePres

	def scrape(self):
		i = 0
		courseNumList = self.writeToCourseNumList()
		coursePrefixList = self.writeToCoursePrefixList()
		courses = []
		course_state = [["0"]*2 for i in range(51)]

		#elasticsearch host variable
		ES_HOST = {
			"host" : "localhost", #added
			"port" : 9200 #added
		}
		INDEX_NAME = 'fall' #added
		TYPE_NAME = 'somecscourse' #added

		self.driver.find_element_by_xpath('//select[@id="CLASS_SRCH_WRK2_STRM$35$"]/option[@value="1178"]').click()
		sleep(1)

		#While loop returns a list of dict objects that will be bulk indexed
		#into a newly created index
		while(i < len(courseNumList)):
			self.clearAndSearch(courseNumList[i], coursePrefixList[i])
			course_state[i][0] = coursePrefixList[i] + "_" + courseNumList[i]

			if(self.checkSearch() == True):
				i = i + 1
				continue
			if(self.checkOverflow() == True):
				self.driver.find_element_by_xpath('//*[@id="#ICSave"]').click()
			#Added index information as parameter to build dict objects
			self.scrapeAndModifySearch(courses, INDEX_NAME, TYPE_NAME)
			course_state[i][1] = "1"
			i = i + 1

		#create ES clinet and index
		esearch = Elasticsearch(hosts = [ES_HOST])

		#Replace exisiting index
		if esearch.indices.exists(INDEX_NAME):
			print ("deleting %s index..." % INDEX_NAME)
			res = esearch.indices.delete(index = INDEX_NAME)
			print ("response: %s" % res)

		#Number of indices
		request_body = {
			"settings" : {
				"number_of_shards" : 1,
				"number_of_replicas" : 0
			}
		}

		#create index
		print ("creating %s index..." % INDEX_NAME)
		res = esearch.indices.create(index = INDEX_NAME, body = request_body)
		print ("response %s" % res)

		#bulk index
		print ("bulk indexing...")
		res = esearch.bulk(index = INDEX_NAME, body = courses, refresh = True)

		return course_state
