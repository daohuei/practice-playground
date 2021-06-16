from datetime import date

from bokeh.application.handlers import FunctionHandler
from bokeh.models import ColumnDataSource, DataTable, TableColumn, Button
from bokeh.plotting import curdoc
from bokeh.layouts import column

session_id = ["1", "2", "3"]
cpu_usage = [10, 20, 30]
memory_usage = [10, 20, 30]
spawn_time = [date(2014, 3, i + 1) for i in range(1, 4)]
connection_time = [date(2014, 3, i + 1) for i in range(1, 4)]
data = dict(
    session_id=session_id,
    cpu_usage=cpu_usage,
    memory_usage=memory_usage,
    spawn_time=spawn_time,
    connection_time=connection_time,
)
source = ColumnDataSource(data)
button = Button(label="Foo", button_type="success")
columns = [
    TableColumn(field="session_id", title="Session ID"),
    TableColumn(field="cpu_usage", title="CPU Usage"),
    TableColumn(field="memory_usage", title="Memory Usage"),
    TableColumn(field="spawn_time", title="Spawn Time"),
    TableColumn(field="connection_time", title="Connection Time"),
]
data_table = DataTable(
    source=source, columns=columns, width=400, height=280, selectable="checkbox"
)


def modify_doc():
    selected_indices = source.selected.indices
    session_infos = source.data
    for indice in selected_indices:
        print(session_infos["session_id"][indice])


button = Button(label="Shutdown Selected Process", button_type="danger")
button.on_click(modify_doc)

curdoc().add_root(column(data_table, button))