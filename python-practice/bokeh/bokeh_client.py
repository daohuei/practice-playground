import random
from bokeh.client import pull_session, push_session
from bokeh.embed import server_session
from bokeh.plotting import figure, ColumnDataSource


doc = None
session_id = None
with pull_session(url="http://localhost:5006/mp4_upload") as session:

    doc = session.document
    source = ColumnDataSource({"x": [], "y": [], "color": []})

    def update():
        new = {
            "x": [random.random()],
            "y": [random.random()],
            "color": [random.choice(["red", "blue", "green"])],
        }
        source.stream(new)

    doc.add_periodic_callback(update, 100)

    fig = figure(
        title="Streaming Circle Plot!",
        sizing_mode="scale_width",
        x_range=[0, 1],
        y_range=[0, 1],
    )
    fig.circle(source=source, x="x", y="y", color="color", size=10)
    print(session.id)
    doc.title = "Now with live updating!"
    doc.add_root(fig)

session = push_session(
    doc, session_id=session_id, url="http://localhost:5006/mp4_upload"
)
session.show()