from fastapi import APIRouter
from scripts.core.handlers.grocery_handler import Grocery_handler
from scripts.core.handlers.email_handler import Email
from schemas.model import Grocery
from scripts.core.handlers.email_handler import Email_handler
from scripts.constants.app_constants import EndPoints
# from scripts.constants.aggregation import db_constant_object


item_router = APIRouter()



@item_router.post(EndPoints.adding_item)
def adding_item(item_id: int, item: Grocery):
    try:
        item_object = Grocery_handler()
        final_list = item_object.add_item(item_id, item)
        return final_list
    except Exception as e:
        return {"Error": str(e)}


@item_router.delete(EndPoints.deleting_item)
def deleting_item(item_id: int):
    try:
        item_object = Grocery_handler()
        del_item = item_object.delete_item(item_id)
        return del_item
    except Exception as e:
        return {"Error": str(e)}


@item_router.put(EndPoints.updating_item)
def updating_item(item_id: int, item: Grocery):
    try:
        item_object = Grocery_handler()
        up_item = item_object.update_item(item_id, item)
        return up_item
    except:
        return {"Error"}


@item_router.get(EndPoints.getting_items)
def fetch():
    try:
        item_object = Grocery_handler()
        get_items = item_object.fetch()
        return get_items
    except Exception as e:
        return {"Error": str(e)}


@item_router.get(EndPoints.total_amount)
def total_price():
    try:
        item_handler = Grocery_handler()
        result = item_handler.find_total()
        return result
    except Exception as e:
        return {"Error": str(e)}


@item_router.post(EndPoints.sending_email)
def sending_item(email: Email):
    try:
        item_object = Email_handler()
        send_items = item_object.send_email(email)
        return "Email sent successfully"
    except Exception as e:
        return ({"Error": str(e)})


@item_router.get(EndPoints.fetching_total)
def find_total():
    try:
        item_object = Grocery_handler()
        return item_object.find_total()
    except Exception as e:
        return ({"Error": str(e)})
