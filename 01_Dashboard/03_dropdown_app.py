#Aplikacja interaktywna - Użytkownik będzie mógł określić pewien wybór w aplikacji co chce zobaczyć
#Zbudujemy ją w oparciu o komponent dropdown czyli tzw. lista rozwijana

#import biblioteki
import dash
#from dash import dcc       #było na Udemy
#from dash import html      #było na Udemy
import plotly.graph_objects as go
#from dash.dependencies import Input, Output    #było na Udemy
from dash import Dash, dcc, html, Input, Output, callback   #Z powyższym cosik nie działało. Znalazłam lepsze i działające rozwiązanie na: https://dash.plotly.com/basic-callbacks

#Ładujemy zewnętrzne style
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Tworzymy instancję aplikacji
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Tworzymy układ naszej aplikacji. Tworzymy sekcję html,
#następnie dodajemy ten dropdown, podajemy tym razem id naszego dropdownu bo będziemy chcieli go powiązać
#z naszym wyborem użytkownika i podajemy opcje do wyboru -> do wyboru będą 2 opcje: Polska albo Niemcy,
#Podajemy sobie label czyli to co zostanie wyświetlone użytkownikowi oraz wartość jaką pod spodem będzie aplikacja
#przechowywać po wyborze, i domyślnie ustawimy sobie wartość value na Pl czy na wybór Polski.
#Następnie dodajemy komponent Graph i w tym komponencie przekażemy tylko paramentr id, nic innego, nie przekazujemy
#obiektu figure bo on będzie zależny od tego jaki wybór dokonał użytkownik.

app.layout = html.Div([

    html.H4('Interaktywna aplikacja z listą rozwijaną'),
    html.H5('tego i powyższego tytułu na Udemy nie było, dodałam sobie, a co ;)'),

    dcc.Dropdown(
        id='drop-1',
        options=[
            {'label': 'Polska', 'value': 'PL'},
            {'label': 'Niemcy', 'value': 'GER'}
        ],
        value='PL'
    ),

    dcc.Graph(
        id='graph-1'
    )
])

#To co powyżej będzie zwrócone zostanie uzupełnione przez funkcję update_graph

#Dodajemy do naszej funkcji dekorator app.collback, czyli wywołanie zwrotne, które dzięki temu
#wyborowi, którego dokona użytkownik ten callback bierze nasz input czyli naszą wartość,
#którą użytkownik zaznaczył oraz outputem będzie obiekt figure, który zostanie utworzony przez naszą funkcję
#update_graph i zwrócony do obiektu o tym id czyli dokładnie do naszego grafu.
#Na Udemy było @app.callback i tak nie działało, zmieniłam na @callback, wcześniej importując callback z dash i teraz dopiero działa.
@callback(
    Output('graph-1', 'figure'),
    [Input('drop-1', 'value')]
)

#Tworzymy funkcę update_graph, która przyjmuje parametr value (jest to ta wartość, która użytkownik wybierze,
#i w zależności od tego parametru (my sobie go pomocniczo wyprintujemy żęby zobaczyć także jak on wygląda
#i utworzymy sobie dane, które zostaną wyświetlone i będzie wyświetlony wykres typu scatter, i będzie on wykresem
#powierzchniowym (wypełniamy go poprzez fill: 'tozeroy')
def update_graph(value):
    print(value)
    data_dict = {
        'PL': [3, 2, 5, 4, 7, 2, 4],
        'GER': [4, 1, 3, 4, 2, 4, 1]
    }
    return {'data': [
        {'y': data_dict[value],
         'type': 'scatter',
         'fill': 'tozeroy'}
    ]}


if __name__ == '__main__':
    app.run_server(debug=True)