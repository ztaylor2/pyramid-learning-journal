def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('detail', '/entry/{id:\d+}')
    config.add_route('create', '/create')
    config.add_route('update', '/update/{id:\d+}')
