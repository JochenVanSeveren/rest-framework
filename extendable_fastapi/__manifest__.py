# Copyright 2023 ACSONE SA/NV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Extendable Fastapi",
    "summary": """
        Allows the use of extendable into fastapi apps""",
    "version": "17.0.0.0.1",
    "license": "LGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "maintainers": ["lmignon"],
    "website": "https://www.odoo.com",
    "depends": ["fastapi", "extendable"],
    "data": [],
    "demo": [],
    "external_dependencies": {
        "python": [
            "pydantic>=2.0.0",
            "extendable-pydantic>=1.2.0",
        ],
    },
    "installable": False,
}
