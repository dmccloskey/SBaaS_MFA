from SBaaS_base.postgresql_orm_base import *
class data_stage02_isotopomer_tracers(Base):
    __tablename__ = 'data_stage02_isotopomer_tracers'
    id = Column(Integer, Sequence('data_stage02_isotopomer_tracers_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    met_id = Column(String(50)) # e.g glc_DASH_D_e
    met_name = Column(String(100)) # e.g. 1-13C Glucose
    isotopomer_formula = Column(postgresql.ARRAY(String(50))) # e.g. ['[13C]HO','CH2O','CH2O','CH2O','CH2O','CH3O']
    met_elements = Column(postgresql.ARRAY(String(3))) # the elements that are labeled (e.g. C,C,C)
    met_atompositions = Column(postgresql.ARRAY(Integer)) #the atoms positions that are labeled (e.g. 1,2,3) 
    ratio = Column(Float)
    supplier = Column(String(100))
    supplier_reference = Column(String(100))
    purity = Column(Float)
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name_abbreviation','met_id','met_name'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.supplier_reference=data_dict_I['supplier_reference'];
        self.supplier=data_dict_I['supplier'];
        self.sample_name_abbreviation=data_dict_I['sample_name_abbreviation'];
        self.comment_=data_dict_I['comment_'];
        self.ratio=data_dict_I['ratio'];
        self.met_atompositions=data_dict_I['met_atompositions'];
        self.experiment_id=data_dict_I['experiment_id'];
        self.met_elements=data_dict_I['met_elements'];
        self.isotopomer_formula=data_dict_I['isotopomer_formula'];
        self.met_name=data_dict_I['met_name'];
        self.met_id=data_dict_I['met_id'];
        self.purity=data_dict_I['purity'];

    def __set__row__(self,experiment_id_I,
            sample_name_abbreviation_I,
            met_id_I,
            met_name_I,
            isotopomer_formula_I,
            met_elements_I,
            met_atompositions_I,
            ratio_I,
            supplier_I,
            supplier_reference_I,
            purity_I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.met_id=met_id_I
        self.met_name=met_name_I
        self.isotopomer_formula=isotopomer_formula_I
        self.met_elements=met_elements_I
        self.met_atompositions=met_atompositions_I
        self.ratio=ratio_I
        self.supplier=supplier_I
        self.supplier_reference=supplier_reference_I
        self.purity=purity_I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
            'sample_name_abbreviation':self.sample_name_abbreviation,
                'met_id':self.met_id,
                'met_name':self.met_name,
                'isotopomer_formula':self.isotopomer_formula,
                'met_elements':self.met_elements,
                'met_atompositions':self.met_atompositions,
                'ratio':self.ratio,
                'supplier':self.supplier,
                'supplier_reference':self.supplier_reference,
                'purity':self.purity,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())