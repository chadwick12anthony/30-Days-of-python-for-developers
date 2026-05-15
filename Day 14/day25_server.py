#gunicorn

def template_one(template_name = "index.html"):
    return "<h1>What do you know ?</h1>"

def app(environ, start_response):
    for i,k in environ.items():
        print(i,k)
    #data = "Hello world!"
    data = template_one()
    data = data.encode("utf-8")
    start_response = (
        f"200 ok", [
            # ("content-type", "text/plain"),
            ("content-type", "text/html"),
            ("content-Length", str(len(data)))
        ]
    )
    return iter([data])
