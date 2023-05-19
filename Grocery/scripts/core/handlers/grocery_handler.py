from schemas.model import Grocery
from scripts.core.db.mongo.interns_b2_23.mongo_q import grocery
from scripts.utility.mongo_utility import grocery_object
from scripts.constants.aggregation import DatabaseConstants


class Grocery_handler:

    def read_item(self):
        return {"Welcome to Grocery"}

    def fetch(self):
        try:
            all_items = grocery_object.fetch()
            if all_items == []:
                return {"status": "Success", "Message": "No items found"}
            return all_items
        except Exception as e:
            return {"status": "failed", "error": str(e.args)}

    def add_item(self, item_id: int, item: Grocery):
        try:
            if list(grocery_object.find_by_id({"id": item_id})) != []:
                return {"status": "failed", "error": "item already exist"}
            return grocery_object.add_item(item)
        except Exception as e:
            return {"status": "failed", "error": str(e.args)}

    def update_item(self, item_id: int, item: Grocery):
        try:
            if grocery_object.find_by_id({"id": item_id}) == []:
                return {"status": "failed", "error": "item does not exist"}
            # return item_object.update(item_id, item)
            return grocery_object.update_item(item_id, item)
        except Exception as e:
            return {"status": "failed", "error": str(e.args)}

    def delete_item(self, item_id: int):
        try:
            if grocery_object.find_by_id({"id": item_id}) == []:
                return {"status": "failed", "error": "item does not exist"}
            return grocery_object.delete_item(item_id)
        except Exception as e:
            return {"status": "failed", "error": str(e.args)}

    def find_total(self):
        try:
            db_constant_object = DatabaseConstants()
            total = grocery_object.find_total(db_constant_object.aggregate)
            return total
        except Exception as e:
            return {"status": "failed", "error": str(e.args)}



