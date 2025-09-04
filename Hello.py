first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

if not first_name:  # If no first name was entered
    # Try to guess based on last name (not reliable) or just ask
    gender = input("Is this Mr. or Mrs.? ").strip().lower()
    if gender in ["mr"or "mr.", "mister"]:
        first_name = "Mr."
    elif gender in ["ms", "ms."]:
        first_name = "Ms."
    elif gender in ["mrs.", "mrs"]:
        first_name = "Mrs."
    else:
        first_name = "Friend"  # fallback if unclear

output = f"hello, {first_name} {last_name}"
print(output)

