import os
import pickle



#path_base = os.getcwdb() # выводит адрес, где работает с двумя слэшами вместо одного
#from imp import reload - подхватывает изменения в импортируемом модуле командой reload(script)
from fractions import Fraction


class CTricks:


    def dictionary_from_two_lists(self, list_key,list_value):
        dict_ = dict(zip(list_key, list_value))
        print(dict_)
        return dict_


    def format_euro_float(self,figure):
        x = "{:,.2f}".format(figure)
        return x

    def format_fraction(self,nom,denom):
        x = Fraction(nom,denom)
        return x

    def export_to_pickle(self,object,destination,file):
        path = destination + file
        f_ = open(path,'wb')
        pickle.dump(object,f_)
        f_.close()
        return path

    def import_from_pickle(self,destination,file):
        path = destination + file
        f_ = open(path, 'rb')
        import_object = pickle.load(f_)
        return import_object

    def mysum_universal_for_list_recursion(self,L):
        first, *rest = L
        return first if not rest else first + self.mysum_universal_for_list_recursion(rest)

    #def cross_to_flat(self,dataframe):