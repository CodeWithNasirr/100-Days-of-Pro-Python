# The current population of a town is 10000. The population of the town is
# increasing at the rate of 10% per year. You have to write a program to
# find out the population at the end of each of the last 10 years. For eg
# current population is 10000 so the output should be like this: 10th year 10000
                                                                # 9th year - 9000
                                                                # 8th year - 8100 and so on...

def cal_population_over_year(c_population:int,year:int,rate:float):
    for year in range(year,0,-1):
        print(f"{year}th year - {c_population}")
        c_population = int(c_population /(1 + rate))
if __name__=='__main__':
    c_population=10000
    year=10
    rate=0.10
    cal_population_over_year(c_population,year,rate)                