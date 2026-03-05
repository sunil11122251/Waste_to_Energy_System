from config import WASTE_PER_PERSON

def city_waste_simulation(population):

    waste = population * WASTE_PER_PERSON

    return waste


def waste_growth_prediction(total_waste):

    years = [1,2,3,4,5]

    growth = [total_waste*(1.05**y) for y in years]

    return years,growth