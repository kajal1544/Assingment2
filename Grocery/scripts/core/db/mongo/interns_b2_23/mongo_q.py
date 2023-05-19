from pymongo import MongoClient

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")

database = client["interns_b2_23"]

grocery = database.kajal_grocery_item_collection


