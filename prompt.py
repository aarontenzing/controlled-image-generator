import csv
from random import choices

with open('descriptions\\details.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    shots = []
    appearance = []
    person = []
    details1_box = []
    details2_box = []
    company = []
    background = []
    weather = []

    # Parse the CSV data into corresponding lists
    current_list = None
    for line in reader:
        if line:
            line = line[0]
            # print(line)
            if line.startswith('#'):
                current_list = line.strip('#').strip()
            else:
                if current_list == 'shots':
                    shots.append(line.strip())    
                elif current_list == 'appearance':
                    appearance.append(line.strip())
                elif current_list == 'person':
                    person.append(line.strip())
                elif current_list == 'details1_box':
                    details1_box.append(line.strip())
                elif current_list == 'details2_box':
                    details2_box.append(line.strip())
                elif current_list == 'company':
                    company.append(line.strip())
                elif current_list == 'background':
                    background.append(line.strip())
                elif current_list == 'weather':
                    weather.append(line.strip())

    
def prompt_generator():
    personType = choices(person)[0]
    pronoun = 'his' if personType in ['boy', 'man'] else 'her'
    pronoun = choices(['his', 'her'])[0] if personType == 'child' else pronoun
    return f"A medium shot view of {choices(appearance)[0]} {personType} holding a {choices(details1_box)[0]} cardboard box {choices(details2_box)[0]} from {choices(company)[0]} webshop in {pronoun} hands, standing in front of a {choices(background)[0]} background, the weather is {choices(weather)[0]}, high photorealistic quality."

def prompt_generator_no_human():
    return f"A medium shot view of a {choices(details1_box)[0]} cardboard box {choices(details2_box)[0]} from {choices(company)[0]} webshop, in front of a {choices(background)[0]} background, the weather is {choices(weather)[0]}, high photorealistic quality."

if __name__ == '__main__':
    print(prompt_generator())