# GenerateK-merCompositionOfAString Implementation

with open("Rosalind_data_p23.txt") as f:
    k = int(f.readline())
    text = f.readline()

def kMerComposition(text, k):
    composition = []
    for i in range(0, len(text)-k+1):
        composition.append(text[i:i+k])
    return composition

print("\n".join(str(x) for x in kMerComposition(text, k)))