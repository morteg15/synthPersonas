#Q1
questions_v1_v6 = {
    "v1": "Hvor viktig er hvert av følgende områder i livet ditt? Arbeid",
    "v2": "Hvor viktig er hvert av følgende områder i livet ditt? Familie",
    "v3": "Hvor viktig er hvert av følgende områder i livet ditt? Venner og bekjente",
    "v4": "Hvor viktig er hvert av følgende områder i livet ditt? Fritid",
    "v5": "Hvor viktig er hvert av følgende områder i livet ditt? Politikk",
    "v6": "Hvor viktig er hvert av følgende områder i livet ditt? Religion"
}

answer_mapping_v1_v6 = {
    1.0: "Svært viktig",
    2.0: "Ganske viktig",
    3.0: "Ikke viktig",
    4.0: "Slett ikke viktig",
    8.0: "Vet ikke",
    9.0: "Ikke svart"
}

#Q2
questions_v7 ={
    "v7": "Alt i alt, vil du si at du er:"
}

answer_mapping_v7 = {
    1.0: "Meget lykkelig",
    2.0: "Ganske lykkelig",
    3.0: "Ikke spesielt lykkelig",
    4.0: "Slett ikke lykkelig"
}

#Q3
questions_v8 = {
    "v8": "Hvordan vil du beskrive din nåværende allmenne helsetilstand?"
}

answer_mapping_v8 = {
    1.0: "Meget bra",
    2.0: "Bra",
    3.0: "Middels",
    4.0: "Dårlig",
    5.0: "Meget dårlig",
    8.0: "Vet ikke (spontant)",
    9.0: "Ikke svar (spontant)"
}

#Q4

questions_v9_v20 = {
    "v9": "kan du fortelle meg om du er medlem i noen av disse? A Kirkelig eller religiøs organisasjon",
    "v10": "kan du fortelle meg om du er medlem i noen av disse? B Kunst-, kultur-, musikk- eller studiegruppe",
    "v11": "kan du fortelle meg om du er medlem i noen av disse? C Fagforening",
    "v12": "kan du fortelle meg om du er medlem i noen av disse? D Politisk parti eller partipolitisk forening",
    "v13": "kan du fortelle meg om du er medlem i noen av disse? E Naturvern-, miljøvern- eller dyrevernsorganisasjon",
    "v14": "kan du fortelle meg om du er medlem i noen av disse? F Yrkesorganisasjon",
    "v15": "kan du fortelle meg om du er medlem i noen av disse? G Idrettslag, tur- eller trimforening",
    "v16": "kan du fortelle meg om du er medlem i noen av disse? H Humanitær eller veldedig organisasjon",
    "v17": "kan du fortelle meg om du er medlem i noen av disse? I Forbrukerorganisasjon",
    "v18": "kan du fortelle meg om du er medlem i noen av disse? J Selvhjelpsgruppe, støttegruppe",
    "v19": "Kkan du fortelle meg om du er medlem i noen av disse?  Andre frivillige lag og organisasjoner",
    "v20": "kan du fortelle meg om du er medlem i noen av disse? L Ingen (spontant)"
}

answer_mapping_v9_v20 = {
    1.0: "Nevnt", 2.0: "Ikke nevnt", 8.0: "Vet ikke", 9.0: "Ikke svart"}


#Q5

questions_v21 = {
    "v21": "Har du utført frivillig arbeid de siste 6 måneder?"
}

answer_mapping_v21 = {
    1.0: "Ja",
    2.0: "Nei",
    8.0: "Vet ikke (spontant)",
    9.0: "Ikke svar (spontant)"
}


#Q6

questions_v22_v30 = {
    "v22": "Vil du fortelle hvilke du ikke vil ha som nabo? A Personer av en annen rase",
    "v23": "Vil du fortelle hvilke du ikke vil ha som nabo? B Alkoholikere",
    "v24": "Vil du fortelle hvilke du ikke vil ha som nabo C Innvandrere/fremmedarbeidere",
    "v25": "Vil du fortelle hvilke du ikke vil ha som nabo D Narkomane",
    "v26": "Vil du fortelle hvilke du ikke vil ha som nabo E Homoseksuelle",
    "v28": "Vil du fortelle hvilke du ikke vil ha som nabo G Muslimer",
    "v29": "Vil du fortelle hvilke du ikke vil ha som nabo H Jøder",
    "v30": "Vil du fortelle hvilke du ikke vil ha som nabo I Sigøynere/Romfolk"
}

# The answer mapping remains the same as before, i.e., 
answer_mapping_v22_v30 = {1.0: "Nevnt", 2.0: "Ikke nevnt", 8.0: "Vet ikke", 9.0: "Ikke svart"}

#Q7

