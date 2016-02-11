#LIMS
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *
#SBaaS
from .stage02_isotopomer_fittedFluxRatios_postgresql_models import *

from SBaaS_base.sbaas_base import sbaas_base

class stage02_isotopomer_fittedFluxRatios_query(sbaas_base):
    def initialize_datastage02_isotopomer_fittedFluxRatios(self):
        try:
            data_stage02_isotopomer_fittedFluxRatios.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_datastage02_isotopomer_fittedFluxRatios(self):
        try:
            data_stage02_isotopomer_fittedFluxRatios.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage02_isotopomer_fittedFluxRatios(self,simulation_id_I = None,simulation_dateAndTime_I=None):
        try:
            if simulation_id_I and simulation_dateAndTime_I:
                reset = self.session.query(data_stage02_isotopomer_fittedFluxRatios).filter(
                    data_stage02_isotopomer_fittedFluxRatios.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxRatios.simulation_dateAndTime==self.convert_string2datetime(simulation_dateAndTime_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_fittedFluxRatios).filter(data_stage02_isotopomer_fittedFluxRatios.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);