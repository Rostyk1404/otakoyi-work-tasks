""" Provides class Templates"""
import datetime

from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from db.entities.db_connector import mongoDB_client
from typing import Optional, List


class Template:
    """Provides interface for hashing and sending requests to Mongo database."""

    collection = mongoDB_client.mydatabase["templates"]

    @classmethod
    def creating_unique_field(cls):

        """Current function creating unique constraints for pymongo."""

        return cls.collection.create_index('name', unique=True)

    @classmethod
    def create(cls, name: str, lyostat_id: str, cycle_id: str, recipe_name: str) -> Optional[str]:
        """
         :return: An ObjectId if user was created and None if wasn't.
         #https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/
        """

        try:
            data = {'name': name, 'lyostat_id': lyostat_id, 'cycle_id': cycle_id, 'recipe_name': recipe_name,
                    'created_on': datetime.datetime.now(), 'updated_on': datetime.datetime.now(),
                    'to_be_delete_on': None}
            result = cls.collection.insert_one(data)
            return str(result.inserted_id)
        except DuplicateKeyError:
            return None

    @classmethod
    def get_user_by_name(cls, user_name: str) -> dict:
        return cls.collection.find_one({'name': user_name})

    @classmethod
    def get_user_by_id(cls, user_id: str) -> dict:
        """
        :return:if user exist return dict  if user does not exist return None.
        #https://docs.mongodb.com/manual/reference/method/db.collection.find/index.html
        """

        return cls.collection.find_one({'_id': ObjectId(user_id)})

    @classmethod
    def get_all(cls) -> List[dict]:
        """:return: if user exist return list of dict if user does not exist return an empty list."""
        return list(self.collection.find())

    @classmethod
    def get_all_by_lyostat_id(cls, lyostat_id: str) -> List[dict]:

        """:return: if user exist return list of dict if user does not exist return an empty list."""

        return list(cls.collection.find({"lyostat_id": lyostat_id}))

    @classmethod
    def get_elements_by_datetime_range(cls, start: datetime.datetime, end: datetime.datetime) -> List[dict]:

        """
        :return:if datetime range exist will be returned list of dicts in other case will be returned an empty list.
        """

        start_option = "$gte"
        end_option = "$lte"
        return list(cls.collection.find({'created_on': {start_option: start, end_option: end}}))

    @classmethod
    def update(cls, user_id: str, name: str = None, lyostat_id: str = None, cycle_id: str = None,
               recipe_name: str = None) -> bool:
        """:return:bool True if field was updated and False if wasn't or user does not exist."""

        data = {'name': name,
                'lyostat_id': lyostat_id,
                'cycle_id': cycle_id,
                'recipe_name': recipe_name,
                'updated_on': datetime.datetime.now()
                }

        data = {key: value for key, value in data.items() if value is not None}

        if len(data.keys()) > 1:
            result = cls.collection.update_one({'_id': ObjectId(user_id)}, {"$set": data}, upsert=False)
            return True if result.modified_count > 0 else False
        return False

    def marked_delete_by_id(cls, user_id) -> bool:
        """:return:bool True if user was marked and False if wasn't or user does not exist."""
        result = cls.collection.update_one({'_id': ObjectId(user_id)},
                                           {"$set": {'to_be_delete_on': datetime.datetime.now()}}, upsert=False)
        return True if result.modified_count > 0 else False

    @classmethod
    def unmarked_delete_by_id(cls, user_id) -> bool:
        """:return:bool True if user was unmarked and False if wasn't or user does not exist."""
        result = cls.collection.update_one({'_id': ObjectId(user_id)},
                                           {"$set": {'to_be_delete_on': None}}, upsert=False)
        return True if result.modified_count > 0 else False

    @classmethod
    def delete_all_scheduled_for_delete(cls) -> bool:
        """:return:bool True if user was unmarked and False if wasn't or user does not exist."""
        result = self.collection.delete_many({'to_be_delete_on': {"$lt": datetime.datetime.now()}})
        return True if result.deleted_count else False

    @classmethod
    def delete_all(cls) -> bool:
        """:return:bool True if all user's was deleted and False if they were not or user does not exist."""
        delete = cls.collection.delete_many({})
        return True if delete.deleted_count else False
