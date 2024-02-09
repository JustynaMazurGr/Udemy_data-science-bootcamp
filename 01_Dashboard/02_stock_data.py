#import potrzebnych bibliotek
import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

#Funkcja pobierająca dane
def fetch_financial_data(company='AMZN'):
    """
    This function fetch stock market quotations.
    """
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

#Nieco przygotowujemy nasze dane, czyli zresetujemy indeks i wytniemy dane > 2019-01-01
df = fetch_financial_data()
df.reset_index(inplace=True)
df = df[df.Date > '2019-01-01']

#Dorzucamy zewnętrzne style tak żeby nasza aplikacja nieco ładniej wyglądała
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']   #link do stylu

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Następnie przekazujemy jak ma aplikacja wyglądać
#Czyli tworzymy na początek sekcję html, w tej sekcji podajemy nagłowek H4 'Notowania spółki...'
#Następnie tworzymy komponent graph czyli nasz wykres i w naszym komponencie tworzymy obiekt figure
#przekazujemy parametr data jako go.Scatter (można powiedzieć, żetworzymy wykres punktowy),
#ale ustawiamy parametr fill='tozeroy' czyli pozwoli nam to wypełnić obszar do wartości y-greków,
#więc dostaniemy wykres powierzchniowy.
#Ustawimy także wygląd tego wykresu. Ustawimy oś y na logarytmiczną, wysokość, tytuł, czy pokazać legendę.
#Następnie tworzymy kolejny komponent Graph. Tu będzie wykres słupkowy.
app.layout = html.Div([

    html.H4('Notowania spółki Amazon'),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x=df.Date,
                    y=df.Close,
                    mode='lines',
                    fill='tozeroy',
                    name='Amazon'
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=500,
                title_text='Wykres ceny',
                showlegend=True
            )
        )
    ),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=df.Date,
                    y=df.Volume,
                    name='Wolumen'
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=300,
                title_text='Wykres wolumenu',
                showlegend=True
            )
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)