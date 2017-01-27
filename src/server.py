#!/usr/bin/python
from flask import Flask, Markup, render_template
from pandas import read_csv
from plotly.offline import plot
from plotly.graph_objs import Scatter, Layout, Figure

app = Flask(__name__)

@app.route('/')
def graph():
    graph = read_csv('/usr/src/app/mnt/logging/speedtest.csv')
    ping_trace = Scatter(x=graph['Timestamp'], y=graph['Ping'],
                         mode='lines', name='Ping', yaxis='y2')
    download_trace = Scatter(x=graph['Timestamp'], y=graph['Download'],
                             mode='lines', name='Download')
    upload_trace = Scatter(x=graph['Timestamp'], y=graph['Upload'],
                           mode='lines', name='Upload')
    layout = Layout(title='Internet speed and ping results',
                    plot_bgcolor='rgb(230, 230, 230)',
                    yaxis=dict(title='Speed (bps)'),
                    yaxis2=dict(title='Ping (ms)', overlaying='y',
                    side='right'))
    figure = Figure(data=[ping_trace, download_trace, upload_trace],
                    layout=layout)
    result = plot(figure, output_type='div')
    return render_template('graph.html',
                           graph_placeholder=Markup(result))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
