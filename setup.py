from distutils.core import setup
setup(
  name = 'django-webpack-loader',
  packages = ['webpack_loader', 'webpack_loader/templatetags'], # this must be the same as the name above
  version = '0.0.1',
  description = 'Load your webpack bundles and chunks in django',
  author = 'Owais Lone',
  author_email = 'hello@owaislone.org',
  url = 'https://github.com/owais/django-webpack-loader', # use the URL to the github repo
  keywords = ['django', 'webpack', 'assets'], # arbitrary keywords
  classifiers = [],
)
