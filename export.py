import urllib2
import json
import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc
sc.doc = Rhino.RhinoDoc.ActiveDoc

output_folder = "C:\\Users\\81803\\Desktop\\outputFolder\\"
obj_name = "voronoiSphere"
object_file_name = "{}.fbx".format(obj_name)
file_path = output_folder + object_file_name

def compression():
    url = 'http://localhost:3001/api/compression'
    sendValues = {
      'path':output_folder,
      'fileName':obj_name
    }

    sendValuesJson = json.dumps(sendValues).encode("utf8")
    request = urllib2.Request(url,sendValuesJson)
    request.add_header("Content-Type",'application/json')
    request.get_method = lambda: 'POST'
    response = json.load(urllib2.urlopen(request))
    print (response)

if baked != None:
    ids = rs.ObjectsByLayer(layer_name)
    selected_objects = rs.SelectObjects(ids)
    rs.Command("_-SaveAs {} _Enter _Enter".format(file_path))
    rs.UnselectAllObjects()
    compression()
    finish_export = "finish"