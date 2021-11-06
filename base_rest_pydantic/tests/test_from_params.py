# Copyright 2021 Wakari SRL
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from typing import Type

import mock

from odoo.exceptions import UserError
from odoo.tests.common import SavepointCase

from pydantic import BaseModel

from .. import restapi


class TestPydantic(SavepointCase):
    def setUp(self):
        super(TestPydantic, self).setUp()

        class Model1(BaseModel):
            name: str
            description: str = None

        self.Model1: BaseModel = Model1

    def _from_params(self, pydantic_cls: Type[BaseModel], params: dict, **kwargs):
        restapi_pydantic = restapi.PydanticModel(pydantic_cls, **kwargs)
        mock_service = mock.Mock()
        mock_service.env = self.env
        return restapi_pydantic.from_params(mock_service, params)

    def test_from_params(self):
        params = {"name": "Instance Name", "description": "Instance Description"}
        instance = self._from_params(self.Model1, params)
        self.assertEqual(instance.name, params["name"])
        self.assertEqual(instance.description, params["description"])

    def test_from_params_missing_optional_field(self):
        params = {"name": "Instance Name"}
        instance = self._from_params(self.Model1, params)
        self.assertEqual(instance.name, params["name"])
        self.assertIsNone(instance.description)

    def test_from_params_missing_required_field(self):
        msg = r"value_error.missing"
        with self.assertRaisesRegex(UserError, msg):
            self._from_params(self.Model1, {"description": "Instance Description"})
