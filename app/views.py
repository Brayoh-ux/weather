from flask import render_template, flash, url_for, redirect, request
from app import app, db
import requests
from app.models import City

@app.route('/', methods = ['GET', 'POST'])
def index():
    
   

    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'

    new_city = request.form.get('city')
    api_key = 'a778d9642410a11ed2cbd17c20c246bc'


    response = requests.get(url.format(new_city, api_key)).json()
    climate = response

    weather_data = []

    if climate:
        weather = {
            'city': new_city,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }

        weather_data.append(weather)


    return render_template('weather.html', weather_data = weather_data)


@app.route('/save', methods = ['GET', 'POST'])
def save():
    
    if request.method == 'POST':
        new_city = request.form.get('city')
        new_city_obj = City(name = new_city)

        if new_city:
            db.session.add(new_city_obj)
            db.session.commit()

    page = request.args.get('page', 1, type=int) 
    cities = City.query.order_by(City.date_posted.desc()).all()
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'


    weather_data = []

    api_key = 'a778d9642410a11ed2cbd17c20c246bc'

    for city in cities:

        r = requests.get(url.format(city.name, api_key)).json()

        weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(weather)

    
    page = request.args.get('page', type=int) 
    places = City.query.order_by(City.date_posted.desc())\
        .paginate(page = page, per_page=3)

    return render_template('save.html', weather_data = weather_data, cities = places)


@app.route('/save/delete_city/<int:city_id>', methods = ['GET', 'POST'])
def delete_city(city_id):
    if request.method == 'POST':
        city = City.query.get_or_404(city_id)
        # if post.author != current_user:
        #     abort(403)
        if city:
            db.session.delete(city)
            db.session.commit()

    flash('City deleted', 'success')
    return redirect( url_for('save'))