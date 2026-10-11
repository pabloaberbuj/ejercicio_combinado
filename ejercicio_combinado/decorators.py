'''
Este es un modulo generado para la funcion anadir_ruido
'''
import functools
from typing import Dict
from numpy.random import choice, random

def anadir_ruido(noise_probability : float, noise_distribution : Dict[str, float]):
    '''
    funcion que añade ruido con una probabilidad definida por noise_probability
    y una distribucion deifnida por noise_distribution
    
    Parametros
    ----------
    noise_probability (float):
        probabilidad de reemplazar un dato por ruido
        
    noise_distribution (Dict[str,float])
        distribucion de rudio
        
    Returns
    -------
    inner_decorator
    
    '''
    def inner_decorator(func):
        '''funcion que genera un decorador interno'''
        possible_noise_values = list(noise_distribution.keys())
        noise_value_probabilities = list(noise_distribution.values())
        @functools.wraps(func)
        def wrapper(*args):
            '''funcion que genera un wrapper'''
            true_value = func(*args)
            if random() <= noise_probability: #ie con prob `noise_probability`
                vals, probs = exclude_true_value(possible_noise_values,
                                                 noise_value_probabilities, true_value)
                return choice(vals, p=probs)
            return true_value
        return wrapper
    return inner_decorator


def exclude_true_value(possible_noise_values, noise_value_probabilities, true_value):
    '''funcion que ecluche un valor verdadero de una lista'''
    try:
        i = possible_noise_values.index(true_value)
        possible_noise_values = possible_noise_values[:i] + possible_noise_values[i+1:]
        noise_value_probabilities = noise_value_probabilities[:i] + noise_value_probabilities[i+1:]
        z = sum(noise_value_probabilities)
        noise_value_probabilities = [x/z for x in noise_value_probabilities]
    except ValueError:
        pass
    return possible_noise_values, noise_value_probabilities

if __name__ == "__main__":
    @anadir_ruido(0.5, {'ups!':0.7, 'UPS!':0.3})
    def funcion_de_ejemplo(x):
        ''' Funcion que devuelve el doble del input'''
        return 2*x
    for y in range(10):
        print(funcion_de_ejemplo(y))
