try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

# Change encoding to avoid silly errors
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create the output csv file and create headers
f = open('./output/captera_scrape.csv', 'w+')
f.write('"name", "info","company_size", "rating"\n')

# Open file and parse
with open('./data/captera.html', 'rb') as file:
    soup = BeautifulSoup(file,"html.parser")

cnt = 0
err = 0

# Find all member DOM elements
elements = soup.find_all("div", class_="cell-review".split())

# Process them
for member in elements:
	name = ''
	company = ''
	size = ''
	rating = ''

	# Get the name of the user
	info = member.find("div", class_="reviewer-details")
	name_ = info.find("div", class_="epsilon weight-semibold inline-block")
	if(len(name_)>0):
		name = name_

	# additional info
	company_block = info.find_all("div", class_="opacity-threequarters".split())
	company_ = ''
	for cb in company_block:
		value = cb.text.strip()
		if(len(value)>0):
			company_ = company_ + "-" + value
	if(len(company_)>0):
		company = company_

	# Size
	size_ = info.find("div", class_="italic opacity-threequarters").text.strip()
	if(len(size_)>0):
		size = size_

	# Get rating
	rating_block = member.find("span", class_="overall-rating")
	rating_ = rating_block.find("span")
	if(len(rating_)>0):
		rating = rating_
	
	# Return results
	try:
		f.write('"' + name.string + '","' + company + '","' + size + '","'+ rating.string + '"\n')
		cnt =+1
	except:
		print("error with user " + name.string)
		err =+1
message = "inserted " + str(cnt) + " successfully records into the file, there were " + str(err) + " errors"
print(message)