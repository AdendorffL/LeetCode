class Solution:
    def romanToInt(self, s: str) -> int:
        # Conversion
        c = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Roman Numeral input
        split = list(s.upper())
        # Converted Number list
        cnl = []
        for key in split:
            if key in c:
                # Check for smaller numbers eg. IV = 4
                if len(cnl) != 0 and c[key] > cnl[-1]:
                    result = c[key] - cnl[-1]
                    cnl.remove(cnl[-1])
                    cnl.append(result)
                # Append converted number to list if not special number.
                else:
                    cnl.append(c[key])

        return sum(cnl)
