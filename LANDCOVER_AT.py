import gdal
import gpsinfo
gpsinfo.Layer.allowUnsafeSSL(True)
service = gpsinfo.Service('https://raw.githubusercontent.com/maegger/LANDCOVER_AT/master/gpsinfoWMTSCapabilities.xml')
layer = gpsinfo.Layer(service, 'SENTINEL_10M')
print(layer.value('upper_left',404140.4293,382819.6223))

