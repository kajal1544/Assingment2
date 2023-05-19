from schemas.model import Grocery
from scripts.constants.aggregation import DatabaseConstants
# from scripts.constants.app_constants import db_constant_object
from scripts.core.db.mongo.interns_b2_23.mongo_q import grocery


class Grocery_handler:

    def add_item(self, item_id: int, item: Grocery):
        try:
            if list(grocery.find({"item_id": item_id})):
                return {"error": "This ID is already present"}
            grocery.insert_one(item.dict())
            return {"message": "Successfully Added"}

        except Exception as e:
            return {"error": str(e)}

    def delete_item(self, item_id: int):
        try:
            if list(grocery.find({"item_id": item_id})) == []:
                return {"error": "Item not found"}

            else:
                grocery.delete_one({"item_id": item_id})
                return {"Message": "Item deleted successfully"}

        except Exception as e:
            return {"error": str(e)}

    def update_item(self, item_id: int, item: Grocery):
        try:
            if list(grocery.find({"item_id": item_id})) != []:
                grocery.update_one({"item_id": item_id}, {
                    "$set": item.dict()})
                return {"Message": "It is updated successfully"}

            else:
                return {"error": "Item not found"}

        except Exception as e:
            return {"error": str(e)}

    def fetch(self):
        try:
            items = list(grocery.find({}, {'_id': 0}))
            if items == []:
                return {"Warning:": "there are not items"}
            else:
                return items
        except Exception as e:
            return {"error": str(e)}

    def find_by_id(self, item_id):
        try:
            found_data = list(grocery.find(id, {"_id": False}))
            return found_data
        except Exception as e:
            return {"status": "failed", "error": str(e.args)}

    def find_total(self, agg):
        try:
            total = grocery.aggregate(agg)
            if total == 0:
                return {"Warning:": "there are not items so the total price is zero"}
            else:
                return (list(total))[0]['total']
        except Exception as e:
            return {"error": str(e)}


grocery_object = Grocery_handler()
