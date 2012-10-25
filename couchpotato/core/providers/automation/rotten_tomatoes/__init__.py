from .main import RottenTomatoes

def start():
    return RottenTomatoes()

config = [{
    'name': 'rottentomatoes',
    'groups': [
        {
            'tab': 'automation',
            'name': 'rottentomatoes',
            'label': 'Rotten Tomatoes',
            'description': 'Automatically add new DVD releases from <a href="http://rottentomatoes.com">Rotten Tomatoes</a>',
            'options': [
                {
                    'name': 'automation_enabled',
                    'default': False,
                    'type': 'enabler',
                },
                {
                    'name': 'automation_api_key',
                    'label': 'Apikey',
                },
            ],
        },
    ],
}]
