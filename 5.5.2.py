from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)
print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(breakfast_counter & lunch_counter)
print(breakfast_counter | lunch_counter)