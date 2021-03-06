#!/usr/bin/env python3

from flask_migrate import MigrateCommand
from flask_script import Manager

from opwen_email_client.webapp import app
from opwen_email_client.webapp.management import BabelCommand

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('babel', BabelCommand)

manager.run()
