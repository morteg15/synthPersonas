
import toml

def update_profile_answers(profile_path):
    with open(profile_path, 'r', encoding='utf-8') as f:
        profile = toml.load(f)

    for q_and_a in profile["question_and_answer"]:
        question = q_and_a["question"]
        answer = q_and_a["answer"]

        options_start = question.find('[')
        options_end = question.find(']')
        options = question[options_start+1:options_end].split(', ')
        
        for option in options:
            if option in answer:
                break
        else:
            # Hvis ingen alternativer ble funnet i svaret, la brukeren velge et
            print(question)
            for idx, option in enumerate(options):
                print(f"{idx+1}. {option}")
            
            choice = int(input("Velg et alternativ: ")) - 1
            updated_answer = answer + f" [{options[choice]}]"
            q_and_a["answer"] = updated_answer

    # Lagre endringer tilbake til TOML-filen
    with open(profile_path, 'w', encoding='latin1') as f:
        toml.dump(profile, f)

profile_path = "path_to_your_toml_file.toml"
update_profile_answers(profile_path)
