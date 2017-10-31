def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/home')
    config.add_route('detail', '/detail')
    config.add_route('create', '/create')
    config.add_route('update', '/update')
