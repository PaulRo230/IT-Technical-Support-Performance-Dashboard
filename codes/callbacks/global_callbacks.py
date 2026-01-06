from dash import Input, Output

def register_global_callbacks(app):

    @app.callback(
        Output("global-office-store", "data"),
        Input("global-office-filter", "value"),
    )
    def update_global_office(value):
        return value