import scrapy

class BooksSpider(scrapy.Spider):
	name = "books"

	def start_requests(self):
		urls = {
			'https://books.toscrape.com/catalogue/category/books/science_22/',
			'https://books.toscrape.com/catalogue/category/books/poetry_23/'
		}
#This for loop will return the url request and parse 
		for u in urls:
			yield scrapy.Request(url=u, callback=self.parse)

# we define the parse here, what are we looking for. 
	def parse(self, response):

		all_books = response.css("ol.row li")
# Because all the elements we need are in the same table structure we can just use ol

# we now create a variable for for each css response
		for book in all_books:
			img = book.css("div.image_container a img::attr(src)").get()
			name = book.css('h3 a::text').get()
			price = book.css('div.product_price p::text').get()

			yield{

				'url' : img,
				'name' : name,
				'price' : price
			}
