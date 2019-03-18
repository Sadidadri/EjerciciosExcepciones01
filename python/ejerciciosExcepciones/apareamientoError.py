'''
Created on 18 mar. 2019
Error que se lanza cuando no se pueden aparear 2 gatos
@author: d18momoa
'''
class apareamientoError(Exception):
    def __init__(self):  # define método constructor ...   
        Exception.__init__(self)  # … de excepción ... 
        print("No pueden aparearse dos gatos de mismo sexo.")