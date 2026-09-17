# Step 1: Preloaded Feedbacks (Given Data)
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        '  Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# Step 2: Add More Feedbacks
n = int(input("How many more feedbacks would you like to add? "))
next_s_no = feedback_data['S_No'][-1] + 1

for i in range(n):
    print(f"\nEnter details for feedback #{i + 1}")
    name = input("Name: ")
    feedback_text = input("Feedback: ")
    rating = int(input("Rating (1-5): "))

    feedback_data['S_No'].append(next_s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback_text)
    feedback_data['Rating'].append(rating)
    next_s_no += 1

# Step 3: Text Cleaning
def clean_text(text):
    # Remove punctuation
    punctuations = ['.', ',', '!', '?']
    for p in punctuations:
        text = text.replace(p, '')

    # Replace multiple spaces with a single space
    text = ' '.join(text.split())

    # Remove leading/trailing spaces (already handled by split/join, but for safety)
    text = text.strip()

    # Convert to lowercase
    text = text.lower()

    return text

feedback_data['Feedback'] = [clean_text(fb) for fb in feedback_data['Feedback']]

# Step 4: Word Count Insights
def count_word_in_feedbacks(word):
    word = word.lower()
    count = 0
    for feedback in feedback_data['Feedback']:
        words = feedback.split()
        if word in words:
            count += 1
    return count

print("\n--- Word Count Insights ---")
print(f"Feedbacks containing 'good': {count_word_in_feedbacks('good')}")
print(f"Feedbacks containing 'poor': {count_word_in_feedbacks('poor')}")
print(f"Feedbacks containing 'excellent': {count_word_in_feedbacks('excellent')}")

# Step 5: Final Summary & Insights

# Display the final cleaned feedback_data
print("\n--- Final Cleaned Feedback Data ---")
for key, values in feedback_data.items():
    print(f"{key}: {values}")

# Average rating
average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(f"\nAverage Rating: {average_rating:.2f}")

# Feedback with the longest comment (by word count)
longest_index = 0
max_word_count = 0
for i, feedback in enumerate(feedback_data['Feedback']):
    word_count = len(feedback.split())
    if word_count > max_word_count:
        max_word_count = word_count
        longest_index = i

print("\nLongest Feedback:")
print(f"Name: {feedback_data['Name'][longest_index]}")
print(f"Feedback: {feedback_data['Feedback'][longest_index]}")
print(f"Word Count: {max_word_count}")

# Unique words used across all feedbacks
unique_words = set()
for feedback in feedback_data['Feedback']:
    for word in feedback.split():
        unique_words.add(word)

print("\nUnique Words Used Across All Feedbacks:")
print(sorted(unique_words))

# Optional: Sort feedbacks by rating (highest to lowest)
combined = list(zip(feedback_data['Rating'], feedback_data['S_No'], feedback_data['Name'], feedback_data['Feedback']))
sorted_combined = sorted(combined, key=lambda x: x[0], reverse=True)

print("\n--- Feedbacks Sorted by Rating (Highest to Lowest) ---")
for rating, s_no, name, feedback in sorted_combined:
    print(f"S_No: {s_no} | Name: {name} | Rating: {rating} | Feedback: {feedback}")