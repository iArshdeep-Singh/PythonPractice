# symmetic_difference(): Returns a new set containing the elements that are present in
# either set, but not in both.

iSet = {"a", "e", "i", "o", "u"}
iSetX = {"a", "b", "c", "d", "e"}

iSymmetric_difference = iSet.symmetric_difference(iSetX)

print(iSymmetric_difference)
