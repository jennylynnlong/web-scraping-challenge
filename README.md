# Mission to Mars Challenge

## Details About the Challenge
This assignment was designed to challenge me to build a web application that scrapes various websites for data related to the Mission to Mars. Once this information is scraped, it is displayed in a single HTML page.

## Step 1 - Web Scraping
In this [Jupyter notebook](/Missions_to_Mars/Mission_to_Mars-Starter.ipynb), you will find the following:
1. ***NASA Mars News***
   - This scrapes the [Mars News Site](https://redplanetscience.com/) and collects the latest news title and related paragraph text and assigns them to variables as shown below.
     - ![image](https://user-images.githubusercontent.com/88349512/146228155-9c428863-5dbb-428b-843c-e9087743baeb.png)
     - ![image](https://user-images.githubusercontent.com/88349512/146228220-6df3c4cd-063e-4a7d-a649-387a32572d8b.png)
2. ***JPL Mars Space Images - Featured Image***
   - Navigates through the [Featured Space Image Site](https://spaceimages-mars.com/) and assigns the full-sized featured Mars image to a url string variable.
     - ![image](https://user-images.githubusercontent.com/88349512/146260801-41b14483-4fb8-417e-99be-a859485ab97f.png)
     - ![image](https://user-images.githubusercontent.com/88349512/146260873-2fdce374-acd4-4195-acc4-5e7b5cf77b19.png)
3. ***Mars Facts***
   - Visits the [Mars Facts](https://galaxyfacts-mars.com/) page and uses the Pandas library to scrape the Mars-Earth comparison table and convert that information to a HTML string.
     - ![image](https://user-images.githubusercontent.com/88349512/146261342-047ff35f-adc3-4859-8860-dcb08f5ad89b.png)
     - ![image](https://user-images.githubusercontent.com/88349512/146261386-bca5915b-e1c9-4b58-b4a6-bdaa8e5a334f.png)
4. ***Mars Hemispheres***
   - Clicks through each link on the [Mars Hemispheres](https://marshemispheres.com/) page and pulls out the full resolution image url and its title. This code then creates a dictionary for each hemisphere and appends these to a list.
     - ![image](https://user-images.githubusercontent.com/88349512/146261931-946bba71-523b-4651-a537-85e86d4f2461.png)

## Step 2 - MongoDB and Flask Application
This step includes using MongoDB with Flask templating to create a new HTML page that displays the information that was scraped during Step 1.
1. I started by converting the [Jupyter notebook](/Missions_to_Mars/Mission_to_Mars-Starter.ipynb) to a python script titled [scrape_mars.py](/scrape_mars.py) that executes all of the code from the notebook and returns one dictionary containing all of the scraped data.
   - ![image](https://user-images.githubusercontent.com/88349512/146263084-bb41d3ca-0036-4d39-8662-171dc0243ebd.png)
2. Then, I used another python [script](/app.py) to create a route called /scrape which imports my scrape_mars.py script and calls the scrape function.
   - ![image](https://user-images.githubusercontent.com/88349512/146263388-e454f986-f4bd-4a14-b1f5-fec98769d077.png)
3. Inside of that same [script](/app.py) I also created a root route (/) that queries the Mongo database and passes the Mars data into an HTML template to display the data.
   - ![image](https://user-images.githubusercontent.com/88349512/146263631-753d1aa7-fce1-4cf5-99f5-3f60e208bc18.png)
   - ![image](https://user-images.githubusercontent.com/88349512/146263762-4244427d-f8d5-430c-be0c-3896e7b2376e.png)
4. Finally, I created a template HTML file titled [index.html](/templates/index.html) that takes the Mars dictionary and displays all of the data in the appropriate HTML elements.
   - ![image](/JLL_final_app_screenshot.png)

## How to Run the Code
1. Pull the files from this repository
2. Open the [Jupyter notebook](/Missions_to_Mars/Mission_to_Mars-Starter.ipynb) file and run the kernel.
3. Open your files from this repository via your File Explorer on your computer.
4. Right click and select "Git Bash Here"
5. Type "python app.py" in your terminal and press enter.
6. Open your web browser and type: localhost:5000/
7. Click "Scrape New Data" for updated news articles.
   - ![image](https://user-images.githubusercontent.com/88349512/146265251-5a25fc73-e71f-487b-9875-4b5a680bcdc2.png)
