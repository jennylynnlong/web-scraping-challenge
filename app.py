from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data_db"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    # access info from DB
    mars_data = mongo.db.marsData.find_one()
    # return rendered data
    return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scrape():
    # reference to a DB collection
    marsTable = mongo.db.marsData

    # drop the table if exists
    mongo.db.marsData.drop()

    # call scrape_mars script
    mars_data = scrape_mars.scrape_all()
    
    # load the dictionary into MongoDB
    marsTable.insert_one(mars_data)
    
    # go back to index route
    return redirect("/")

if __name__ == "__main__":
    app.run()