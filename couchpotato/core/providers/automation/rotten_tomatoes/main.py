from couchpotato.core.event import fireEvent
from couchpotato.core.helpers.variable import md5, getImdb
from couchpotato.core.logger import CPLog
from couchpotato.core.providers.automation.base import Automation
from couchpotato.environment import Env
import json

log = CPLog(__name__)


class RottenTomatoes(Automation):

    interval = 86400

    urls = {
        'base': 'http://api.rottentomatoes.com/api/public/v1.0',
        'upcoming': '/lists/dvds/upcoming.json?page_limit=50&apikey=%s',
    }

    def getIMDBids(self):

        if self.isDisabled():
            return

        movies = []
        for movie in self.getMovies('upcoming'):
            name = movie.get('title')
            year = movie.get('year')

            imdb = self.search(name, year)

            if imdb and self.isMinimalMovie(imdb):
                movies.append(imdb['imdb'])

        return movies

    def getMovies(self, list):

        list_url = self.urls['base'] + self.urls[list] % self.conf('automation_api_key')

        return self.call(list_url)

    def call(self, list_url):

        try:
            cache_key = 'rotten_tomatoes.%s' % md5(list_url)
            json_string = self.getCache(cache_key, list_url)

            if json_string:
                return json.loads(json_string).get('movies')

        except:
            log.error('Failed to get data from rotten tomatoes.')

        return []
