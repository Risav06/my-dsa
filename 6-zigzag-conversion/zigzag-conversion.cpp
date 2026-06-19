class Solution {
public:
    string convert(string s, int numRows) {
        // Edge case: if only one row, the string remains unchanged
        if (numRows == 1) return s;
        
        // Create a vector of strings for each row
        vector<string> rows(min(numRows, (int)s.length()));
        
        int currentRow = 0;
        bool goingDown = false;
        
        // Traverse the string and place each character in the appropriate row
        for (char c : s) {
            rows[currentRow] += c;
            
            // Change direction when we reach the top or bottom row
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }
            
            // Move to the next row
            currentRow += goingDown ? 1 : -1;
        }
        
        // Concatenate all rows
        string result;
        for (string row : rows) {
            result += row;
        }
        
        return result;
    }
};