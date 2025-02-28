import json

# Load the input JSONL file
input_file = "../Datengenerierung/Bauwesen-v1.json"
output_file = "../Datengenerierung/instruction_dataset.json"

def process_entry(entry):
    messages = entry["messages"]
    
    # Extract user messages
    user_messages = [msg["content"] for msg in messages if msg["role"] == "user"]
    
    # Extract assistant messages
    assistant_messages = [msg["content"] for msg in messages if msg["role"] == "assistant"]
    
    # Ensure there is at least one user and one assistant message
    if not user_messages or not assistant_messages:
        return None
    
    # Last user sentence as input
    input_text = user_messages[0].split(".")[-1]
    print(user_messages)
    
    # Context is all previous user sentences (if any)
    context = "\n".join(user_messages[0].split(".")[:-1]) if len(user_messages[0].split(".")) > 1 else ""
    
    # Assistant response as output
    output_text = "\n".join(assistant_messages)
    
    return {
        "instruction": "Answer the question based on the provided context.",
        "input": input_text,
        "context": context,
        "output": output_text
    }

# Process the dataset
with open(input_file, "r", encoding="utf-8") as f:
    print(f)
    processed_data = json.load(f)
    
processed_data_2 = [] 
for elem in processed_data:
    processed_data_2.append(process_entry(elem))

# Save the transformed dataset
with open(output_file, "w", encoding="utf-8") as f:
    for item in processed_data_2:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Processed {len(processed_data_2)} entries and saved to {output_file}")
