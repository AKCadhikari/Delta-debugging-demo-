import json

def parse_json(data):
    """Try to parse JSON. Raises ValueError on failure."""
    return json.loads(data)

failing_input = "{ [ 1, 2, 3, invalid, data, here, ..., ] }"
def test(input_str):
    """Test function: returns True if input still fails, False otherwise"""
    try:
        parse_json(input_str)
        return False  # success -> not failing
    except Exception:
        return True   # still failing

def ddmin(data):
    """Delta Debugging algorithm: minimize failing input"""
    n = 2
    while len(data) >= 2:
        start = 0
        subset_length = len(data) // n
        some_complement_is_failing = False

        while start < len(data):
            subset = data[start:start + subset_length]
            complement = data[:start] + data[start + subset_length:]
            
            if test(subset):
                data = subset
                n = max(n - 1, 2)
                some_complement_is_failing = True
                break
            elif test(complement):
                data = complement
                n = max(n - 1, 2)
                some_complement_is_failing = True
                break

            start += subset_length

        if not some_complement_is_failing:
            if n == len(data):
                break
            n = min(n * 2, len(data))
    return data
if __name__ == "__main__":
    failing_input = "{ [ 1, 2, invalid, data, here, ], nonsense }"
    print("Original input:", failing_input)
    minimized = ddmin(failing_input)
    print("Minimized failing input:", minimized)
