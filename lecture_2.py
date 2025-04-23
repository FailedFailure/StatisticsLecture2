import math

def s_square(list_to_calculate,number):
    sum_to_calculate = 0.0
    s_square_to_calculate = 0.0
    for i in range(0,number):
        list_to_calculate.append(float(input()))
        sum_to_calculate = sum_to_calculate + list_to_calculate[i]
    average_to_calculate = sum_to_calculate / number
    for i in range(0,number):
        s_square_to_calculate = s_square_to_calculate + (average_to_calculate - list_to_calculate[i]) * (average_to_calculate - list_to_calculate[i]) / number
    s_standard_to_calculate = math.sqrt(s_square_to_calculate)
    print(str(average_to_calculate) + "\n" + str(s_square_to_calculate) + "\n" + str(s_standard_to_calculate))
def covariance_of_two_lists(list_a_to_cal,list_b_to_cal,number):
    sum_a_to_cal = 0.0
    sum_b_to_cal = 0.0
    convariance_to_cal = 0.0
    s_square_a_to_cal = 0.0
    s_square_b_to_cal = 0.0
    for i in range(0,number):
        list_a_to_cal.append(float(input()))
        list_b_to_cal.append(float(input()))
        sum_a_to_cal = sum_a_to_cal + list_a_to_cal[i]
        sum_b_to_cal = sum_b_to_cal + list_b_to_cal[i]
    average_a_to_cal = sum_a_to_cal / number
    average_b_to_cal = sum_b_to_cal / number
    for i in range(0,number):
        s_square_a_to_cal = s_square_a_to_cal + (average_a_to_cal - list_a_to_cal[i]) * (average_a_to_cal - list_a_to_cal[i]) / number
        s_square_b_to_cal = s_square_b_to_cal + (average_b_to_cal - list_b_to_cal[i]) * (average_b_to_cal - list_b_to_cal[i]) / number
        convariance_to_cal = convariance_to_cal + (average_a_to_cal - list_a_to_cal[i]) * (average_b_to_cal - list_b_to_cal[i]) / number
    s_standard_a_to_cal = math.sqrt(s_square_a_to_cal)
    s_standard_b_to_cal = math.sqrt(s_square_b_to_cal)
    relation = convariance_to_cal / (s_standard_a_to_cal * s_standard_b_to_cal)
    print(str(convariance_to_cal) + "\n" + str(relation))

# list_points = []
# s_square(list_points,5)

list_age = []
list_salary = []
covariance_of_two_lists(list_age,list_salary,5)

