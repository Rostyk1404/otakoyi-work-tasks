import pytest
from db.entities.template import Template


@pytest.fixture(scope='function', autouse=False)
def template_db_collection():
    obj = Template()
    # obj.delete_all()
    yield obj
