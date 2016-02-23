# System
import json
# SBaaS
from .stage02_isotopomer_measuredData_query import stage02_isotopomer_measuredData_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage02_isotopomer_measuredData_io(stage02_isotopomer_measuredData_query,
                                            sbaas_template_io):
    def import_data_stage02_isotopomer_measuredFluxes_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_data_stage02_isotopomer_measuredFluxes(data.data);
        data.clear_data();
    def import_data_stage02_isotopomer_measuredFragments_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_data_stage02_isotopomer_measuredFragments(data.data);
        data.clear_data();
    def export_data_stage02_isotopomer_measuredFragments_csv(self,experiment_ids_I,sample_name_abbreviations_I,filename_O,time_points_I=[]):
        """export data_stage02_isotopomer_measuredFragments
        INPUT:
        experiment_ids_I = [] of string, experiment_id
        sample_name_abbreviations_I = [] of string, sample_name_abbreviation
        filename_O = string, filename for export
        time_points_I = [] of strings, time_point"""
        data_O = [];
        for experiment_id in experiment_ids_I:
            for sna in sample_name_abbreviations_I:
                if time_points_I:
                    for tp in time_points_I:
                        data_tmp =[];
                        data_tmp = self.get_row_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage02IsotopomerMeasuredFragments(experiment_id,sna,tp);
                        data_O.extend(data_tmp);
                else:
                    data_tmp =[];
                    data_tmp = self.get_row_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFragments(experiment_id,sna);
                    data_O.extend(data_tmp);
        if data_O:
            io = base_exportData(data_O);
            io.write_dict2csv(filename_O);
    def export_data_stage02_isotopomer_measuredFluxes_csv(self,experiment_ids_I,model_ids_I,sample_name_abbreviations_I,filename_O):
        """export data_stage02_isotopomer_measuredFluxes
        INPUT:
        experiment_ids_I = [] of string, experiment_id
        model_ids_I = [] of strings, model_id
        sample_name_abbreviations_I = [] of string, sample_name_abbreviation
        filename_O = string, filename for export
        """
        data_O = [];
        for experiment_id in experiment_ids_I:
            for model_id in model_ids_I:
                for sna in sample_name_abbreviations_I:
                    data_tmp =[];
                    data_tmp = self.get_rows_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFluxes(experiment_id,model_id,sna);
                    data_O.extend(data_tmp);
        if data_O:
            io = base_exportData(data_O);
            io.write_dict2csv(filename_O);
   