from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
import subprocess
from subprocess import PIPE, Popen
import shutil

URL_MODEL = 'http://ml-private-ip/classify-bottle/'

@view_config(
    route_name='home',
    renderer='templates/home.jinja2'
)
def home(request):
    return {}


@view_config(
    route_name='make_preidction',
    renderer='json'
)
def make_preidction(request):
    # Get and save file
    input_file = request.POST['filename'].file

    with open('./temp_file.jpg', 'wb') as output_file:
        shutil.copyfileobj(input_file, output_file)

    # Make request to ML server
    url_request = ['curl', '-X', 'POST',
                    URL_MODEL,
                    '-H', 'accept: application/json',
                    '-H', 'Content-Type: multipart/form-data',
                    '-F', 'file=@temp_file.jpg;type=image/jpeg']

    pipe = Popen(url_request, stdout=PIPE)
    text = pipe.communicate()[0]
    
    
    return {"Out" : str(text)[3:-2]}


if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_static_view(name='static', path='static')

        config.add_route('home', '/')
        config.add_route('make_preidction', '/make_preidction')
        
        config.scan()

        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()