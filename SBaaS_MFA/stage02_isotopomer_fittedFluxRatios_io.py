# System
import json
# SBaaS
from .stage02_isotopomer_fittedFluxRatios_query import stage02_isotopomer_fittedFluxRatios_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage02_isotopomer_fittedFluxRatios_io(stage02_isotopomer_fittedFluxRatios_query,
                                            sbaas_template_io):
    pass;
   