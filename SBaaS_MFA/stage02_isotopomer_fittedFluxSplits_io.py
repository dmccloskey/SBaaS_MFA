# System
import json
# SBaaS
from .stage02_isotopomer_fittedFluxSplits_query import stage02_isotopomer_fittedFluxSplits_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage02_isotopomer_fittedFluxSplits_io(stage02_isotopomer_fittedFluxSplits_query,
                                            sbaas_template_io):
    def plot_fluxSplits(self,simulation_ids_I = [], split_ids_I = [], plot_by_split_id_I=True, individual_plots_I=True, exclude_I = {}, use_lbubAsErrorBars_I=True):
        '''Plot the flux splits for a given set of simulations and a given set of reactions
        Default: plot the flux precision for each simulation on a single plot for a single reaction'''

        #Input:
        # simulation_ids_I
        # split_ids_I
        # plot_by_split_id_I = if True, simulations will be plotted per split; if false, splitss will be plotted per simulation
        # individual_plots_I = if True, each split/simulation will be plotted per figure; if false, all data will be plotted on a single figure
        # exclude_I = dict, {simulation_id:split_id}, simulations_ids/split_ids to exclude from the plot
        # use_lbubAsErrorBars_I = if True, the lb/ub will be used as error bars; if false, the std_dev will be used as error bars
        # 

        from resources.matplot import matplot
        plot = matplot();

        data_O ={}; # keys = simulation_id, values = {rxn_id:{flux_info}};
        for simulation_id in simulation_ids_I:
            # get the simulation dataAndTime
            simulation_dateAndTimes = [];
            simulation_dateAndTimes = self.get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedFluxSplits(simulation_id);
            data_O[simulation_id] = {};
            if len(simulation_dateAndTimes) > 1:
                print('more than 1 simulation date and time found!')
                continue;
            else:
                simulation_dataAndTime = simulation_dateAndTimes[0];
            # get the split_ids
            if split_ids_I:
                split_ids = split_ids_I;
            else:
                split_ids = [];
                split_ids = self.get_splitIDs_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedFluxSplits(simulation_id,simulation_dataAndTime)
            # get the split information for each simulation
            for split_id in split_ids:
                data_O[simulation_id][split_id] = {}
                if exclude_I and split_id in exclude_I and exclude_I[split_id] == simulation_id:
                    data_O[simulation_id][split_id] = {};
                else:
                    split_rxn_id_O,split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O=[],[],[],[],[],[];
                    split_rxn_id_O,split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O = self.get_split_simulationIDAndSimulationDateAndTimeAndSplitID_dataStage02IsotopomerfittedFluxSplits(simulation_id,simulation_dataAndTime,split_id);
                    # check for None split
                    if not split_O: continue;
                    # save the split information
                    for rxn_id_cnt,rxn_id in enumerate(split_rxn_id_O):
                        data_O[simulation_id][split_id][rxn_id] = {}
                        tmp_O = {};
                        tmp_O = {'split':split_O[rxn_id_cnt],'split_stdev':split_stdev_O[rxn_id_cnt],
                                 'split_lb':split_lb_O[rxn_id_cnt],'split_ub':split_ub_O[rxn_id_cnt],
                                 'split_units':split_units_O[rxn_id_cnt]}
                        data_O[simulation_id][split_id][rxn_id] = tmp_O;
        # reorder the data for plotting
        if plot_by_split_id_I:
            split_ids_all = [];
            for k1,v1 in data_O.items():
                for k in list(v1.keys()):
                    split_ids_all.append(k);
            split_ids = list(set(split_ids_all));
            split_rxn_ids_all = {};
            for split_id in split_ids:
                split_rxn_ids_all[split_id]=[];
            for k1,v1 in data_O.items():
                for k2,v2 in v1.items():
                    for k in list(v2.keys()):
                        split_rxn_ids_all[k2].append(k)
            split_rxn_ids = {};
            for k1,v1 in split_rxn_ids_all.items():
                split_rxn_ids[k1] = list(set(v1));                
            if individual_plots_I:
                for split_id,rxn_ids in split_rxn_ids.items():
                    title_I,xticklabels_I,ylabel_I,xlabel_I,data_I,mean_I,ci_I = '',[],'','',[],[],[];
                    for simulation_id in simulation_ids_I:
                        for rxn_id in rxn_ids:
                            if data_O[simulation_id][split_id] and data_O[simulation_id][split_id][rxn_id]:
                                xticklabels_I.append(simulation_id+'\n'+rxn_id);
                                mean_I.append(data_O[simulation_id][split_id][rxn_id]['split'])
                                if use_lbubAsErrorBars_I:
                                    data_I.append([data_O[simulation_id][split_id][rxn_id]['split_lb'],data_O[simulation_id][split_id][rxn_id]['split_ub'],data_O[simulation_id][split_id][rxn_id]['split']])
                                    ci_I.append([data_O[simulation_id][split_id][rxn_id]['split_lb'],data_O[simulation_id][split_id][rxn_id]['split_ub']])
                                else:
                                    ci_I.append([data_O[simulation_id][split_id][rxn_id]['split']-data_O[simulation_id][split_id][rxn_id]['split_stdev'],data_O[simulation_id][split_id][rxn_id]['split']+data_O[simulation_id][split_id][rxn_id]['split_stdev']])
                                    data_I.append([data_O[simulation_id][split_id][rxn_id]['split']-data_O[simulation_id][split_id][rxn_id]['split_stdev'],data_O[simulation_id][split_id][rxn_id]['split']+data_O[simulation_id][split_id][rxn_id]['split_stdev'],data_O[simulation_id][split_id][rxn_id]['split']])
                                ylabel_I = 'split [' + data_O[simulation_id][split_id][rxn_id]['split_units'] + ']';
                    title_I = split_id;
                    xlabel_I = 'Simulation_id'
                    plot.boxAndWhiskersPlot(title_I,xticklabels_I,ylabel_I,xlabel_I,data_I=data_I,mean_I=mean_I,ci_I=ci_I)
            else:
                title_I,xticklabels_I,ylabel_I,xlabel_I,data_I,mean_I,ci_I = '',[],'','',[],[],[];
                for split_id,rxn_ids in split_rxn_ids.items():
                    for simulation_id in simulation_ids_I:
                        for rxn_id in rxn_ids:
                            if data_O[simulation_id][split_id] and data_O[simulation_id][split_id][rxn_id]:
                                xticklabels_I.append(simulation_id+'\n'+split_id+'\n'+rxn_id);
                                mean_I.append(data_O[simulation_id][split_id][rxn_id]['split'])
                                if use_lbubAsErrorBars_I:
                                    data_I.append([data_O[simulation_id][split_id][rxn_id]['split_lb'],data_O[simulation_id][split_id][rxn_id]['split_ub'],data_O[simulation_id][split_id][rxn_id]['split']])
                                    ci_I.append([data_O[simulation_id][split_id][rxn_id]['split_lb'],data_O[simulation_id][split_id][rxn_id]['split_ub']])
                                else:
                                    ci_I.append([data_O[simulation_id][split_id][rxn_id]['split']-data_O[simulation_id][split_id][rxn_id]['split_stdev'],data_O[simulation_id][split_id][rxn_id]['split']+data_O[simulation_id][split_id][rxn_id]['split_stdev']])
                                    data_I.append([data_O[simulation_id][split_id][rxn_id]['split']-data_O[simulation_id][split_id][rxn_id]['split_stdev'],data_O[simulation_id][split_id][rxn_id]['split']+data_O[simulation_id][split_id][rxn_id]['split_stdev'],data_O[simulation_id][split_id][rxn_id]['split']])
                                ylabel_I = 'split [' + data_O[simulation_id][split_id][rxn_id]['split_units'] + ']';
                title_I = '';
                xlabel_I = 'Simulation_id\nSplit_id\nReaction_id'
                plot.boxAndWhiskersPlot(title_I,xticklabels_I,ylabel_I,xlabel_I,data_I=data_I,mean_I=mean_I,ci_I=ci_I)
        else: 
            return;
   