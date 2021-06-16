from datetime import date
from random import randint
from bokeh.plotting import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import ColumnDataSource, CustomJS, CheckboxGroup, Button
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn


data = dict(
    dates=[date(2014, 3, i + 1) for i in range(10)],
    downloads=[randint(0, 100) for i in range(10)],
)
source = ColumnDataSource(data)

columns = [
    TableColumn(field="dates", title="Date", formatter=DateFormatter()),
    TableColumn(field="downloads", title="Downloads"),
]

data_table = DataTable(
    source=source, columns=columns, width=400, height=280, selectable=True
)
checkbox = CheckboxGroup(labels=[str(i) for i in data["dates"]])
button = Button(label="Log")

source_code = """
var inds = cb_obj.selected['1d'].indices;

checkbox.active = inds;

checkbox.change.emit()
"""

checkbox_code = """
source.selected['1d'].indices = cb_obj.active;
"""

button_code = """
console.log('checkbox',checkbox.active);
console.log('source',source.selected['1d'].indices);
"""

source.js_event_callbacks = CustomJS(args=dict(checkbox=checkbox), code=source_code)

checkbox.js_event_callbacks = CustomJS(
    args=dict(table=data_table, source=source), code=checkbox_code
)

button.js_event_callbacks = CustomJS(
    args=dict(table=data_table, checkbox=checkbox, source=source), code=button_code
)

curdoc.add_root(widgetbox(data_table, checkbox, button))
