from SBaaS_base.postgresql_orm_base import *
class data_stage02_isotopomer_simulation(Base):
    __tablename__ = 'data_stage02_isotopomer_simulation'
    id = Column(Integer, Sequence('data_stage02_isotopomer_simulation_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    mapping_id = Column(String(100))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('experiment_id','model_id','mapping_id','sample_name_abbreviation','time_point'),
            UniqueConstraint('simulation_id'),
            )

    def __init__(self,
            simulation_id_I,
            experiment_id_I,
            model_id_I,mapping_id_I,
            sample_name_abbreviation_I,
            time_point_I,
            used__I,
            comment__I):
        self.simulation_id=simulation_id_I
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.mapping_id=mapping_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
            'simulation_id':self.simulation_id,
            'experiment_id':self.experiment_id,
            'model_id':self.model_id,
            'mapping_id':self.mapping_id,
            'sample_name_abbreviation':self.sample_name_abbreviation,
            'time_point':self.time_point,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