questions_v31 = {
    "v31": "Synes du at man generelt kan stole på de fleste mennesker, eller synes du man ikke kan være forsiktig nok i omgangen med mennesker?"
}

answer_mapping_v31 = {
    1.0: "Man kan stole på de fleste",
    2.0: "Man kan ikke være forsiktig nok",
    8.0: "Vet ikke (spontant)",
    9.0: "Ikke svar (spontant)"
}

#Q8


questions_v32_v37 = {
    "v32": "Kan du fortelle om du stoler på følgende grupper av personer? Familien din",
    "v33": "Kan du fortelle om du stoler på følgende grupper av personer? Personer i nabolaget ditt",
    "v34": "Kan du fortelle om du stoler på følgende grupper av personer? Personer du kjenner personlig",
    "v35": "Kan du fortelle om du stoler på følgende grupper av personer? Personer du møter for første gang",
    "v36": "Kan du fortelle om du stoler på følgende grupper av personer? Personer av en annen religion",
    "v37": "Kan du fortelle om du stoler på følgende grupper av personer? Personer med en annen nasjonalitet"
}



answer_mapping_v32_to_v37 = {
    1.0: "Stoler fullstendig på",
    2.0: "Stoler noe på",
    3.0: "Stoler lite på",
    4.0: "Stoler ikke på",
    8.0: "Vet ikke",
    9.0: "Ikke svart"
}


#Q9

questions_v38 = {
    "v38": "En del mennesker mener de har full valgfrihet og selv kan bestemme hvordan livet skal bli. Andre mennesker mener at det de selv gjør har liten innvirkning på hva som skjer med dem. Vil du se på denne skalaen fra 1 til 10 og vise hvor mye valgfrihet og selvbestemmelse du mener du har når det gjelder hvordan livet ditt blir?"
}

answer_mapping_v38 = {
    1.0: "Overhodet ingen",
    2.0: "2",
    3.0: "3",
    4.0: "4",
    5.0: "5",
    6.0: "6",
    7.0: "7",
    8.0: "8",
    9.0: "9",
    10.0: "En hel del",
    88.0: "Vet ikke",
    99.0: "Ikke svart"
}


# Q10

questions_v39 = {
    "v39": "Alt i alt, hvor tilfreds er du med livet ditt for tiden? Svar ved hjelp av denne skalaen fra 1 til 10."
}

answer_mapping_v39 = {
    1.0: "Svært utilfreds",
    2.0: "2",
    3.0: "3",
    4.0: "4",
    5.0: "5",
    6.0: "6",
    7.0: "7",
    8.0: "8",
    9.0: "9",
    10.0: "Svært tilfreds",
    88.0: "Vet ikke",
    99.0: "Ikke svart"
}

# Q11

questions_v40_v45 = {
    "v40": "hvilken forhold med jobben anser du som viktig God lønn",
    "v41": "hvilken forhold med jobben anser du som viktig God arbeidstid",
    "v42": "hvilken forhold med jobben anser du som viktig Mulighet til å ta initiativ",
    "v43": "hvilken forhold med jobben anser du som viktig Lang ferie",
    "v44": "hvilken forhold med jobben anser du som viktig Et arbeid som gir følelsen av å utrette noe",
    "v45": "hvilken forhold med jobben anser du som viktig En ansvarsfull jobb",
    "v45a": "Ingen av disse (spontant)"
}

answer_mapping_v40_v45 = {
    1.0: "Nevnt",
    2.0: "Ikke nevnt",
    8.0: "Vet ikke",
    9.0: "Ikke svart"
}


def transform_to_qa_structure(questions, answer_mapping):
    structure = {}

    for q_key, q_value in questions.items():
            structure[q_value] = answer_mapping[q_key]


    return structure


# individual mappings for specific questions
specific_mappings = [
    [questions_v1_v6, answer_mapping_v1_v6],
    [questions_v7, answer_mapping_v7],
    [questions_v8, answer_mapping_v8],
    [questions_v9_v20, answer_mapping_v9_v20],
    [questions_v21, answer_mapping_v21],
    [questions_v22_v30, answer_mapping_v22_v30],
    [questions_v31, answer_mapping_v31],
    [questions_v32_v37, answer_mapping_v32_to_v37],
    [questions_v38, answer_mapping_v38],
    [questions_v39, answer_mapping_v39],
    [questions_v40_v45, answer_mapping_v40_v45]
]

# merge the answer_mappings
survey = {}
for combination in specific_mappings:
    for key in combination[0]:
        survey[key] = {combination[0][key] : combination[1]}
print(survey)


import json
# Save data to a JSON file
with open('data//gss//data.json', 'w', encoding='utf8') as outfile:
    json.dump(survey, outfile, indent=4, ensure_ascii=False)