# System
import json
# SBaaS
from .stage02_isotopomer_fittedExchangeFluxes_query import stage02_isotopomer_fittedExchangeFluxes_query
from .stage02_isotopomer_analysis_query import stage02_isotopomer_analysis_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from genomeScale_MFA.MFA_methods import MFA_methods
from SBaaS_models.models_escherMaps_query import models_escherMaps_query
import numpy

class stage02_isotopomer_fittedExchangeFluxes_io(stage02_isotopomer_fittedExchangeFluxes_query,
                                            stage02_isotopomer_analysis_query,
                                            models_escherMaps_query):
    def plot_fluxPrecision(self,simulation_ids_I = [], rxn_ids_I = [], plot_by_rxn_id_I=True, individual_plots_I=True, exclude_I = {}, use_lbubAsErrorBars_I=True):
        '''Plot the flux precision for a given set of simulations and a given set of reactions
        Default: plot the flux precision for each simulation on a single plot for a single reaction'''

        #Input:
        # simulation_ids_I
        # rxn_ids_I
        # plot_by_rxn_id_I = if True, simulations will be plotted per reaction; if false, reactions will be plotted per simulation
        # individual_plots_I = if True, each reaction/simulation will be plotted per figure; if false, all data will be plotted on a single figure
        # exclude_I = dict, {simulation_id:rxn_id}, simulations_ids/rxn_ids to exclude from the plot
        # use_lbubAsErrorBars_I = if True, the lb/ub will be used as error bars; if false, the std_dev will be used as error bars
        # 

        from resources.matplot import matplot
        plot = matplot();

        data_O ={}; # keys = simulation_id, values = {rxn_id:{flux_info}};
        for simulation_id in simulation_ids_I:
            # get the simulation dataAndTime
            simulation_dateAndTimes = [];
            simulation_dateAndTimes = self.get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedExchangeFluxes(simulation_id);
            data_O[simulation_id] = {};
            if len(simulation_dateAndTimes) > 1:
                print('more than 1 simulation date and time found!')
                continue;
            else:
                simulation_dataAndTime = simulation_dateAndTimes[0];
            # get the rxn_ids
            if rxn_ids_I:
                rxn_ids = rxn_ids_I;
            else:
                rxn_ids = [];
                rxn_ids = self.get_rxnIDs_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedExchangeFluxes(simulation_id,simulation_dataAndTime)
            # get the flux information for each simulation
            for rxn_id in rxn_ids:
                data_O[simulation_id][rxn_id] = {}
                if exclude_I and rxn_id in exclude_I and exclude_I[rxn_id] == simulation_id:
                    data_O[simulation_id][rxn_id] = {};
                else:
                    flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=0.0,0.0,0.0,0.0,'';
                    flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O = self.get_flux_simulationIDAndSimulationDateAndTimeAndRxnID_dataStage02IsotopomerfittedExchangeFluxes(simulation_id,simulation_dataAndTime,rxn_id);
                    # check for None flux
                    if not flux_O: flux_O = 0.0;
                    # save the flux information
                    tmp_O = {};
                    tmp_O = {'flux':flux_O,'flux_stdev':flux_stdev_O,'flux_lb':flux_lb_O,
                             'flux_ub':flux_ub_O,'flux_units':flux_units_O}
                    data_O[simulation_id][rxn_id] = tmp_O;
        # reorder the data for plotting
        if plot_by_rxn_id_I:
            rxn_ids_all = [];
            for k1,v1 in data_O.items():
                for k in list(v1.keys()):
                    rxn_ids_all.append(k);
            rxn_ids = list(set(rxn_ids_all));
            if individual_plots_I:
                for rxn_id in rxn_ids:
                    title_I,xticklabels_I,ylabel_I,xlabel_I,data_I,mean_I,ci_I = '',[],'','',[],[],[];
                    for simulation_id in simulation_ids_I:
                        if data_O[simulation_id][rxn_id]:
                            xticklabels_I.append(simulation_id);
                            mean_I.append(data_O[simulation_id][rxn_id]['flux'])
                            if use_lbubAsErrorBars_I:
                                ci_I.append([data_O[simulation_id][rxn_id]['flux_lb'],data_O[simulation_id][rxn_id]['flux_ub']])
                                data_I.append([data_O[simulation_id][rxn_id]['flux_lb'],data_O[simulation_id][rxn_id]['flux_ub'],data_O[simulation_id][rxn_id]['flux']])
                            else:
                                ci_I.append([data_O[simulation_id][rxn_id]['flux']-data_O[simulation_id][rxn_id]['flux_stdev'],data_O[simulation_id][rxn_id]['flux']+data_O[simulation_id][rxn_id]['flux_stdev']])
                                data_I.append([data_O[simulation_id][rxn_id]['flux']-data_O[simulation_id][rxn_id]['flux_stdev'],data_O[simulation_id][rxn_id]['flux']+data_O[simulation_id][rxn_id]['flux_stdev'],data_O[simulation_id][rxn_id]['flux']])
                            ylabel_I = 'Flux [' + data_O[simulation_id][rxn_id]['flux_units'] + ']';
                    title_I = rxn_id;
                    xlabel_I = 'Simulation_id'
                    plot.boxAndWhiskersPlot(title_I,xticklabels_I,ylabel_I,xlabel_I,data_I=data_I,mean_I=mean_I,ci_I=ci_I)
            else:
                title_I,xticklabels_I,ylabel_I,xlabel_I,data_I,mean_I,ci_I = '',[],'','',[],[],[];
                for rxn_id in rxn_ids:
                    for simulation_id in simulation_ids_I:
                        if data_O[simulation_id][rxn_id]:
                            xticklabels_I.append(simulation_id+'\n'+rxn_id);
                            mean_I.append(data_O[simulation_id][rxn_id]['flux'])
                            if use_lbubAsErrorBars_I:
                                ci_I.append([data_O[simulation_id][rxn_id]['flux_lb'],data_O[simulation_id][rxn_id]['flux_ub']])
                                data_I.append([data_O[simulation_id][rxn_id]['flux_lb'],data_O[simulation_id][rxn_id]['flux_ub'],data_O[simulation_id][rxn_id]['flux']])
                            else:
                                ci_I.append([data_O[simulation_id][rxn_id]['flux']-data_O[simulation_id][rxn_id]['flux_stdev'],data_O[simulation_id][rxn_id]['flux']+data_O[simulation_id][rxn_id]['flux_stdev']])
                                data_I.append([data_O[simulation_id][rxn_id]['flux']-data_O[simulation_id][rxn_id]['flux_stdev'],data_O[simulation_id][rxn_id]['flux']+data_O[simulation_id][rxn_id]['flux_stdev'],data_O[simulation_id][rxn_id]['flux']])
                            ylabel_I = 'Flux [' + data_O[simulation_id][rxn_id]['flux_units'] + ']';
                title_I = '';
                xlabel_I = 'Simulation_id/Reaction_id'
                plot.boxAndWhiskersPlot(title_I,xticklabels_I,ylabel_I,xlabel_I,data_I=data_I,mean_I=mean_I,ci_I=ci_I)
        else: 
            return;
    def export_dataStage02IsotopomerFittedExchangeFluxes_js(self,analysis_id_I = None,
                        simulation_ids_I = [],
                        bullet_chart_I = True,
                        data_dir_I="tmp"):
        '''Plot the flux precision for a given set of simulations and a given set of reactions
        Input:
        analysis_id_I = string, analysis id
        Optional Input:
        simulation_ids_I = [] of strings, simulation_ids in a specific order
        bullet_chart_I = True: show the flux estimation +/- StDev
                         False: show the 95% confidence invervals and flux estimation +/- StDev
        '''
        MFAmethods = MFA_methods();
        #Input:
        # analysis_id_I or
        # simulation_ids_I

        if simulation_ids_I:
            simulation_ids = simulation_ids_I;
        else:
            simulation_ids = [];
            simulation_ids = self.get_simulationID_analysisID_dataStage02IsotopomerAnalysis(analysis_id_I);
        data_O =[]; 
        for simulation_id in simulation_ids:
            # get the flux information for each simulation
            flux_data = [];
            flux_data = self.get_rows_simulationID_dataStage02IsotopomerfittedExchangeFluxes(simulation_id);
            #min_flux,max_flux = None,None;
            #min_flux,max_flux = self.get_fluxMinAndMax_simulationID_dataStage02IsotopomerfittedExchangeFluxes(simulation_id)
            for i,row in enumerate(flux_data):
                observable = MFAmethods.check_observableExchangeFlux(row['flux'],row['flux_lb'],row['flux_ub']);
                if not row['flux'] is None:
                    row['simulation_dateAndTime'] = self.convert_datetime2string(row['simulation_dateAndTime']);
                    row['flux_units'] = row['flux_units'].replace('*','x');
                    row['flux_lb_stdev'] = row['flux'] - row['flux_stdev'];
                    row['flux_ub_stdev'] = row['flux'] + row['flux_stdev'];
                    row['flux_mean'] = numpy.mean([row['flux_lb'],row['flux_ub']]);
                    if observable: row['observable'] = 'Yes';
                    else: row['observable'] = 'No';
                    data_O.append(row);
                #if not row['flux'] is None and observable:
                #    row['simulation_dateAndTime'] = self.convert_datetime2string(row['simulation_dateAndTime']);
                #    row['flux_units'] = row['flux_units'].replace('*','x');
                #    row['flux_lb_stdev'] = row['flux'] - row['flux_stdev'];
                #    row['flux_ub_stdev'] = row['flux'] + row['flux_stdev'];
                #    row['flux_mean'] = numpy.mean([row['flux_lb'],row['flux_ub']]);
                #    data_O.append(row);
                #elif not row['flux'] is None and not observable: 
                #    row['simulation_dateAndTime'] = self.convert_datetime2string(row['simulation_dateAndTime']);
                #    row['flux_units'] = row['flux_units'].replace('*','x');
                #    row['flux_lb'] = None;
                #    row['flux_ub'] = None;
                #    row['flux_mean'] = None;
                #    data_O.append(row);
                #elif row['flux']==0.0 and observable:
                #    row['simulation_dateAndTime'] = self.convert_datetime2string(row['simulation_dateAndTime']);
                #    row['flux_units'] = row['flux_units'].replace('*','x');
                #    row['flux_lb_stdev'] = 0.0;
                #    row['flux_ub_stdev'] = 0.0;
                #    row['flux_mean'] = numpy.mean([row['flux_lb'],row['flux_ub']]);
                #    data_O.append(row);
                #elif row['flux']==0.0 and not observable:
                #    row['simulation_dateAndTime'] = self.convert_datetime2string(row['simulation_dateAndTime']);
                #    row['flux_units'] = row['flux_units'].replace('*','x');
                #    row['flux_lb'] = None;
                #    row['flux_ub'] = None;
                #    #row['flux_mean'] = None;
                #    row['flux_lb_stdev'] = None;
                #    row['flux_ub_stdev'] = None;
                #    row['flux']=None;
                #    data_O.append(row);
                elif row['flux']==0.0:
                    row['simulation_dateAndTime'] = self.convert_datetime2string(row['simulation_dateAndTime']);
                    row['flux_units'] = row['flux_units'].replace('*','x');
                    row['flux_lb_stdev'] = 0.0;
                    row['flux_ub_stdev'] = 0.0;
                    row['flux_mean'] = numpy.mean([row['flux_lb'],row['flux_ub']]);
                    if observable: row['observable'] = 'Yes';
                    else: row['observable'] = 'No';
                    data_O.append(row);
        # dump chart parameters to a js files
        data1_keys = ['simulation_id','rxn_id','simulation_dateAndTime','flux_units','observable'
                    ];
        data1_nestkeys = ['rxn_id'];
        if bullet_chart_I:
            data1_keymap = {'xdata':'rxn_id',
                        'ydata':'flux',
                        'ydatalb':'flux_lb_stdev',
                        'ydataub':'flux_ub_stdev',
                        'serieslabel':'simulation_id',
                        'featureslabel':'rxn_id'};
        else:
            data1_keymap = {'xdata':'rxn_id',
                        #'ydata':'flux',
                        'ydata':'flux_mean',
                        'ydatalb':'flux_lb',
                        'ydataub':'flux_ub',
                        #'ydatamin':'min',
                        #'ydatamax':'max',
                        'ydataiq1':'flux_lb_stdev',
                        'ydataiq3':'flux_ub_stdev',
                        'ydatamedian':'flux',
                        'serieslabel':'simulation_id',
                        'featureslabel':'rxn_id'};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 350, 'bottom': 50, 'left': 50 },
                            "svgwidth":750,"svgheight":350,
                            "svgx1axislabel":"rxn_id","svgy1axislabel":"flux",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Flux precision','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Flux precision','tiletype':'table','tileid':"tile3",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0],"tile3":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage02_isotopomer_fittedExchangeFluxes' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
    def export_dataStage02IsotopomerFluxMap_js(self,analysis_id_I,simulation_id_I = None,data_dir_I="tmp"):
        '''Export flux map for viewing'''
        
        MFAmethods = MFA_methods();
        # Get the simulation information
        if simulation_id_I:
            simulation_id = simulation_id_I;
        else:
            simulation_ids = [];
            simulation_ids = self.get_simulationID_analysisID_dataStage02IsotopomerAnalysis(analysis_id_I);
        if not simulation_ids:
            print('No simulation found for the analysis_id ' + analysis_id_I);
        elif len(simulation_ids)>1:
            print('More than 1 simulation found for the analysis_id ' + analysis_id_I);
            simulation_id_I = simulation_ids[0];
        else:
            simulation_id_I = simulation_ids[0];
        # Get the flux information
        flux = [];
        flux_tmp = [];
        #flux = self.get_rowsEscherFluxList_simulationID_dataStage02IsotopomerfittedExchangeFluxes(simulation_id_I);
        flux_tmp = self.get_rows_simulationID_dataStage02IsotopomerfittedExchangeFluxes(simulation_id_I);
        for i,row in enumerate(flux_tmp):
            observable = MFAmethods.check_observableExchangeFlux(row['flux'],row['flux_lb'],row['flux_ub']);
            if not row['flux'] is None and row['flux']!=0.0 and numpy.abs(row['flux']) < 10.0:
                flux_tmp[i]['simulation_dateAndTime'] = self.convert_datetime2string(row['simulation_dateAndTime']);
                flux_tmp[i]['flux_units'] = self.remove_jsRegularExpressions(row['flux_units']);
                if observable: flux_tmp[i]['observable'] = 'Yes';
                else: flux_tmp[i]['observable'] = 'No';
                flux.append(flux_tmp[i]);
            elif row['flux']==0.0 and numpy.abs(numpy.mean([row['flux_lb'],row['flux_ub']]))<10.0:
                flux_tmp[i]['simulation_dateAndTime'] = self.convert_datetime2string(row['simulation_dateAndTime']);
                flux_tmp[i]['flux_units'] = self.remove_jsRegularExpressions(row['flux_units']);
                #flux_tmp[i]['flux'] = numpy.mean([row['flux_lb'],row['flux_ub']]);
                if observable: flux_tmp[i]['observable'] = 'Yes';
                else: flux_tmp[i]['observable'] = 'No';
                flux.append(flux_tmp[i]);

        # Get the map information
        map = [];
        map = self.get_rows_modelID_modelsEschermaps('iJO1366');
        # dump chart parameters to a js files
        data1_keys = ['simulation_id','rxn_id','simulation_dateAndTime','flux_units','observable'
                    ];
        data1_nestkeys = ['simulation_id'];
        data1_keymap = {'values':'flux','key':'rxn_id'};
        data2_keys = ['model_id','eschermap_id'
                    ];
        data2_nestkeys = ['model_id'];
        data2_keymap = {'data':'eschermap_json'};
        # make the data object
        dataobject_O = [{"data":flux,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":map,"datakeys":data2_keys,"datanestkeys":data2_nestkeys}];
        # make the tile parameter objects
        formtileparameters1_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        formparameters1_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters1_O.update(formparameters1_O);
        formtileparameters2_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        formparameters2_O = {'htmlid':'filtermenuform2',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit2','text':'submit'},"formresetbuttonidtext":{'id':'reset2','text':'reset'},"formupdatebuttonidtext":{'id':'update2','text':'update'}};
        formtileparameters2_O.update(formparameters2_O);
        htmlparameters_O = {"htmlkeymap":[data1_keymap,data2_keymap],
                        'htmltype':'escher_01','htmlid':'html1',
                        'escherdataindex':{"reactiondata":0,"mapdata":1},
                        'escherembeddedcss':None,
                        'escheroptions':None};
        htmltileparameters_O = {'tileheader':'Escher map','tiletype':'html','tileid':"tile1",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        htmltileparameters_O.update(htmlparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Flux precision','tiletype':'table','tileid':"tile2",'rowid':"row3",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters1_O,formtileparameters2_O,htmltileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"filtermenu2":[1],"tile1":[0,1],"tile2":[0]};
        filtermenuobject_O = [{"filtermenuid":"filtermenu1","filtermenuhtmlid":"filtermenuform1",
                "filtermenusubmitbuttonid":"submit1","filtermenuresetbuttonid":"reset1",
                "filtermenuupdatebuttonid":"update1"},{"filtermenuid":"filtermenu2","filtermenuhtmlid":"filtermenuform2",
                "filtermenusubmitbuttonid":"submit2","filtermenuresetbuttonid":"reset2",
                "filtermenuupdatebuttonid":"update2"}];
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        filtermenu_str = 'var ' + 'filtermenu' + ' = ' + json.dumps(filtermenuobject_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage02_isotopomer_fittedExchangeFluxes' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str + '\n' + filtermenu_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
            file.write(filtermenu_str);
    def export_data_stage02_isotopomer_fittedExchangeFluxes_csv(self,simulation_ids_I,filename_O):
        """export data_stage02_isotopomer_fittedExchangeFluxes
        INPUT:
        simulation_id_I = [] of string, simulation_id
        filename_O = string, filename for export"""
        data_O = [];
        for simulation_id in simulation_ids_I:
            data_tmp =[];
            data_tmp = self.get_rows_simulationID_dataStage02IsotopomerfittedExchangeFluxes(simulation_id);
            data_O.extend(data_tmp);
        if data_O:
            io = base_exportData(data_O);
            io.write_dict2csv(filename_O);
    def export_data_stage02_isotopomer_fittedExchangeFluxStatistics_csv(self,simulation_ids_I,filename_O,flux_units_I=[]):
        """export data_stage02_isotopomer_fittedExchangeFluxStatistics
        INPUT:
        simulation_id_I = [] of string, simulation_id
        filename_O = string, filename for export"""
        data_O = [];
        for simulation_id in simulation_ids_I:
            if flux_units_I:
                for flux_units in flux_units_I:
                    data_tmp =[];
                    data_tmp = self.get_rows_simulationIDAndFluxUnits_dataStage02IsotopomerFittedExchangeFluxStatistics(simulation_id,flux_units);
                    data_O.extend(data_tmp);
            else:
                data_tmp =[];
                data_tmp = self.get_rows_simulationID_dataStage02IsotopomerFittedExchangeFluxStatistics(simulation_id);
                data_O.extend(data_tmp);
        if data_O:
            io = base_exportData(data_O);
            io.write_dict2csv(filename_O);
   