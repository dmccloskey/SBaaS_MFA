# System
import json
# SBaaS
from .stage02_isotopomer_fittedNetFluxDifferences_query import stage02_isotopomer_fittedNetFluxDifferences_query
from .stage02_isotopomer_analysis_query import stage02_isotopomer_analysis_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
from ddt_python.ddt_container import ddt_container
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage02_isotopomer_fittedNetFluxDifferences_io(stage02_isotopomer_fittedNetFluxDifferences_query,
                                                     stage02_isotopomer_analysis_query,
                                            sbaas_template_io):
    def import_data_stage02_isotopomer_fittedNetFluxDifferences_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_data_stage02_isotopomer_fittedNetFluxDifferences(data.data);
        data.clear_data();

    def import_data_stage02_isotopomer_fittedNetFluxDifferences_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_data_stage02_isotopomer_fittedNetFluxDifferences(data.data);
        data.clear_data();
    def export_dataStage02IsotopomerFittedNetFluxDifferences_js(self,analysis_id_I = None,data_dir_I="tmp"):
        '''Plot the flux differences and fold_change as bar plots for a given analysis
        
        Input:
        analysis_id_I = string
        data_dir_I = output .js file directory and filename
        
        DDT tiles:
        1. filter menu
        2. horizontal bar plot of flux differences
        3. horizontal bar plot of flux fold_change
        4. table
        '''
        
        # get the data
        data_O =[]; 
        flux_data = [];
        flux_data = self.get_rows_analysisID_dataStage02IsotopomerFittedNetFluxDifferences(analysis_id_I);
        # convert dataAndTime to string types
        for i,row in enumerate(flux_data):
            row['simulation_dateAndTime_1'] = self.convert_datetime2string(row['simulation_dateAndTime_1']);
            row['simulation_dateAndTime_2'] = self.convert_datetime2string(row['simulation_dateAndTime_2']);
            #row['flux_units'] = row['flux_units'].replace('*','x');
            if row['significant']: row['significant'] = 'Yes';
            else: row['significant'] = 'No';
            data_O.append(row);
        # dump chart parameters to a js files
        data1_keys = ['simulation_id_1','simulation_dateAndTime_1','simulation_id_2','simulation_dateAndTime_2','rxn_id','flux_units','significant'
                    ];
        data1_nestkeys = ['rxn_id'];
        data1_keymap = {'xdata':'flux_distance',
                        'ydata':'rxn_id',
                        'serieslabel':'simulation_id_2',
                        'featureslabel':'rxn_id'
                        };
        data2_keymap = {'xdata':'fold_change_geo',
                        'ydata':'rxn_id',
                        'serieslabel':'simulation_id_2',
                        'featureslabel':'rxn_id'
                        };
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        # tile 1: form (row 1, col1)
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        # tile 2: vertical bars plot of the flux_difference (row 2, col 1)
        svgparameters1_O = {"svgtype":'horizontalbarschart2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 250, 'bottom': 50, 'left': 50 },
                            "svgwidth":350,"svgheight":900,
                            "svgx1axislabel":"flux_distance","svgy1axislabel":"rxn_id",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters1_O = {'tileheader':'Flux distance','tiletype':'svg','tileid':"tile1",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        svgtileparameters1_O.update(svgparameters1_O);
        # tile 3: vertical bars plot of the flux_difference (row 2, col 2)
        svgparameters2_O = {"svgtype":'horizontalbarschart2d_01',"svgkeymap":[data2_keymap],
                            'svgid':'svg2',
                            "svgmargin":{ 'top': 50, 'right': 250, 'bottom': 50, 'left': 50 },
                            "svgwidth":350,"svgheight":900,
                            "svgx1axislabel":"fold_change","svgy1axislabel":"rxn_id",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters2_O = {'tileheader':'Fold change','tiletype':'svg','tileid':"tile2",'rowid':"row2",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        svgtileparameters2_O.update(svgparameters2_O);
        # tile 4: table of data (row 3, col 1)
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Flux difference','tiletype':'table','tileid':"tile3",'rowid':"row3",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,
                              svgtileparameters1_O,
                              svgtileparameters2_O,
                              tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],
                          "tile1":[0],
                          "tile2":[0],
                          "tile3":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());
   