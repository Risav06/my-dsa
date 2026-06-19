class Solution:                     # No indentation (top level)
    def largestAltitude(self, gain): # Indented 4 spaces (inside class)
        current = 0                  # Indented 8 spaces (inside method)
        max_altitude = 0             # Indented 8 spaces
        
        for g in gain:               # Indented 8 spaces (inside method)
            current += g             # Indented 12 spaces (inside loop)
            if current > max_altitude:  # Indented 12 spaces
                max_altitude = current  # Indented 16 spaces (inside if)
        
        return max_altitude          # Indented 8 spaces (inside method)