from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from utils import makeprediction

app = Flask(__name__)
api = Api(app)

class Forecast(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('lat', type=float,
                 help='slength cannot be converted')
        parser.add_argument('lon', type=float,
                 help='swidth cannot be converted')
        args = parser.parse_args()

        forecast = makeprediction.weatherforecast([
                args['lat],
                args['lon']
            ])

        return {
                'lat': args['lat'],
                'lon': args['lon']
               }

api.add_resource(Forecast, '/forecast')

if __name__ == '__main__':
    app.run(debug=False)