import pandas as pd
import json

# Load the input JSONL file
input_file = 'Daten/QA-JVA.xlsx'
output_file = "Datengenerierung/instruction_dataset_qa.json"

def process_entry(entry):
    
    # Last user sentence as input
    input_text = entry["Frage"]
    
    # Context is all previous user sentences (if any)
    context = f"Der Kontext der Frage ist '{entry['Thema']}'"
    
    # Assistant response as output
    output_text = entry["Antwort"]
    
    return {
        "instruction": "Beantworte die Frage im vorgegebenen Kontext.",
        "input": input_text,
        "context": context,
        "output": output_text
    }
    

# Load the Excel file
df = pd.read_excel(input_file)

# Convert the DataFrame to a dictionary
data_dict = df.to_dict(orient='records')  # Each row becomes a dictionary in a list 

processed_data = []

for elem in data_dict:
    processed_data.append(process_entry(elem))
    
print(processed_data)

# Save the transformed dataset
with open(output_file, "w", encoding="utf-8") as f:
    for item in processed_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Processed {len(processed_data)} entries and saved to {output_file}")
