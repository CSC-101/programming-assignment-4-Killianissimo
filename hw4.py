import sys
import build_data
import hw3
import county_demographics

counties = build_data.get_data()

try:
    with open(sys.argv[1]) as file:
        lines = file.read().splitlines()
        splitlines = []
        print("{} records loaded".format(len(counties)))
        for i in range(len(lines)):
            if ":" or "." in lines[i]:
                temp = lines[i].replace(":", "&")
                temp2 = temp.replace(".", "&")
                splitlines.append(temp2.split("&"))
            #print(splitlines[i])
            if "population-total" == splitlines[i][0]:
                print("2014 Population: {}".format((hw3.population_total(counties))))
            if "population" == splitlines[i][0]:
                if splitlines[i][1] == "Education":
                    try:
                        print("2014 {} population: {}".format(splitlines[i][1],
                                hw3.population_by_education(counties, splitlines[i][2])))
                    except ValueError as e:
                        print(e)
                if splitlines[i][1] == "Ethnicities":
                    try:
                        print("2014 {} population: {}".format(splitlines[i][1],
                                hw3.population_by_ethnicity(counties, splitlines[i][2])))
                    except ValueError as e:
                        print(e)
                if splitlines[i][1] == "Income":
                    try:
                        print("2014 {} population: {}".format(splitlines[i][1],
                                hw3.population_below_poverty_line(counties, splitlines[i][2])))
                    except ValueError as e:
                        print(e)
            if "percent" == splitlines[i][0]:
                if splitlines[i][1] == "Education":
                    try:
                        print("2014 {} population: {}".format(splitlines[i][1],
                                hw3.percent_by_education(counties, splitlines[i][2])))
                    except ValueError as e:
                        print(e)
                if splitlines[i][1] == "Ethnicities":
                    try:
                        print("2014 {} population: {}".format(splitlines[i][1],
                            hw3.percent_by_ethnicity(counties, splitlines[i][2])))
                    except ValueError as e:
                        print(e)
                if splitlines[i][1] == "Income":
                    try:
                        print("2014 {} population: {}".format(splitlines[i][1],
                            hw3.percent_below_poverty_line(counties, splitlines[i][2])))
                    except ValueError as e:
                        print(e)
            if "filter-state" == splitlines[i][0]:
                try:
                    print("Filter: state == {}: {}".format(splitlines[i][1],
                            hw3.filter_by_state(counties, splitlines[i][1])))
                except ValueError as e:
                    print(e)
            if "filter-lt" == splitlines[i][0]:
                if splitlines[i][1] == "Education":
                    if splitlines[i][2] == "High School or Higher":
                        try:
                            filteredCounties = ["filter-lt", "Education", splitlines[i][2], splitlines[i][3], hw3.education_less_than(counties,
                                                    splitlines[i][2], float(splitlines[i][3]))]
                        except ValueError as e:
                            print(e)
            if "filter-gt" == splitlines[i][0]:
                if splitlines[i][1] == "Education":
                    if splitlines[i][2] == "Bachelor's Degree or Higher":
                        try:
                            filteredCounties = ["filter-gt", "Education", splitlines[i][2], splitlines[i][3], hw3.education_greater_than(counties,
                                                    splitlines[i][2], float(splitlines[i][3]))]
                        except ValueError as e:
                            print(e)
            if "display" == splitlines[i][0]:
                try:
                    print("Filter: {}.{} {} {}".format(filteredCounties[1],
                                                filteredCounties[2], filteredCounties[0], filteredCounties[3]))
                    for i in range(len(filteredCounties)):
                       print(filteredCounties[4][i])
                except IndexError as e:
                    print(e)


                        


except FileNotFoundError as e:
    print(e)
