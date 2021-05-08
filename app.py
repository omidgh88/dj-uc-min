import os
import sys

from django.conf import settings
from django.urls import path
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from django.template import RequestContext, Template

settings.configure(
    DEBUG=False,
    ALLOWED_HOSTS=["*"],
    ROOT_URLCONF=__name__,
    SECRET_KEY=os.environ.get("SECRET_KEY", "notreallysecret"),
    TEMPLATES=[{"BACKEND": "django.template.backends.django.DjangoTemplates"}],
    MIDDLEWARE_CLASSES=(
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ),
)


def home(request):
    context = RequestContext(
        request, {"content": "Optional Content"}
    )
    return HttpResponse(MAIN_HTML.render(context))


urlpatterns = [
    path("", home),
]

app = get_wsgi_application()


MAIN_HTML = Template(
    """
<html>
  <head>
    <title>The Company</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
     *{
       margin: 0;
       padding: 0;
       box-sizing: border-box;
     }
     html,body{
       display: grid;
       height: 100%;
       width: 100%;
       place-items: center;
     }
     .wrapper{
       color: #3d3a2c;
       max-width: 900px;
       text-align: center;
       padding: 0 50px;
     }
    </style>
  </head>
  <body>
    <div class="wrapper">
      <h1>The Company is under construction</h1>
      <br>
      <h3>Contact via hi@thecompany.com <h3>
    </div>
  </body>
</html>
"""
)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
