from config import *

def energy_analysis(waste):

    energy_results = {}
    total_energy = 0

    for w in waste:

        energy = waste[w] * ENERGY_FACTOR[w]
        energy_results[w] = energy
        total_energy += energy

    return energy_results,total_energy


def co2_reduction(total_energy):

    return total_energy * 0.7


def revenue(total_energy):

    return total_energy * ELECTRICITY_PRICE


def heat_recovery(total_energy):

    return total_energy * 0.4


def energy_ranking(energy_results):

    return sorted(energy_results.items(),
                  key=lambda x:x[1],
                  reverse=True)