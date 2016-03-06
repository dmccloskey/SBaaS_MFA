from SBaaS_base.postgresql_orm_base import *
class data_stage02_isotopomer_fittedExchangeFluxes(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedExchangeFluxes'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedExchangeFluxes_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    #experiment_id = Column(String(50))
    #model_id = Column(String(50))
    #mapping_id = Column(String(100))
    #sample_name_abbreviation = Column(String(100))
    #time_point = Column(String(10))
    rxn_id = Column(String(100))
    flux_exchange = Column(Float);
    flux_exchange_stdev = Column(Float);
    flux_exchange_lb = Column(Float); # based on 95% CI
    flux_exchange_ub = Column(Float);
    flux_exchange_units = Column(String(50));
    flux_exchange_normalized = Column(Float);
    flux_exchange_normalized_stdev = Column(Float);
    flux_exchange_normalized_lb = Column(Float); # based on 95% CI
    flux_exchange_normalized_ub = Column(Float);
    flux_exchange_normalized_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','rxn_id','simulation_dateAndTime','flux_exchange_units'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.flux_exchange_lb=row_dict_I['flux_exchange_lb'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.flux_exchange_normalized_units=row_dict_I['flux_exchange_normalized_units'];
        self.flux_exchange_normalized_ub=row_dict_I['flux_exchange_normalized_ub'];
        self.flux_exchange_normalized_lb=row_dict_I['flux_exchange_normalized_lb'];
        self.flux_exchange_normalized_stdev=row_dict_I['flux_exchange_normalized_stdev'];
        self.flux_exchange_normalized=row_dict_I['flux_exchange_normalized'];
        self.flux_exchange_units=row_dict_I['flux_exchange_units'];
        self.flux_exchange_ub=row_dict_I['flux_exchange_ub'];
        self.flux_exchange_stdev=row_dict_I['flux_exchange_stdev'];
        self.flux_exchange=row_dict_I['flux_exchange'];
        self.rxn_id=row_dict_I['rxn_id'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.simulation_id=row_dict_I['simulation_id'];

    def __set__row__(self,simulation_id_I,
            simulation_dateAndTime_I,
            rxn_id_I,
            flux_exchange_I,
            flux_exchange_stdev_I,
            flux_exchange_lb_I,
            flux_exchange_ub_I,
            flux_exchange_units_I,
            flux_exchange_normalized_I,
            flux_exchange_normalized_stdev_I,
            flux_exchange_normalized_lb_I,
            flux_exchange_normalized_ub_I,
            flux_exchange_normalized_units_I,
            used__I,
            comment__I,):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        self.rxn_id=rxn_id_I
        self.flux_exchange=flux_exchange_I
        self.flux_exchange_stdev=flux_exchange_stdev_I
        self.flux_exchange_lb=flux_exchange_lb_I
        self.flux_exchange_ub=flux_exchange_ub_I
        self.flux_exchange_units=flux_exchange_units_I
        self.flux_exchange_normalized=flux_exchange_normalized_I
        self.flux_exchange_normalized_stdev=flux_exchange_normalized_stdev_I
        self.flux_exchange_normalized_lb=flux_exchange_normalized_lb_I
        self.flux_exchange_normalized_ub=flux_exchange_normalized_ub_I
        self.flux_exchange_normalized_units=flux_exchange_normalized_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
            'simulation_id':self.simulation_id,
            'simulation_dateAndTime':self.simulation_dateAndTime,
            'rxn_id':self.rxn_id,
            'flux_exchange':self.flux_exchange,
            'flux_exchange_stdev':self.flux_exchange_stdev,
            'flux_exchange_lb':self.flux_exchange_lb,
            'flux_exchange_ub':self.flux_exchange_ub,
            'flux_exchange_units':self.flux_exchange_units,
            'flux_exchange_normalized':self.flux_exchange_normalized,
            'flux_exchange_normalized_stdev':self.flux_exchange_normalized_stdev,
            'flux_exchange_normalized_lb':self.flux_exchange_normalized_lb,
            'flux_exchange_normalized_ub':self.flux_exchange_normalized_ub,
            'flux_exchange_normalized_units':self.flux_exchange_normalized_units,
            'used_':self.used_,
            'comment_':self.comment_,}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage02_isotopomer_fittedExchangeFluxStatistics(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedExchangeFluxStatistics'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedExchangeFluxStatistics_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    n_fluxes = Column(Integer)
    n_observableFluxes = Column(Integer)
    total_precision = Column(Float)
    total_observablePrecision = Column(Float)
    relative_nObservableFluxes = Column(Float);
    average_observableFluxPrecision = Column(Float);
    average_fluxPrecision = Column(Float); 
    flux_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','simulation_dateAndTime','flux_units'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.n_observableFluxes=row_dict_I['n_observableFluxes'];
        self.n_fluxes=row_dict_I['n_fluxes'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.simulation_id=row_dict_I['simulation_id'];
        self.average_fluxPrecision=row_dict_I['average_fluxPrecision'];
        self.comment_=row_dict_I['comment_'];
        self.flux_units=row_dict_I['flux_units'];
        self.used_=row_dict_I['used_'];
        self.average_observableFluxPrecision=row_dict_I['average_observableFluxPrecision'];
        self.relative_nObservableFluxes=row_dict_I['relative_nObservableFluxes'];
        self.total_observablePrecision=row_dict_I['total_observablePrecision'];
        self.total_precision=row_dict_I['total_precision'];

    def __set__row__(self,simulation_id_I,
        simulation_dateAndTime_I,
        n_fluxes_I,
        n_observableFluxes_I,
        total_precision_I,
        total_observablePrecision_I,
        relative_nObservableFluxes_I,
        average_observableFluxPrecision_I,
        average_fluxPrecision_I,
        flux_units_I,
        used__I,
        comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        self.n_fluxes=n_fluxes_I
        self.n_observableFluxes=n_observableFluxes_I
        self.total_precision=total_precision_I
        self.total_observablePrecision=total_observablePrecision_I
        self.relative_nObservableFluxes=relative_nObservableFluxes_I
        self.average_observableFluxPrecision=average_observableFluxPrecision_I
        self.average_fluxPrecision=average_fluxPrecision_I
        self.flux_units=flux_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        'n_fluxes':self.n_fluxes,
        'n_observableFluxes':self.n_observableFluxes,
        'total_precision':self.total_precision,
        'total_observablePrecision':self.total_observablePrecision,
        'relative_nObservableFluxes':self.relative_nObservableFluxes,
        'average_observableFluxPrecision':self.average_observableFluxPrecision,
        'average_fluxPrecision':self.average_fluxPrecision,
        'flux_units':self.flux_units,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())