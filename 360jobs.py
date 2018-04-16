from selenium import webdriver
import time

class job_360(object):
	
	def __init__(self):
		self.dr = webdriver.Chrome()
		self.dr.get('http://hr.360.cn/list')

	def job(self):		
		time.sleep(2)
		self.dr.find_element_by_link_text('技术').click()
		num=1
		
		for i in range(5):
			tbody=self.dr.find_element_by_tag_name('tbody')
			links = tbody.find_elements_by_tag_name('a')
			
			for link  in links:
				print (num)
				num +=1
				self.job_detail(link)								
					
		self.nextPage()

	#self.quit()
	def job_detail(self,link):
		try:
			link.click()
			self.dr.switch_to_window(self.dr.window_handles[1])
			
			title=self.dr.find_element_by_tag_name('h2')
			print (title.text)

			detail=self.dr.find_element_by_xpath('//div[@class="job_detail clearFix"]')
			lis=detail.find_elements_by_tag_name('li')
			for li in lis:
				print (li.text)
					

			describe=self.dr.find_element_by_class_name('job_describe')
			self.printContent(describe)

			requirement=self.dr.find_element_by_class_name('job_requirement')
			self.printContent(requirement)
			print ('\n')
			self.dr.close()
			self.dr.switch_to_window(self.dr.window_handles[0])
		except:
			self.dr.close()
			return self.job_detail(link)
	
	def printContent(self,section):
		title=section.find_element_by_tag_name('h5')
		print (title.text+':')
		description=section.find_element_by_class_name('description')
		print (description.text)

	def nextPage(self):
		link=self.dr.find_element_by_xpath('//li[@class="paginate_button next"]/a')
		link.click()
		
	def quit(self):
		self.dr.quit()

job_360().job()
