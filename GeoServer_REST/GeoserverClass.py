from geo.Geoserver import Geoserver

class GeoServerClass:

    def __init__(self):
        self.server = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')

    def get_layer_names(self, workspace=None):
        """Get list of all layers
        If no workspace is given, it will return list of all layers"""
        layers = self.server.get_layers(workspace)['layers']['layer']

        if workspace is None:
            layer_names = [layer['name'].split(":")[1] for layer in layers]
        else:
            layer_names = [layer['name'] for layer in layers]

        return layer_names

    def get_workspace_names(self):
        "List all workspace names"
        workspaces = self.server.get_workspaces()['workspaces']['workspace']
        return [workspace['name'] for workspace in workspaces]

    def get_style_names(self, workspace=None):
        "Will return styles of default workspace of no workspace is given"
        styles = self.server.get_styles(workspace)['styles']['style']
        return [style['name'] for style in styles]

    def get_datastore_names(self, workspace=None):
        "Returns list of all datastores"
        datastores = self.server.get_datastores(workspace)['dataStores']
        
        if len(datastores) == 0:
            return None
        datastores = datastores['dataStore']

        return [datastore['name'] for datastore in datastores]




