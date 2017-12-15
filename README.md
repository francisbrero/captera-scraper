# captera-scraper
Scrape lead info from specific pages on captera

![Alt Text](http://g.recordit.co/R6QyY1A1fr.gif)

# Initialization
## ensure you have node
If you don't that's a shame 
	=> with nvm go [here](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-with-nvm-node-version-manager-on-a-vps)
	=> old school [here](https://nodejs.org/en/download/)

## ensure you have python 2.7 (at least) and pip
for pyton, go [here](https://www.python.org/downloads/)
for pip, run
```
sudo easy_install pip
```

## install dependencies for the project
### Node
```
npm install
```

### python
```
. setup_env.sh 
```
if you run into errors about ```Permission denied: ‘/Library/Python/2.7/site-packages/```, you might need to change permissions on your python folder. For that run:
```
sudo chown -R $USER /Library/Python/2.7/
```

### folders
create a data, a debug and an output folder

We're now ready to go!

# Step 1 => configure the scraper

Open lib/scraper.js and: 

## input the page you want to scrape
```
	// input the captera page to scraape
	.goto('https://www.capterra.com/p/165410/WooCommerce/')
```

Save

# Step 2 => run the scraper
```
node lib/scraper.js 
```

### Debug:
This creates a couple pictures in debug to ensure everything went smoothly

### Output
The scraper outputs a raw html in ./data called 'captera.html' which contains all the goodness you're looking for


# Step 3 => parse the html to get a clean csv
```
python lib/html_parse.py 
```

this outputs a csv file '/output/captera.csv' text qualified.

Enjoy!


# Comments/feedback 
are welcome!
