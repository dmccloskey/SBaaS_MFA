#SBaaS
from .stage02_isotopomer_fittedExchangeFluxes_io import stage02_isotopomer_fittedExchangeFluxes_io
from .stage02_isotopomer_fittedNetFluxes_query import stage02_isotopomer_fittedNetFluxes_query
from .stage02_isotopomer_fittedData_query import stage02_isotopomer_fittedData_query
#Resources
from genomeScale_MFA.MFA_methods import MFA_methods
from genomeScale_MFA.MFA_netRxns import isotopomer_netRxns

class stage02_isotopomer_fittedExchangeFluxes_execute(stage02_isotopomer_fittedExchangeFluxes_io,
                                                      stage02_isotopomer_fittedData_query,
                                                      stage02_isotopomer_fittedNetFluxes_query):
    def execute_makeExchangeFluxes(self, simulation_id_I,simulation_dateAndTimes_I=[],normalize_rxn_id_I=None,convert_netRxn2IndividualRxns_I=False,
                              calculate_fluxStdevFromLBAndUB_I=True,calculate_fluxAverageFromLBAndUB_I=True,substitute_zeroFluxForNone_I=True,
                              lower_bound_I=None,upper_bound_I=None):
        '''Determine the exchange flux of reversible reactions
        INPUT:
        normalize_rxn_id_I = rxn_id to normalize all fluxes to
        conver_netRxn2IndividualRxns_I = break apart lumped reactions into individual reactions
        calculate_fluxStdevFromLBAndUB_I = substitute the calculated standard deviation with the lb/ub as follows:
                            (flux_ub_I - flux_lb_I)/4
        calculate_fluxAverageFromLBAndUB_I = calculate the flux average from the mean of the lb/ub
        substitute_zeroFluxForNone_I = substitute 0.0 for None
        lower_bound_I = lower bound for the reaction flux
        upper_bound_I = upper bound for the reaction flux'''
        mfamethods = MFA_methods();
        isotopomernetRxns = isotopomer_netRxns();
        data_O = [];
        # simulation_dateAndTime
        if simulation_dateAndTimes_I:
            simulation_dateAndTimes = [self.convert_string2datetime(x) for x in simulation_dateAndTimes_I];
        else:
            simulation_dateAndTimes = [];
            simulation_dateAndTimes = self.get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedFluxes(simulation_id_I);
        for simulation_dateAndTime in simulation_dateAndTimes:
            # get all reactions included in the simulation (in alphabetical order)
            rxns = [];
            rxns = self.get_rxnIDs_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedFluxes(simulation_id_I,simulation_dateAndTime)
            # group into forward and reverse reactions
            rxns_pairs = {};
            rxn_pair = [];
            for rxn_cnt,rxn in enumerate(rxns):
                #if rxn == 'ValSYN':
                #    print('check');
                if not rxn_pair:
                    rxn_pair.append(rxn);
                else:
                    if '_reverse' in rxn and rxn_pair[0] in rxn:
                        rxn_pair.append(rxn);
                        rxns_pairs[rxn_pair[0]]=rxn_pair;
                        rxn_pair = [];
                    elif '_reverse' in rxn_pair[0]:
                        rxn_pair.insert(0,None);
                        rxn_name = rxn_pair[1].replace('_reverse','');
                        rxns_pairs[rxn_name]=rxn_pair;
                        rxn_pair = [];
                        rxn_pair.append(rxn);
                        if rxn_cnt == len(rxns)-1:
                            #final rxn
                            rxn_pair.insert(0,None);
                            rxn_name = rxn_pair[1].replace('_reverse','');
                            rxns_pairs[rxn_name]=rxn_pair;
                            rxn_pair = [];
                    else:
                        rxn_pair.append(None);
                        rxns_pairs[rxn_pair[0]]=rxn_pair;
                        rxn_pair = [];
                        rxn_pair.append(rxn);
                        if rxn_cnt == len(rxns)-1:
                            #final rxn
                            rxn_pair.append(None);
                            rxns_pairs[rxn_pair[0]]=rxn_pair;
                            rxn_pair = [];
            # query the maximum and minimum flux:
            if not lower_bound_I is None or not upper_bound_I is None:
                min_flux,max_flux=lower_bound_I,upper_bound_I;
            else:
                min_flux,max_flux=None,None
                min_flux,max_flux = self.get_fluxMinAndMax_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedFluxes(simulation_id_I,simulation_dateAndTime);
            # query the normalized rxn flux
            if normalize_rxn_id_I: 
                flux_average_norm,flux_stdev_norm,flux_lb_norm,flux_ub_norm,flux_units_norm = None,None,None,None,None;
                flux_average_norm,flux_stdev_norm,flux_lb_norm,flux_ub_norm,flux_units_norm = self.get_flux_simulationIDAndSimulationDateAndTimeAndRxnID_dataStage02IsotopomerfittedFluxes(simulation_id_I,simulation_dateAndTime,normalize_rxn_id_I);
                min_flux = min_flux/flux_average_norm
                max_flux = max_flux/flux_average_norm
                # check if the sign switched
                if max_flux < min_flux:
                    min_flux_tmp = min_flux;
                    max_flux_tmp = min_flux;
                    max_flux = min_flux_tmp
                    min_flux = max_flux_tmp
            # calculate the net reaction flux average, stdev, lb and ub
            unique_rxn_ids = []; #add only unique rxn_ids
            for k,v in rxns_pairs.items():
                flux_average_1 = 0.0
                flux_average_2 = 0.0
                flux_average_net = 0.0
                flux_stdev_1 = 0.0
                flux_stdev_2 = 0.0
                flux_stdev_net = 0.0
                flux_lb_1 = 0.0
                flux_lb_2 = 0.0
                flux_lb_net = 0.0
                flux_ub_1 = 0.0
                flux_ub_2 = 0.0
                flux_ub_net = 0.0
                flux_units_1 = ''
                flux_units_2 = ''
                flux_units_net = ''
                # get the flux data
                if v[0]:
                    flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1 = self.get_flux_simulationIDAndSimulationDateAndTimeAndRxnID_dataStage02IsotopomerfittedFluxes(simulation_id_I,simulation_dateAndTime,v[0]);
                if v[1]:
                    flux_average_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2 = self.get_flux_simulationIDAndSimulationDateAndTimeAndRxnID_dataStage02IsotopomerfittedFluxes(simulation_id_I,simulation_dateAndTime,v[1]);
                # determine if the fluxes are observable
                observable_1 = mfamethods.check_observableFlux(flux_average_1,flux_lb_1,flux_ub_1)
                observable_2 = mfamethods.check_observableFlux(flux_average_2,flux_lb_2,flux_ub_2)
                # normalize the flux to normalize_rxn_id_I if there was a flux
                if normalize_rxn_id_I:
                    if flux_units_1!='':
                        flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1=mfamethods.normalize_flux(normalize_rxn_id_I,flux_average_norm,flux_stdev_norm,flux_lb_norm,flux_ub_norm,flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1);
                    if flux_units_2!='':
                        flux_average_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2=mfamethods.normalize_flux(normalize_rxn_id_I,flux_average_norm,flux_stdev_norm,flux_lb_norm,flux_ub_norm,flux_average_2,flux_stdev_2,flux_lb_2,flux_ub_2);
                # get the net flux
                if flux_units_1!='':
                    flux_average_net,flux_stdev_net,flux_lb_net,flux_ub_net,flux_units_net = self.get_flux_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndRxnID_dataStage02IsotopomerfittedNetFluxes(
                        simulation_id_I,simulation_dateAndTime,flux_units_1,k);
                elif flux_units_2!='':
                    flux_average_net,flux_stdev_net,flux_lb_net,flux_ub_net,flux_units_net = self.get_flux_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndRxnID_dataStage02IsotopomerfittedNetFluxes(
                        simulation_id_I,simulation_dateAndTime,flux_units_2,k);
                ## calculate the net flux
                #if k=='SUCOAS':
                #    print 'check';
                flux_average,flux_stdev,flux_lb,flux_ub,flux_units,\
                    flux_normalized_average,flux_normalized_stdev,flux_normalized_lb,flux_normalized_ub,flux_normalized_units = mfamethods.calculate_exchangeFlux(
                    flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                    flux_average_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2,
                    flux_average_net,flux_stdev_net,flux_lb_net,flux_ub_net,flux_units_net,
                    min_flux,max_flux)
                # correct the flux stdev
                if calculate_fluxStdevFromLBAndUB_I: 
                    flux_stdev = mfamethods.calculate_fluxStdevFromLBAndUB(flux_lb,flux_ub);
                    #default = true for flux_normalized
                if calculate_fluxAverageFromLBAndUB_I: 
                    flux_average = mfamethods.calculate_fluxAverageFromLBAndUB(flux_average,flux_lb,flux_ub);
                    #default = true for flux_normalized
                if substitute_zeroFluxForNone_I: 
                    flux_average = mfamethods.substitute_zeroFluxForNone(flux_average);
                    flux_normalized_average = mfamethods.substitute_zeroFluxForNone(flux_normalized_average);
                # record net reaction flux
                if convert_netRxn2IndividualRxns_I:
                    rxns_O,fluxes_O,fluxes_stdev_O,fluxes_lb_O,fluxes_ub_O,fluxes_units_O = isotopomernetRxns.convert_netRxn2IndividualRxns(k,flux_average,flux_stdev,flux_lb,flux_ub,flux_units);
                    rxns_normalized_O,fluxes_normalized_O,fluxes_normalized_stdev_O,fluxes_normalized_lb_O,fluxes_normalized_ub_O,fluxes_normalized_units_O = isotopomernetRxns.convert_netRxn2IndividualRxns(k,flux_normalized_average,flux_normalized_stdev,flux_normalized_lb,flux_normalized_ub,flux_normalized_units);
                    if fluxes_O:
                        for i,flux in enumerate(fluxes_O):
                            if not rxns_O[i] in unique_rxn_ids:
                                unique_rxn_ids.append(rxns_O[i]);
                                data_O.append({'simulation_id':simulation_id_I,
                                    'simulation_dateAndTime':simulation_dateAndTime,
                                    'rxn_id':rxns_O[i],
                                    'flux_exchange':fluxes_O[i],
                                    'flux_exchange_stdev':fluxes_stdev_O[i],
                                    'flux_exchange_lb':fluxes_lb_O[i],
                                    'flux_exchange_ub':fluxes_ub_O[i],
                                    'flux_exchange_units':fluxes_units_O[i],
                                    'flux_exchange_normalized':fluxes_normalized_O[i],
                                    'flux_exchange_normalized_stdev':fluxes_normalized_stdev_O[i],
                                    'flux_exchange_normalized_lb':fluxes_normalized_lb_O[i],
                                    'flux_exchange_normalized_ub':fluxes_normalized_ub_O[i],
                                    'flux_exchange_normalized_units':fluxes_normalized_units_O[i],
                                    'used_':True,
                                    'comment_':None})
                    else:
                        if not k in unique_rxn_ids:
                            unique_rxn_ids.append(k);
                            data_O.append({'simulation_id':simulation_id_I,
                                    'simulation_dateAndTime':simulation_dateAndTime,
                                    'rxn_id':k,
                                    'flux_exchange':flux_average,
                                    'flux_exchange_stdev':flux_stdev,
                                    'flux_exchange_lb':flux_lb,
                                    'flux_exchange_ub':flux_ub,
                                    'flux_exchange_units':flux_units,
                                    'flux_exchange_normalized':flux_normalized_average,
                                    'flux_exchange_normalized_stdev':flux_normalized_stdev,
                                    'flux_exchange_normalized_lb':flux_normalized_lb,
                                    'flux_exchange_normalized_ub':flux_normalized_ub,
                                    'flux_exchange_normalized_units':flux_normalized_units,
                                    'used_':True,
                                    'comment_':None})
                else:
                    data_O.append({'simulation_id':simulation_id_I,
                                'simulation_dateAndTime':simulation_dateAndTime,
                                'rxn_id':k,
                                'flux_exchange':flux_average,
                                'flux_exchange_stdev':flux_stdev,
                                'flux_exchange_lb':flux_lb,
                                'flux_exchange_ub':flux_ub,
                                'flux_exchange_units':flux_units,
                                'flux_exchange_normalized':flux_normalized_average,
                                'flux_exchange_normalized_stdev':flux_normalized_stdev,
                                'flux_exchange_normalized_lb':flux_normalized_lb,
                                'flux_exchange_normalized_ub':flux_normalized_ub,
                                'flux_exchange_normalized_units':flux_normalized_units,
                                'used_':True,
                                'comment_':None})

        # add data to the database:
        self.add_data_stage02_isotopomer_fittedExchangeFluxes(data_O);
    def execute_calculateExchangeFluxStatistics(self,simulation_id_I,simulation_dateAndTimes_I=[],flux_units_I=[],rxn_ids_I=[]):
        '''Calculate:
        1. # of unresolved fluxes per total # of reactions
        2. average flux precision per resolved flux'''
        
        mfamethods = MFA_methods();
        data_O = [];
        print('calculating fit statistics...')
        # simulation_dateAndTime
        if simulation_dateAndTimes_I:
            simulation_dateAndTimes = [self.convert_string2datetime(x) for x in simulation_dateAndTimes_I];
        else:
            simulation_dateAndTimes = [];
            simulation_dateAndTimes = self.get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedFluxes(simulation_id_I);
        for simulation_dateAndTime in simulation_dateAndTimes:
            print('calculating flux ratios for simulation_dataAndTime ' + str(simulation_dateAndTime))
            # get all flux_units
            if flux_units_I:
                flux_units = flux_units_I;
            else:
                flux_units = [];
                flux_units = self.get_fluxUnits_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedExchangeFluxes(simulation_id_I,simulation_dateAndTime)
            for flux_unit_cnt,flux_unit in enumerate(flux_units):
                print('calculating fit statistics for flux_units ' + str(flux_unit))
                # get the net fluxes
                flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=[],[],[],[],[];
                if rxn_ids_I:
                    for rxn_id in rxn_ids_I:
                        flux_average_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2 = self.get_flux_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndRxnID_dataStage02IsotopomerfittedExchangeFluxes(simulation_id_I,simulation_dateAndTime,flux_unit,rxn_id);
                        flux_O.append(flux_average_2);
                        flux_stdev_O.append(flux_stdev_2);
                        flux_lb_O.append(flux_lb_2);
                        flux_ub_O.append(flux_ub_2);
                        flux_units_O.append(flux_units_2);     
                else:           
                    flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=self.get_fluxes_simulationIDAndSimulationDateAndTimeAndFluxUnits_dataStage02IsotopomerfittedExchangeFluxes(simulation_id_I,simulation_dateAndTime,flux_unit);
                total_fluxes,observable_fluxes,relative_nObservableFluxes = mfamethods.calculate_relativeNObservableFluxes(flux_O,flux_lb_O,flux_ub_O);
                average_fluxPrecision,average_observable_fluxPrecision = mfamethods.calculate_averageFluxPrecision(flux_O,flux_stdev_O,flux_lb_O,flux_ub_O);
                total_fluxPrecision,total_observable_fluxPrecision = mfamethods.calculate_totalFluxPrecision(flux_O,flux_stdev_O,flux_lb_O,flux_ub_O);
                tmp = {};
                tmp['simulation_id'] = simulation_id_I;
                tmp['simulation_dateAndTime'] = simulation_dateAndTime;
                tmp['n_fluxes'] = total_fluxes
                tmp['n_observableFluxes'] = observable_fluxes
                tmp['total_precision'] = total_fluxPrecision
                tmp['total_observablePrecision'] = total_observable_fluxPrecision
                tmp['relative_nObservableFluxes']= relative_nObservableFluxes;
                tmp['average_observableFluxPrecision'] = average_observable_fluxPrecision;
                tmp['average_fluxPrecision'] = average_fluxPrecision
                tmp['flux_units'] = flux_unit;
                tmp['used_'] = True;
                tmp['comment_'] = None;
                data_O.append(tmp);
        self.add_data_stage02_isotopomer_fittedExchangeFluxStatistics(data_O);