*****READ ME*******

To start you will need Scrapy installed.
	-  ! pip install scrapy
	
Once installed you need to start the project
	- scrapy startproject bookstest

open a shell to the site

	- scrapy shell "https://books.toscrape.com/catalogue/category/books/science_22/index.html"

Test to see if you get a response

	- response.css('ol.row')
	
Then using the inspect element in the browser you can dive into the exact tables you need.

Add the objects to your Py code.



Once your py code is complete run the below command to output your results.

	- scrapy crawl books -O bookstest.csv

