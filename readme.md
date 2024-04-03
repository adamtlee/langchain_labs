# Pet Name Generator using LangChain 🐾

## Overview
This Python script leverages the **LangChain** library to generate creative and unique pet names for your beloved furry companions. Whether you're adopting a new dog, cat, or any other pet, this tool will provide you with fun and imaginative name suggestions.

## How It Works
1. **LangChain Setup**:
   - The script initializes an instance of the **OpenAI** language model from the **LangChain** library.
   - It sets the temperature (a hyperparameter controlling randomness) to 0.7 for balanced creativity.

2. **Prompt Template**:
   - The script defines a prompt template using the `PromptTemplate` class.
   - The template includes an input variable (`animal_type`) that allows customization.

3. **Name Generation**:
   - The `LLMChain` (Language Learning Model Chain) is created with the specified prompt template.
   - When you run the script and provide an `animal_type` (e.g., "dog"), it generates five pet names related to that type.

4. **Example Output**:
   - For the input "dog," the script might suggest names like "Biscuit," "Coco," "Winston," "Luna," and "Oliver."

## Usage
1. Install the required dependencies (e.g., OpenAI, LangChain).
2. Customize the prompt template or modify the script as needed.
3. Run the script, passing your desired `animal_type` as an argument.
4. Enjoy the delightful pet names it generates!

Remember, these names are just for fun, so feel free to get creative and choose the one that resonates with you and your pet. Happy naming! 🐶🐱🐾
