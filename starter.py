def process_stories(file_path):
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Split the data into stories using the delimiter
    stories = data.split('<|endoftext|>')

    # Process each story
    for i, story in enumerate(stories):
        if story.strip():  # Check if the story is not just whitespace
            print(f"Story {i+1}:")
            print(story.strip())  # Print the story, stripping any leading/trailing whitespace
            print("----")  # Separator between stories for clarity

# Specify the path to your file
file_path = 'TinyStories-valid.txt'
process_stories(file_path)
