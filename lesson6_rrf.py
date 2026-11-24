meaning_list = ["diabetes_card", "hyperglycemia_card", "kidney_card"]
words_list   = ["glucose_test_card", "diabetes_card", "insulin_card"]

k = 60
scores = {}

for helper_list in (meaning_list, words_list):
    for place, card in enumerate(helper_list, start=1):
        points = 1 / (k + place)
        scores[card] = scores.get(card, 0) + points
        print(f"{card:20} got place {place} -> +{points:.4f} points")

print("\nFinal mixed list:")
for card, total in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{card:20} {total:.4f}")