from tests.test_db.expected_data import marked_delete_by_id, expected_updated_result, updated_data, test_data_update, \
    test_create_data, expected_create_result, test_get_user_data_by_id, expected_user_info, \
    test_get_all_users_by_lyostat_id, expected_result_to_delete_all_marked_users, expected_users_to_retriev, lyostat_id
from db.entities.template import Template

Template.creating_unique_field()


def test_create(template_db_collection):
    input_data = test_create_data['test_db_fixtured']['test_create']['input_data']
    user_id = template_db_collection.create(*input_data)
    assert user_id is not None
    response = template_db_collection.get_user_by_id(user_id)
    # expected_data = template_db_collection.get_user_by_id(user_id)
    expected_data = expected_create_result
    assert response['name'] == expected_data['name']
    assert response['lyostat_id'] == expected_data['lyostat_id']
    assert response['cycle_id'] == expected_data['cycle_id']
    assert response['recipe_name'] == expected_data['recipe_name']
    assert response == expected_data


def test_get_user_by_id(template_db_collection):
    input_data = test_get_user_data_by_id['test_db_fixtured']['test_create']['input_data']
    user_id = template_db_collection.create(*input_data)
    retrived_user = template_db_collection.get_user_by_id(user_id)
    expected_data = expected_user_info

    assert user_id is not None
    assert retrived_user['name'] == expected_data['name']
    assert retrived_user['lyostat_id'] == expected_data['lyostat_id']
    assert retrived_user['cycle_id'] == expected_data['cycle_id']
    assert retrived_user['recipe_name'] == expected_data['recipe_name']


def test_get_all_by_lyostat_id(template_db_collection):
    input_data1 = test_get_all_users_by_lyostat_id['test_db_fixtured']['test_create']['input_data1']
    input_data2 = test_get_all_users_by_lyostat_id['test_db_fixtured']['test_create']['input_data2']
    input_data3 = test_get_all_users_by_lyostat_id['test_db_fixtured']['test_create']['input_data3']
    user_id1 = template_db_collection.create(*input_data1)
    user_id2 = template_db_collection.create(*input_data2)
    user_id3 = template_db_collection.create(*input_data3)
    get_all_by_lyo_id = template_db_collection.get_all_by_lyostat_id(lyostat_id['lyostat_id'])

    assert len(get_all_by_lyo_id) is 1

    ids = [str(x['_id']) for x in get_all_by_lyo_id]

    assert (user_id1 in ids) == True
    assert (user_id2 in ids) == True
    assert (user_id3 in ids) == True
#
# def test_update(template_db_collection):
#     input_data = test_data_update['test_db_fixtured']['test_create']['input_data']
#     user_id = template_db_collection.create(*input_data)
#     assert user_id is not None
#     update_all_values = template_db_collection.update(user_id, **updated_data)
#     expected_result = expected_updated_result
#     assert update_all_values == True
#
#     update_document = template_db_collection.get_user_by_id(user_id)
#
#     assert update_document['name'] == expected_result['name']
#     assert update_document['lyostat_id'] == expected_result['lyostat_id']
#     assert update_document['cycle_id'] == expected_result['cycle_id']
#     assert update_document['recipe_name'] == expected_result['recipe_name']


# def test_marked_delete_by_id(template_db_collection):
#     input_data1 = marked_delete_by_id['test_db_fixtured']['test_create']['input_data1']
#     input_data2 = marked_delete_by_id['test_db_fixtured']['test_create']['input_data2']
#     input_data3 = marked_delete_by_id['test_db_fixtured']['test_create']['input_data3']
#     user_id1 = template_db_collection.create(*input_data1)
#     user_id2 = template_db_collection.create(*input_data2)
#     user_id3 = template_db_collection.create(*input_data3)
#
#     assert user_id1 is not None
#     assert user_id2 is not None
#     assert user_id3 is not None
#
#     assert template_db_collection.marked_delete_by_id(user_id1)
#     assert template_db_collection.marked_delete_by_id(user_id2)
#     assert template_db_collection.marked_delete_by_id(user_id3)
#
#     template_db_collection.unmarked_delete_by_id(user_id3)
#     update_document = template_db_collection.get_user_by_id(user_id3)
#
#     expected_updated_result = expected_result_to_delete_all_marked_users
#
#     assert update_document['name'] == expected_updated_result['name']
#     assert update_document['lyostat_id'] == expected_updated_result['lyostat_id']
#     assert update_document['cycle_id'] == expected_updated_result['cycle_id']
#     assert update_document['recipe_name'] == expected_updated_result['recipe_name']
#     template_db_collection.delete_all_scheduled_for_delete()
#
#     updated_document = template_db_collection.get_all()
#     assert updated_document is not None
#
# delete_all_users_from_DB = template_db_collection.delete_all()
# assert delete_all_users_from_DB
