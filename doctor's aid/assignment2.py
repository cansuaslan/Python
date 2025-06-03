#create_list will be used in the create() function and it will contain the patient infos.
create_list = []
#create() gets rid of words before the "create" word. It converts the input file to a list.
def create():
    patient_infos = line[7:len(line)].split(", ")
    create_list.append(patient_infos)
    return "Patient {} is recorded.\n".format(patient_infos[0])
#calculate_prob() function calculates people's possibility to have the cancer risk.
# It will be called in the recommendation() and probability() function.
def calculate_prob(i):
    numerator = float(create_list[i][3][:2])
    constant = 100
    population = float(create_list[i][3][3:])
    possibility = float(create_list[i][1])
    denominator = ((1 - possibility) * population) + numerator
    result = (numerator * constant) / denominator
    print(result)
    return result
#It checks whether the names in the input file are same with the create list or not.
# Then calls calculate_prob() function to calculate asked person's risk.
def probability():
    line_probability = line[12:-1]
    for patients in range(len(create_list)):
        if line_probability in create_list[patients]:
            prob_float = float(calculate_prob(patients))
            prob_rounded = str(format(prob_float,"g"))
            prob_meaningful = prob_rounded[:5] + "%"
            return "Patient {} has a probability of {} of having {}.\n".format(create_list[patients][0],
                                                                               prob_meaningful,create_list[patients][2])

    return "Probability for {} cannot be calculated due to absence.\n".format(line_probability)
#It checks whether the names in the input file are same with the create list or not.
# If it is same then calls calculate_prob() function.
# According to the result of function it gives outputs.
def recommendation():
    line_recommendation = line[15:-1]
    for patient in range(len(create_list)):
        if line_recommendation in create_list[patient]:
            calculate_prob(patient)
            ratio = 100 * float(create_list[patient][5][:-1])
            if calculate_prob(patient) >= ratio :
                return "System suggests {} to have the treatment.\n".format(line_recommendation)
            else:
                return "System suggests {} NOT to have the treatment.\n".format(line_recommendation)
    return "Recommendation for {} cannot be calculated due to absence.\n".format(line_recommendation)
#It checks the list and create list. If it suits then it removes the asked name.
def remove():
    line_removed=line[7:-1]
    for i in range(len(create_list)):
        if line_removed == create_list[i][0]:
            create_list.pop(i)
            return "Patient {} is removed.\n".format(line_removed)
    return "Patient {} cannot be removed due to absence.\n".format(line_removed)
#It classifys the create_list's indexes and by the help of format function.
# It converts those infos to a table.
def info_list():
    all_people_list = ""
    first_line= f"{'Patients': <9}{'Diagnosis': <12}{'Disease': <16}" \
                f"{'Disease': <12}{'Treatment': <17}{'Treatment': <5}\n"
    all_people_list += first_line
    second_line = f"{'Name': <9}{'Accuracy': <12}{'Name': <16}{'Incidence': <12}{'Name': <17}{'Risk'}\n"
    all_people_list += second_line
    tires = f"{'-------------------------------------------------------------------------'}\n"
    all_people_list += tires
    for index in range(len(create_list)):
        patient_name = create_list[index][0]
        diagnosis_accuracy = str(float(create_list[index][1])*100) + "%"
        disease_name = create_list[index][2]
        disease_incidence = create_list[index][3]
        treatment_name = create_list[index][4]
        treatment_ris = float(create_list[index][5])*100
        treatment_risk = format(treatment_ris,"g")
        each_person_list = f"{patient_name: <8}{diagnosis_accuracy:<12}{disease_name: <16}" \
                           f"{disease_incidence: <12}{treatment_name: <17}{treatment_risk}%\n"
        all_people_list += each_person_list
    return all_people_list
#It writes the outputs of the function to the requested file.
def write_output(i):
    with open("doctors_aid_outputs.txt","a", encoding="utf-8") as o:
        o.write(i)
#this line will take information from the doctors_aid_inputs.txt
output_doc = open("doctors_aid_outputs.txt","w", encoding="utf-8")
output_doc.close()
with open("doctors_aid_inputs.txt","a",encoding="utf-8") as f:
    f.write(" ")
with open("doctors_aid_inputs.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while True:
        if "create" in line:
            write_output(create())
            line = f.readline()
        elif "recommendation" in line:
            write_output(recommendation())
            line = f.readline()
        elif "list" in line:
            write_output(info_list())
            line = f.readline()
        elif "remove" in line:
            write_output(remove())
            line = f.readline()
        elif "probability" in line:
            write_output(probability())
            line = f.readline()
        else:
            break