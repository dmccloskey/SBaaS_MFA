from SBaaS_base.postgresql_orm_base import *
class data_stage02_isotopomer_fittedNetFluxDifferences(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedNetFluxDifferences'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedNetFluxDifferences_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    simulation_id_1 = Column(String(500))
    simulation_dateAndTime_1 = Column(DateTime);
    simulation_id_2 = Column(String(500))
    simulation_dateAndTime_2 = Column(DateTime);
    rxn_id = Column(String(100))
    flux_difference = Column(Float);
    flux_distance = Column(Float);
    significant = Column(Boolean);
    significant_criteria = Column(String(100))
    flux_units = Column(String(50));
    fold_change_geo = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('analysis_id','simulation_id_1','simulation_dateAndTime_1','simulation_id_2','simulation_dateAndTime_2','rxn_id','simulation_dateAndTime_1','flux_units','significant_criteria'),
            )

    def __init__(self,
        analysis_id_I,
        simulation_id_1_I,
        simulation_dateAndTime_1_I,
        simulation_id_2_I,
        simulation_dateAndTime_2_I,
        rxn_id_I,
        flux_difference_I,
        flux_distance_I,
        significant_I,
        significant_criteria_I,
        flux_units_I,
        fold_change_geo_I,
        used__I,
        comment__I):
        self.analysis_id=analysis_id_I
        self.simulation_id_1=simulation_id_1_I
        self.simulation_dateAndTime_1=simulation_dateAndTime_1_I
        self.simulation_id_2=simulation_id_2_I
        self.simulation_dateAndTime_2=simulation_dateAndTime_2_I
        self.rxn_id=rxn_id_I
        self.flux_difference=flux_difference_I
        self.flux_distance=flux_distance_I
        self.significant=significant_I
        self.significant_criteria=significant_criteria_I
        self.flux_units=flux_units_I
        self.fold_change_geo=fold_change_geo_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
        'analysis_id':self.analysis_id,
        'simulation_id_1':self.simulation_id_1,
        'simulation_dateAndTime_1':self.simulation_dateAndTime_1,
        'simulation_id_2':self.simulation_id_2,
        'simulation_dateAndTime_2':self.simulation_dateAndTime_2,
        'rxn_id':self.rxn_id,
        'flux_difference':self.flux_difference,
        'flux_distance':self.flux_distance,
        'significant':self.significant,
        'significant_criteria':self.significant_criteria,
        'flux_units':self.flux_units,
        'fold_change_geo':self.fold_change_geo,
        'used_':self.used_,
        'comment_':self.comment_}