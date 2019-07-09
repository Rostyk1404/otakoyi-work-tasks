test_create_data = {'test_db_fixtured': {
    'test_create':
        {'input_data': ['Rodon', '4', '2', '44'],

         }}

}


expected_create_result = {'name': 'Rodon',
                          'lyostat_id': '4',
                          'cycle_id': '2',
                          'recipe_name': '44'}

test_get_user_data_by_id = {'test_db_fixtured': {
    'test_create':
        {'input_data': ['Romario', '4', '2', '44']

         }}
}

expected_user_info = {'name': 'Romario',
                      'lyostat_id': '4',
                      'cycle_id': '2',
                      'recipe_name': '44'}

test_get_all_users_by_lyostat_id = {'test_db_fixtured': {
    'test_create':
        {
            'input_data1': ['Ross', '4', '2', '44'],
            'input_data2': ['Roho', '4', '2', '44'],
            'input_data3': ['Rondo', '5', '2', '44']

        }}

}

lyostat_id = {'lyostat_id': '4'}

expected_users_to_retriev = [{'input_data1': {'name': 'Ross',
                                              'lyostat_id': '4',
                                              'cycle_id': '2',
                                              'recipe_name': "44"},
                              'input_data2': {'name': 'Roho',
                                              'lyostat_id': '4',
                                              'cycle_id': '2',
                                              'recipe_name': "44"}}]

test_data_update = {'test_db_fixtured': {
    'test_create':
        {'input_data': ['Super Mario', '4', '2', '44'],

         }}

}
updated_data = {"recipe_name": "plumber"}
expected_updated_result = {'name': 'Super Mario',
                           'lyostat_id': '4',
                           'cycle_id': '2',
                           'recipe_name': "plumber"}

marked_delete_by_id = {'test_db_fixtured': {
    'test_create':
        {
            'input_data1': ['Sviat', '4', '2', '44'],
            'input_data2': ['Ihor', '4', '2', '44'],
            'input_data3': ['Vasia', '5', '2', '44']

        }}

}

expected_result_to_delete_all_marked_users = {'name': 'Vasia',
                                              'lyostat_id': '5',
                                              'cycle_id': '2',
                                              'recipe_name': "44"}
