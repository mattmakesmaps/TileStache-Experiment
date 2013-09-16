__author__ = 'matt'
__date__ = '9/15/13'

import TileStache
import ModestMaps

config = {
  "cache": {
    "name": "Disk",
    "path": "."
  },
  "layers": {
    "osm_layer": {
      "provider": {
        "name": "proxy",
        "url": "http://tile.openstreetmap.org/{Z}/{X}/{Y}.png"
      }
    },
    "mbtiles_layer": {
      "provider": {
        "name": "mbtiles",
        "tileset": "data/mbtiles/open-streets-dc.mbtiles"
      }
    },
    "composite": {
      "provider": {
        "class": "TileStache.Goodies.Providers.Composite:Provider",
        "kwargs": {
          "stack": [
              {"src": "osm_layer", "zoom": "0-9"},
              {"src": "mbtiles_layer", "zoom": "10-18"}
          ]
        }
      }
    }
  }
}

# http://localhost:8080/mbtiles_layer/14/4688/6267.png
coord = ModestMaps.Core.Coordinate(6267,4688,14)
config = TileStache.Config.buildConfiguration(config)
type, bytes = TileStache.getTile(config.layers['mbtiles_layer'], coord, 'png', ignore_cached=True)

open('tile.png', 'w').write(bytes)
