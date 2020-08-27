import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.NavItem(dbc.NavLink("Page 2", href="/home")),
        dbc.NavItem(dbc.NavLink("Page 3", href="/page1")),
    ],
    brand="Name Bar",
    brand_href="#",
    color="primary",
    dark=True,
)

navbar2 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)

navbar3 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)

navbar4 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.NavItem(dbc.NavLink("Page 2", href="/home")),
        dbc.NavItem(dbc.NavLink("Page 3", href="/page1")),
    ],
    brand="Name Bar",
    brand_href="#",
    color="#1f5f55",
    dark=True,
)

navbar5 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.NavItem(dbc.NavLink("Page 2", href="/home")),
        dbc.NavItem(dbc.NavLink("Page 3", href="/page1")),
    ],
    brand="Name Bar",
    brand_href="#",
    color="#1f5f55",
    dark=False,
)
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        navbar,
        html.Br(),
        navbar2,
        html.Br(),
        navbar3,
        html.Br(),
        navbar4,
        html.Br(),
        navbar5,
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
