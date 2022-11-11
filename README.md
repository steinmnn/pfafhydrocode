# pfafhydrocode
Holds a python module to decode the hydrological [Pfafstetter Coding System](https://en.wikipedia.org/wiki/Pfafstetter_Coding_System).

The _pfafhydrocode.py_ file contains the functions `upstream` and `downstream` 
help to identify watersheds or affected areas of river manipulations.

With the optional parameter `oddOrZero=True` the modified version of the Pfaffstetter code 
used in the [HydroBASINS dataset](https://www.hydrosheds.org/products/hydrobasins) can be decoded as well.

The examples on the HydroBASNINS dataset from the _examples.py_ are illustrated in the QGIS project file _examples_qgis_illu.qgz_.

The module is an analogue of the R-package [HydroCode](https://cran.r-project.org/web/packages/HydroCode/index.html).
