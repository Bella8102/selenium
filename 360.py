#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('http://hr.360.cn/list')

driver.find_element_by_link_text("技术").click()
num = 1
for i in range (5):

	body=driver.find_element_by_xpath('//tbody')
	links=body.find_elements_by_tag_name('a')

	for link in links:
		
		
		link.click()

		driver.switch_to_window(driver.window_handles[1])

		try:
			box=driver.find_element_by_class_name('detail_box')
		except:
			time.sleep(1)
			driver.refresh()
			time.sleep(1)
			box=driver.find_element_by_class_name('detail_box')
			continue

			#职位名称
		print num
		num += 1
		job_name=box.find_element_by_tag_name('h2').text
		print job_name
		print '\n'

		#职位细节
		job_details=box.find_elements_by_xpath('//li')
		for i in job_details:
			job_detail=i.text
			print job_detail
		print '\n'

		#职位描述
		describe=box.find_element_by_class_name('job_describe')
		print describe.find_element_by_tag_name('h5').text
		print describe.find_element_by_tag_name('div').text
		print '\n'

		#职位要求
		requirement=box.find_element_by_class_name('job_requirement')
		print requirement.find_element_by_tag_name('h5').text
		print requirement.find_element_by_tag_name('div').text
		print '\n'
		print '\n'
	
		
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		time.sleep(2)

	driver.find_element_by_xpath('//li[@id="dataTable_next"]').click()
time.sleep(2)


#python F:\sublime\360.py   
