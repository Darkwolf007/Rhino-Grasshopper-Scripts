import rhinoscriptsyntax as rs

allLayers = rs.LayerNames()

for layer in allLayers:
    layer_c = rs.LayerColor(layer)
    layer_m = rs.LayerMaterialIndex(layer)
    if layer_m == -1:
        layer_m = rs.AddMaterialToLayer(layer)
    rs.MaterialColor(layer_m, layer_c)
    rs.LayerPrintColor(layer, layer_c)