import dash
#import dash_core_components as dcc  #Tu są dostępne komponenty do budowy aplikacji. Taki kod był w filmie Udemy
from dash import dcc    #Powyższy był przestarzały (wg debugera), ten jest poprawny obecnie
#import dash_html_components as html #Tu są komponenty języka html do budowy aplikacji. Z Udemy
from dash import html   #poprawny obecnie
import plotly.graph_objects as go   #Abyśmy byli w stanie zbudować wykres

#Tworzymy najprostszą aplikację
app = dash.Dash(__name__)   #Tworzymy instancję naszej prostej aplikacji dzięki bibliotece Dash, przekazujemy name

#Aby nadać kształt aplikacji musimy ustawić atrybut layout. Do atrybutu layout podajemy jak nasza aplikacja ma wyglądać.
#Na początek zaczynamy od sekcji języka html. Dzięki zaimportowanemu dash_html_componets możemy utworzyć sekcję Div,
#następnie przekazać parametr children i w tym przekazać kolejne obiekty, które w tej sekcji się znajdą.
#Czyli na razie mamy sekcję języka html i w tej sekcji podamy sobie zwyklły prosty nagłówek.
#I będzie to komponent także biblioteki dash_html_components, będzie to nagłówek h2. Jak ustawimy paramert children
#to będzie tekst, który zostanie wyświetlony w tym nagłówku ('Hello Dash!')

app.layout = html.Div(children=[

    html.H2(children='Hello Dash!'),

    #Z powyższym jest bardzo podstawowa aplikacja wyświetlająca tylko Hello Dash!
    #Poniżej dokładamy komponent do naszej aplikacji -> dodajemy graf
    #Ponieważ cały czas jesteśmy w sekcji Div możemy dodawać te komponenty jako listę
    #Chcemy stworzyć graf więc wykorzystamy dash_core_components i klasę Graph i przekażem konkretne parametry do tej klasy.
    #Jako graf przekazujemy obiekt figure z biblioteki plotly teraz jesteśmy w stanie dodać do tego obiektu figure
    #parametr data i także layout (tak jak budowanie wykresów dzięki bibliotece plotly).
    #Najpierw tworzymy ślad go.Bar czyli to będzie wykres słupkowy, x to konkretne lata, y to konkretne wartości
    #podajemy także nazwę name='lokalnie'.
    #Następnie rozbudowujemy ten nasz obiekt typu figure.
    #Dodamy sobie do tego obiektu kolejny element. Tworzymy kolejny ślad na naszym wykresie, czyli go.Bar i teraz
    #przekazujemy paramentr x z tymi samymi wartościami, paramentr y z innymi wartościami.
    #Skąd name='lokalnie' albo 'online? Chcemy pokazać sprzedaż sklepu stacjonarnie (lokalnie) i sklepu online.

    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[150, 180, 220],
                name='lokalnie'
            ),
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[80, 160, 240],
                name='online'
            )
        ])
    )

])

#Uruchomimy sobie tę aplikację:
#Potrzebujemy warunku:

if __name__== '__main__':       #ten warunek mówi: jeśli bezpośrednio uruchamiamy nasz skrypt
    app.run_server(debug=True)  #to uruchomimy naszą aplikację. Ustawiamy jeszcze parametr debug na wartość logiczną
                                #prawda, tak abyśmy mogli na bieżąco debugować naszą aplikację.
