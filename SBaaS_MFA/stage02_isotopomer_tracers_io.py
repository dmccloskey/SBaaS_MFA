# System
import json
# SBaaS
from .stage02_isotopomer_tracers_query import stage02_isotopomer_tracers_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage02_isotopomer_tracers_io(stage02_isotopomer_tracers_query,
                                            sbaas_template_io):
    def import_data_stage02_isotopomer_tracers_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_data_stage02_isotopomer_tracers(data.data);
        data.clear_data();
   