# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import json
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from pyfiglet import Figlet


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))


f = Figlet(font='slant')
print(f.renderText('tyder'))
print('Hello, welcome to tyder!')
print('Lets set-up your backup process')

old_questions = [
    {
        'type': 'confirm',
        'name': 'toBeDelivered',
        'message': 'Is this for delivery?',
        'default': False
    },
    {
        'type': 'input',
        'name': 'phone',
        'message': 'What\'s your phone number?',
    },
    {
        'type': 'list',
        'name': 'size',
        'message': 'What size do you need?',
        'choices': ['Large', 'Medium', 'Small'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'input',
        'name': 'quantity',
        'message': 'How many do you need?',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'expand',
        'name': 'toppings',
        'message': 'What about the toppings?',
        'choices': [
            {
                'key': 'p',
                'name': 'Pepperoni and cheese',
                'value': 'PepperoniCheese'
            },
            {
                'key': 'a',
                'name': 'All dressed',
                'value': 'alldressed'
            },
            {
                'key': 'w',
                'name': 'Hawaiian',
                'value': 'hawaiian'
            }
        ]
    },
    {
        'type': 'rawlist',
        'name': 'beverage',
        'message': 'You also get a free 2L beverage',
        'choices': ['Pepsi', '7up', 'Coke']
    },
    {
        'type': 'input',
        'name': 'comments',
        'message': 'Any comments on your purchase experience?',
        'default': 'Nope, all good!'
    },
    {
        'type': 'list',
        'name': 'prize',
        'message': 'For leaving a comment, you get a freebie',
        'choices': ['cake', 'fries'],
        'when': lambda answers: answers['comments'] != 'Nope, all good!'
    },
    {
        'type': 'input',
        'name': 'backup_file',
        'message': 'Full path of the file to be backed up'
    }
]

questions = [
    {'type': 'input', 'name': 'project',
     'message': 'Whats your project name'},
    {'type': 'input', 'name': 'backup_file',
     'message': 'Full path of the file to be backed up'},
    {'type': 'list', 'name': 'path_type',
     'message': 'Is it a file or a directory',
     'choices': ['file', 'directory']},
    {'type': 'input', 'name': 'dropbox_token',
     'message': 'Insert your dropbox token'},
]

answers = prompt(questions, style=style)
with open("settings.py", "w") as dict_file:
    dict_file.write('set_file = ')
    json.dump(answers, dict_file)
print('Everything configured!')
print('Run "python backup.py" to start backing up!')
